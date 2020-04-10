# This file is Copyright (c) 2019 Antony Pavlov <antonynpavlov@gmail.com>
# License: BSD

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform

# IOs ------------------------------------------------------------------

_io = [
    ("clk_50",  0, Pins("AF14"), IOStandard("3.3-V LVTTL")),
    ("clk2_50", 0, Pins("AA16"), IOStandard("3.3-V LVTTL")),
    ("clk3_50", 0, Pins(" Y26"), IOStandard("3.3-V LVTTL")),
    ("clk4_50", 0, Pins(" K14"), IOStandard("3.3-V LVTTL")),

    ("msel", 0, Pins("L8 K6 G6 L7 L9"), IOStandard("3.3-V LVTTL")),  # SW10.1 ... SW10.6

    ("keys", 0, Pins("AA14 AA15 W15 Y16"), IOStandard("3.3-V LVTTL")),  # KEY0 KEY1 KEY2 KEY3

    ("switches", 0, Pins("AB12 AC12 AF9 AF10 AD11 AD12 AE11 AC9 AD10 AE12"), IOStandard("3.3-V LVTTL")),  # SW0 ... SW9

    ("leds", 0, Pins("V16 W16 V17 V18 W17 W19 Y19 W20 W21 Y21"), IOStandard("3.3-V LVTTL")),  # LEDR0 ... LEDR9

    ("hex0", 0, Pins("AE26 AE27 AE28 AG27 AF28 AG28 AH28"), IOStandard("3.3-V LVTTL")),  # HEX0[0] ... HEX0[6]
    ("hex1", 0, Pins("AJ29 AH29 AH30 AG40 AF29 AF30 AD27"), IOStandard("3.3-V LVTTL")),  # HEX1[0] ... HEX1[6]
    ("hex2", 0, Pins("AB23 AE29 AD29 AC28 AD30 AC29 AC30"), IOStandard("3.3-V LVTTL")),  # HEX2[0] ... HEX2[6]
    ("hex3", 0, Pins("AD26 AC27 AD25 AB29 AB25 AB22 AA24"), IOStandard("3.3-V LVTTL")),  # HEX3[0] ... HEX3[6]
    ("hex4", 0, Pins("AA24  Y23  Y24  W22  W24  V23  W25"), IOStandard("3.3-V LVTTL")),  # HEX4[0] ... HEX4[6]
    ("hex5", 0, Pins("V25  AA28  Y27 AB27 AB26 AA26 AA25"), IOStandard("3.3-V LVTTL")),  # HEX5[0] ... HEX5[6]

    ("gpio0", 0, Pins("AC18  Y17 AD17  Y18 AK16 AK18 AK19 AJ19 AJ17 AJ16 AH18 AH17 AG16 AE16 AF16 AG17 AA18 AA19 AE17 AC20 AH19 AJ20 AH20 AK21 AD19 AD20 AE18 AE19 AF20 AF21 AF19 AG21 AF18 AG20 AG18 AJ21"), IOStandard("3.3-V LVTTL")),  # GPIO_0[0] ... GPIO_0[35]
    ("gpio1", 0, Pins("AB18 AA21 AB21 AC23 AD24 AE23 AE24 AF25 AF26 AG25 AG26 AH24 AH27 AJ27 AK29 AK28 AK27 AJ26 AK26 AH25 AJ25 AJ24 AK24 AG23 AK23 AH23 AK22 AJ22 AH22 AG22 AF24 AF23 AE22 AD21 AA20 AC22"), IOStandard("3.3-V LVTTL")),  # GPIO_1[0] ... GPIO_1[35]

    ("aud", 0,
        Subsignal("adclrck", Pins("K8"), IOStandard("3.3-V LVTTL")),  # AUD_ADCLRCK
        Subsignal("adcdat",  Pins("K7"), IOStandard("3.3-V LVTTL")),  # AUD_ADCDAT
        Subsignal("dacrck",  Pins("H8"), IOStandard("3.3-V LVTTL")),  # AUD_DACRCK
        Subsignal("datdac",  Pins("J7"), IOStandard("3.3-V LVTTL")),  # AUD_DACDAT
        Subsignal("xck",     Pins("G7"), IOStandard("3.3-V LVTTL")),  # AUD_XCK
        Subsignal("bclk",    Pins("H7"), IOStandard("3.3-V LVTTL")),  # AUD_BCLK
    ),

    ("i2c_fpga", 0
        Subsignal("sclk", Pins("J12"), IOStandard("3.3-V LVTTL")),  # FPGA_I2C_SCLK
        Subsignal("sdat", Pins("K12"), IOStandard("3.3-V LVTTL")),  # FPGA_I2C_SDAT
    ),

    ("i2c1_hps", 0
        Subsignal("sclk", Pins("E23"), IOStandard("3.3-V LVTTL")),# HPS_I2C1_SCLK
        Subsignal("sdat", Pins("C24"), IOStandard("3.3-V LVTTL")),# HPS_I2C1_SDAT
    ),

    ("i2c2_hps", 0
        Subsignal("sclk", Pins("H23"), IOStandard("3.3-V LVTTL")),# HPS_I2C2_SCLK
        Subsignal("sdat", Pins("A25"), IOStandard("3.3-V LVTTL")),# HPS_I2C2_SDAT
    ),

    ("vga", 0,
        Subsignal("r", Pins("A13 C13 E13 B12 C12 D12 E12 F13"), IOStandard("3.3-V LVTTL")),   # VGA_R[0] ... VGA_R[7]
        Subsignal("g", Pins(" J9 J10 H12 G10 G11 G12 F11 E11"), IOStandard("3.3-V LVTTL")),   # VGA_G[0] ... VGA_G[7]
        Subsignal("b", Pins("B13 G13 H13 F14 H14 F15 G15 J14"), IOStandard("3.3-V LVTTL")),   # VGA_B[0] ... VGA_B[7]
        Subsignal("clk",        Pins("A11"), IOStandard("3.3-V LVTTL")),   # VGA_CLK
        Subsignal("blank_n",    Pins("F10"), IOStandard("3.3-V LVTTL")),   # VGA_BLANK_N
        Subsignal("hs",         Pins("B11"), IOStandard("3.3-V LVTTL")),   # VGA_HS
        Subsignal("vs",         Pins("D11"), IOStandard("3.3-V LVTTL")),   # VGA_VS
        Subsignal("sync_n",     Pins("C10"), IOStandard("3.3-V LVTTL")),   # VGA_SYNC_N
    ),

    ("tv", 0,
        Subsignal("data",   Pins("D2 B1 E2 B2 D1 E1 C2 B3"), IOStandard("3.3-V LVTTL")),   # TD_DATA[0] ... TD_DATA[7]
        Subsignal("hs",     Pins("A5"),  IOStandard("3.3-V LVTTL")),   # TD_HS
        Subsignal("vs",     Pins("A3"),  IOStandard("3.3-V LVTTL")),   # TD_VS
        Subsignal("clk27",  Pins("H15"), IOStandard("3.3-V LVTTL")),   # TD_CLK27
        Subsignal("rst_n",  Pins("F6"),  IOStandard("3.3-V LVTTL")),   # TD_RESET_N
    ),

    ("ir", 0,
        Subsignal("rx", Pins("AA30"), IOStandard("3.3-V LVTTL")),   # IRDA_RXD
        Subsignal("tx", Pins("AB30"), IOStandard("3.3-V LVTTL")),   # IRDA_TXD
    ),

    ("ps2", 0,
        Subsignal("clk",  Pins("AD7"), IOStandard("3.3-V LVTTL")), # PS2_CLK
        Subsignal("dat",  Pins("AE7"), IOStandard("3.3-V LVTTL")), # PS2_DAT
        Subsignal("clk2", Pins("AD9"), IOStandard("3.3-V LVTTL")), # PS2_CLK2
        Subsignal("dat2", Pins("AE9"), IOStandard("3.3-V LVTTL")), # PS2_DAT2
    ),

    ("adc", 0,
        Subsignal("cs_n", Pins("AJ4"), IOStandard("3.3-V LVTTL")), # ADC_CS_N
        Subsignal("dout", Pins("AK3"), IOStandard("3.3-V LVTTL")), # ADC_DOUT
        Subsignal("din",  Pins("AK4"), IOStandard("3.3-V LVTTL")), # ADC_DIN
        Subsignal("sclk", Pins("AK2"), IOStandard("3.3-V LVTTL")), # ADC_SCLK
    ),

    ("serial", 0,
        Subsignal("tx", Pins("AC18"), IOStandard("3.3-V LVTTL")), # JP1 GPIO[0]
        Subsignal("rx", Pins("Y17"),  IOStandard("3.3-V LVTTL")), # JP1 GPIO[1]
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

    ("hps", 0,
        Subsignal("clk1_25", Pins("D25"), IOStandard("3.3-V LVTTL")),
        Subsignal("clk2_25", Pins("F25"), IOStandard("3.3-V LVTTL")),
        Subsignal("nrst", Pins("C27"), IOStandard("3.3-V LVTTL")),  # KEY7 (HPS_WARM_RST_n)
        Subsignal("npor", Pins("F23"), IOStandard("3.3-V LVTTL")),  # KEY5 (HPS_RESET_n)
        Subsignal("gpio_42", Pins("G17"), IOStandard("3.3-V LVTTL")),  # KEY5 (HPS_RESET_PHY)
        Subsignal("gpio_43", Pins("E18"), IOStandard("3.3-V LVTTL")),  # KEY5 (HPS_ENET_RESET_n)
    )

    ("jtag_hps", 0,
        Subsignal("tck", Pins("H22"), IOStandard("3.3-V LVTTL")),
        Subsignal("tms", Pins("A29"), IOStandard("3.3-V LVTTL")),
        Subsignal("tdi", Pins("B27"), IOStandard("3.3-V LVTTL")),
        Subsignal("tdo", Pins("B28"), IOStandard("3.3-V LVTTL")),
    ),

    ("jtag_fpga", 0,
        Subsignal("tck", Pins("AC5"), IOStandard("3.3-V LVTTL")),
        Subsignal("tms", Pins("V9"),  IOStandard("3.3-V LVTTL")),
        Subsignal("tdi", Pins("U8"),  IOStandard("3.3-V LVTTL")),
        Subsignal("tdo", Pins("AB9"), IOStandard("3.3-V LVTTL")),
    ),

]

# Platform -------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name = "clk_50"
    default_clk_period = 1e9/50e6

    def __init__(self):
        AlteraPlatform.__init__(self, "5CSEMA5F31C6", _io)
