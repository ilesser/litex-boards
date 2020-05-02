#!/usr/bin/env python3

# This file is Copyright (c) 2019 Antony Pavlov <antonynpavlov@gmail.com>
# This file is Copyright (c) 2020 Ignacio Lesser <ignacio.lesser@gmail.com>
# License: BSD

import argparse

from migen import Module, Instance, Signal, ClockDomain
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex.build.io import DDROutput

from litex_boards.platforms import de1soc

from litex.soc.cores.clock import CycloneVPLL
from litex.soc.integration.soc_core import SoCCore
from litex.soc.integration.soc_sdram import soc_sdram_args, soc_sdram_argdict
from litex.soc.integration.builder import Builder, builder_args, builder_argdict

from litedram.modules import IS42S16320
from litedram.phy import GENSDRPHY

# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module):
    def __init__(self, platform, sys_clk_freq):
        self.clock_domains.cd_sys    = ClockDomain()
        self.clock_domains.cd_sys_ps = ClockDomain(reset_less=True)

        # # #

        # Clk / Rst
        clk50 = platform.request("clk_50")
        platform.add_period_constraint(clk50, 1e9/50e6)

        # PLL
        self.submodules.pll = pll = CycloneVPLL(speedgrade="-C6")
        pll.register_clkin(clk50, 50e6)
        pll.create_clkout(self.cd_sys,    sys_clk_freq)
        pll.create_clkout(self.cd_sys_ps, sys_clk_freq, phase=90)

        # SDRAM clock
        self.specials += DDROutput(1, 0, platform.request("sdram_clock"), ClockSignal("sys_ps"))

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCore):
    def __init__(self, sys_clk_freq=int(50e6), **kwargs):
        platform = de1soc.Platform()
        super().__init__(platform, clk_freq=sys_clk_freq, **kwargs)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform, sys_clk_freq)

        # HPS DE1-SoC IOs --------------------------------------------------------------------------
        if self.cpu_type == "hps":
            self.add_hps_de1soc_ios()

        # SDR SDRAM --------------------------------------------------------------------------------
        if not self.cpu_type == "hps" and not self.integrated_main_ram_size:
            self.submodules.sdrphy = GENSDRPHY(platform.request("sdram"))
            self.add_sdram("sdram",
                phy                     = self.sdrphy,
                module                  = IS42S16320(sys_clk_freq, "1:1"),
                origin                  = self.mem_map["main_ram"],
                size                    = kwargs.get("max_sdram_size", 0x40000000),
                l2_cache_size           = kwargs.get("l2_size", 8192),
                l2_cache_min_data_width = kwargs.get("min_l2_data_width", 128),
                l2_cache_reverse        = True
            )

    def add_hps_de1soc_ios(self):
        hps_ios = self.platform.request("hps_ios")
        self.cpu.hps_params.update(
            io_hps_io_gpio_inst_GPIO09 = hps_ios.conv_usb_n,
            io_hps_io_gpio_inst_GPIO35 = hps_ios.enet_int_n,
            io_hps_io_gpio_inst_GPIO40 = hps_ios.ltc_gpio,
            io_hps_io_gpio_inst_GPIO48 = hps_ios.i2c_control,
            io_hps_io_gpio_inst_GPIO53 = hps_ios.led,
            io_hps_io_gpio_inst_GPIO54 = hps_ios.key,
            io_hps_io_gpio_inst_GPIO61 = hps_ios.gsensor_int,
        )

# Build --------------------------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="LiteX SoC on DE1-SoC")
    builder_args(parser)
    soc_sdram_args(parser)
    args = parser.parse_args()

    soc = BaseSoC(**soc_sdram_argdict(args))
    builder = Builder(soc, **builder_argdict(args))
    builder.build()


if __name__ == "__main__":
    main()
