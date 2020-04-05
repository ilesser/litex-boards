# This file is Copyright (c) 2019 Antony Pavlov <antonynpavlov@gmail.com>
# License: BSD

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform

# IOs ------------------------------------------------------------------

_io = [
    ("clk_50", 0, Pins("AF14"), IOStandard("3.3-V LVTTL")),
    ("clk2_50", 0, Pins("AA16"), IOStandard("3.3-V LVTTL")),
    ("clk3_50", 0, Pins("Y26"), IOStandard("3.3-V LVTTL")),
    ("clk4_50", 0, Pins("K14"), IOStandard("3.3-V LVTTL")),

    ("hps", 0,
        Subsignal("clk1_25", Pins("D25"), IOStandard("3.3-V LVTTL")),
        Subsignal("clk2_25", Pins("F25"), IOStandard("3.3-V LVTTL")),
        Subsignal("nrst", Pins("C27"), IOStandard("3.3-V LVTTL")),  # KEY7 (HPS_WARM_RST_n)
        Subsignal("npor", Pins("F23"), IOStandard("3.3-V LVTTL")),  # KEY5 (HPS_RESET_n)
        Subsignal("gpio_42", Pins("G17"), IOStandard("3.3-V LVTTL")),  # KEY5 (HPS_RESET_PHY)
        Subsignal("gpio_43", Pins("E18"), IOStandard("3.3-V LVTTL")),  # KEY5 (HPS_ENET_RESET_n)
    )

    ("keys", 0, Pins("AA14 AA15 W15 Y16"), IOStandard("3.3-V LVTTL")),  # KEY0 KEY1 KEY2 KEY3

    ("switches", 0, Pins("AB12 AC12 AF9 AF10 AD11 AD12 AE11 AC9 AD10 AE12"), IOStandard("3.3-V LVTTL")),  # SW0 ... SW9

    ("leds", 0, Pins("V16 W16 V17 V18 W17 W19 Y19 W20 W21 Y21"), IOStandard("3.3-V LVTTL")),  # LEDR0 ... LEDR9

    ("hex0", 0, Pins("AE26 AE27 AE28 AG27 AF28 AG28 AH28"), IOStandard("3.3-V LVTTL")),  # HEX0[0] ... HEX0[6]
    ("hex1", 0, Pins("AJ29 AH29 AH30 AG40 AF29 AF30 AD27"), IOStandard("3.3-V LVTTL")),  # HEX1[0] ... HEX1[6]
    ("hex2", 0, Pins("AB23 AE29 AD29 AC28 AD30 AC29 AC30"), IOStandard("3.3-V LVTTL")),  # HEX2[0] ... HEX2[6]
    ("hex3", 0, Pins("AD26 AC27 AD25 AB29 AB25 AB22 AA24"), IOStandard("3.3-V LVTTL")),  # HEX3[0] ... HEX3[6]
    ("hex4", 0, Pins("AA24  Y23  Y24  W22  W24  V23  W25"), IOStandard("3.3-V LVTTL")),  # HEX4[0] ... HEX4[6]
    ("hex5", 0, Pins(""), IOStandard("3.3-V LVTTL")),  # HEX5[0] ... HEX5[6]

    ("serial", 0,
        Subsignal("tx", Pins("AC18"), IOStandard("3.3-V LVTTL")), # JP1 GPIO[0]
        Subsignal("rx", Pins("Y17"), IOStandard("3.3-V LVTTL"))   # JP1 GPIO[1]
    ),

    ("sdram_clock", 0, Pins("AH12"), IOStandard("3.3-V LVTTL")),
    ("sdram", 0,
        Subsignal("a", Pins("AK14 AH14 AG15 AE14 AB15 AC14 AD14 AF15 AH15 AG13 AG12 AH13 AJ14")),
        Subsignal("ba", Pins("AF13 AJ12")),
        Subsignal("cs_n", Pins("AG11")),
        Subsignal("cke", Pins("AK13")),
        Subsignal("ras_n", Pins("AE13")),
        Subsignal("cas_n", Pins("AF11")),
        Subsignal("we_n", Pins("AA13")),
        Subsignal("dq", Pins("AK6 AJ7 AK7 AK8 AK9 AG10 AK11 AJ11 AH10 AJ10 AJ9 AH9 AH8 AH7 AJ6 AJ5")),
        Subsignal("dm", Pins("AB13 AK12")),
        IOStandard("3.3-V LVTTL")
    ),
]

# Platform -------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name = "clk_50"
    default_clk_period = 1e9/50e6

    def __init__(self):
        AlteraPlatform.__init__(self, "5CSEMA5F31C6", _io)
