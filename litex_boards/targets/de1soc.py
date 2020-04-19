#!/usr/bin/env python3

# This file is Copyright (c) 2019 Antony Pavlov <antonynpavlov@gmail.com>
# License: BSD

import argparse

from migen import Module, Instance, Signal, ClockDomain
from migen.genlib.resetsync import AsyncResetSynchronizer

from litex_boards.platforms import de1soc

from litex.soc.integration.soc_sdram import soc_sdram_args, soc_sdram_argdict
from litex.soc.integration.soc_cyclonev import SoCCycloneV, soc_cyclonev_args, soc_cyclonev_argdict
from litex.soc.integration.builder import Builder, builder_args, builder_argdict

from litedram.modules import IS42S16320
from litedram.phy import GENSDRPHY

# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module):
    def __init__(self, platform):
        self.clock_domains.cd_sys    = ClockDomain()
        self.clock_domains.cd_sys_ps = ClockDomain(reset_less=True)

        # # #

        # Clk / Rst
        clk50 = platform.request("clk_50")
        platform.add_period_constraint(clk50, 1e9/50e6)

        # PLL
        pll_locked  = Signal()
        pll_clk_out = Signal(6)
        self.specials += \
            Instance("ALTPLL",
                p_BANDWIDTH_TYPE         = "AUTO",
                p_CLK0_DIVIDE_BY         = 1,
                p_CLK0_DUTY_CYCLE        = 50,
                p_CLK0_MULTIPLY_BY       = 1,
                p_CLK0_PHASE_SHIFT       = "0",
                p_CLK1_DIVIDE_BY         = 1,
                p_CLK1_DUTY_CYCLE        = 50,
                p_CLK1_MULTIPLY_BY       = 1,
                p_CLK1_PHASE_SHIFT       = "5000", # 90°
                p_COMPENSATE_CLOCK       = "CLK0",
                p_INCLK0_INPUT_FREQUENCY = 20000,
                p_OPERATION_MODE         = "NORMAL",
                i_INCLK                  = clk50,
                o_CLK                    = pll_clk_out,
                i_ARESET                 = 0,
                i_CLKENA                 = 0x3f,
                i_EXTCLKENA              = 0xf,
                i_FBIN                   = 1,
                i_PFDENA                 = 1,
                i_PLLENA                 = 1,
                o_LOCKED                 = pll_locked,
            )
        self.comb += [
            self.cd_sys.clk.eq(pll_clk_out[0]),
            self.cd_sys_ps.clk.eq(pll_clk_out[1]),
        ]
        self.specials += AsyncResetSynchronizer(self.cd_sys, ~pll_locked)

        # SDRAM clock
        self.comb += platform.request("sdram_clock").eq(self.cd_sys_ps.clk)

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCCycloneV):
    def __init__(self, sys_clk_freq=int(50e6), **kwargs):
        assert sys_clk_freq == int(50e6)
        platform = de1soc.Platform()
        super().__init__(platform, clk_freq=sys_clk_freq, **kwargs)

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform)

        # HPS DE1-SoC IOs --------------------------------------------------------------------------
        if self.hps:
            self.add_hps_de1soc_ios()

        # SDR SDRAM --------------------------------------------------------------------------------
        if not self.hps and not self.integrated_main_ram_size:
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
        self.hps_params.update(
            io_hps_io_gpio_inst_GPIO09 = hps_ios.conv_usb_n,
            io_hps_io_gpio_inst_GPIO35 = hps_ios.enet_int_n,
            io_hps_io_gpio_inst_GPIO40 = hps_ios.ltc_gpio,
            io_hps_io_gpio_inst_GPIO48 = hps_ios.i2c_control,
            io_hps_io_gpio_inst_GPIO53 = hps_ios.led,
            io_hps_io_gpio_inst_GPIO54 = hps_ios.key,
            io_hps_io_gpio_inst_GPIO61 = hps_ios.gsensor_int,
        )

# Build --------------------------------------------------------------------------------------------

def base_soc_parser():
    parser = argparse.ArgumentParser(
        description="LiteX SoC on DE1-SoC",
        conflict_handler='resolve',
    )
    builder_args(parser)
    soc_cyclonev_args(parser)
    soc_sdram_args(parser)
    return parser

def base_soc_argdict(args):
    soc_cyclonev_dict = soc_cyclonev_argdict(args)
    soc_sdram_dict = soc_sdram_argdict(args)
    soc_cyclonev_dict.update(soc_sdram_dict)
    return soc_cyclonev_dict

def main():
    parser = base_soc_parser()
    args = parser.parse_args()

    soc = BaseSoC(**base_soc_argdict(args))
    builder = Builder(soc, **builder_argdict(args))
    builder.build()


if __name__ == "__main__":
    main()
