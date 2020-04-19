# This file is Copyright (c) 2019 Antony Pavlov <antonynpavlov@gmail.com>
# This file is Copyright (c) 2020 Ignacio Lesser <ignacio.lesser@gmail.com>
# License: BSD

import os

from litex.build.generic_platform import Pins, IOStandard, Subsignal
from litex.build.altera import AlteraPlatform

# IOs ------------------------------------------------------------------

_io = [
    ("clk_50",  0, Pins("AF14"), IOStandard("3.3-V LVTTL")), # CLK0P
    ("clk2_50", 0, Pins("AA16"), IOStandard("3.3-V LVTTL")), # CLK2P
    ("clk3_50", 0, Pins(" Y26"), IOStandard("3.3-V LVTTL")), # CLK4P
    ("clk4_50", 0, Pins(" K14"), IOStandard("3.3-V LVTTL")), # CLK6P

    ("msel", 0, Pins("L8 K6 G6 L7 L9"), IOStandard("3.3-V LVTTL")),  # MSEL[0:4]

    ("fan_ctrl", 0, Pins("AA12"), IOStandard("3.3-V LVTTL")),  # FAN_CTRL

    ("keys", 0, Pins("AA14 AA15 W15 Y16"), IOStandard("3.3-V LVTTL")),  # KEY0 KEY1 KEY2 KEY3

    ("switches", 0, Pins("AB12 AC12 AF9 AF10 AD11 AD12 AE11 AC9 AD10 AE12"), IOStandard("3.3-V LVTTL")),  # SW[0:9]

    ("leds", 0, Pins("V16 W16 V17 V18 W17 W19 Y19 W20 W21 Y21"), IOStandard("3.3-V LVTTL")),  # LEDR[0:9]

    ("hex", 0, Pins("AE26 AE27 AE28 AG27 AF28 AG28 AH28"), IOStandard("3.3-V LVTTL")),  # HEX0[0:6]
    ("hex", 1, Pins("AJ29 AH29 AH30 AG40 AF29 AF30 AD27"), IOStandard("3.3-V LVTTL")),  # HEX1[0:6]
    ("hex", 2, Pins("AB23 AE29 AD29 AC28 AD30 AC29 AC30"), IOStandard("3.3-V LVTTL")),  # HEX2[0:6]
    ("hex", 3, Pins("AD26 AC27 AD25 AB29 AB25 AB22 AA24"), IOStandard("3.3-V LVTTL")),  # HEX3[0:6]
    ("hex", 4, Pins("AA24  Y23  Y24  W22  W24  V23  W25"), IOStandard("3.3-V LVTTL")),  # HEX4[0:6]
    ("hex", 5, Pins("V25  AA28  Y27 AB27 AB26 AA26 AA25"), IOStandard("3.3-V LVTTL")),  # HEX5[0:6]

    ("gpio", 0, Pins("AC18  Y17 AD17  Y18 AK16 AK18 AK19 AJ19 AJ17 AJ16 AH18 AH17 AG16 AE16 AF16 AG17 AA18 AA19 AE17 AC20 AH19 AJ20 AH20 AK21 AD19 AD20 AE18 AE19 AF20 AF21 AF19 AG21 AF18 AG20 AG18 AJ21"), IOStandard("3.3-V LVTTL")),  # JP1 GPIO_0[0:35]
    ("gpio", 1, Pins("AB18 AA21 AB21 AC23 AD24 AE23 AE24 AF25 AF26 AG25 AG26 AH24 AH27 AJ27 AK29 AK28 AK27 AJ26 AK26 AH25 AJ25 AJ24 AK24 AG23 AK23 AH23 AK22 AJ22 AH22 AG22 AF24 AF23 AE22 AD21 AA20 AC22"), IOStandard("3.3-V LVTTL")),  # JP2 GPIO_1[0:35]

    ("aud", 0,
        Subsignal("adclrck", Pins("K8")), # AUD_ADCLRCK
        Subsignal("adcdat",  Pins("K7")), # AUD_ADCDAT
        Subsignal("dacrck",  Pins("H8")), # AUD_DACRCK
        Subsignal("datdac",  Pins("J7")), # AUD_DACDAT
        Subsignal("xck",     Pins("G7")), # AUD_XCK
        Subsignal("bclk",    Pins("H7")), # AUD_BCLK
        IOStandard("3.3-V LVTTL")
    ),

    ("i2c", 0,
        Subsignal("sclk", Pins("J12")), # FPGA_I2C_SCLK
        Subsignal("sdat", Pins("K12")), # FPGA_I2C_SDAT
        IOStandard("3.3-V LVTTL")
    ),

    ("vga", 0,
        Subsignal("r",          Pins("A13 C13 E13 B12 C12 D12 E12 F13")),   # VGA_R[0] ... VGA_R[7]
        Subsignal("g",          Pins(" J9 J10 H12 G10 G11 G12 F11 E11")),   # VGA_G[0] ... VGA_G[7]
        Subsignal("b",          Pins("B13 G13 H13 F14 H14 F15 G15 J14")),   # VGA_B[0] ... VGA_B[7]
        Subsignal("clk",        Pins("A11")),                               # VGA_CLK
        Subsignal("blank_n",    Pins("F10")),                               # VGA_BLANK_N
        Subsignal("hs",         Pins("B11")),                               # VGA_HS
        Subsignal("vs",         Pins("D11")),                               # VGA_VS
        Subsignal("sync_n",     Pins("C10")),                               # VGA_SYNC_N
        IOStandard("3.3-V LVTTL")
    ),

    ("tv", 0,
        Subsignal("data",   Pins("D2 B1 E2 B2 D1 E1 C2 B3")),   # TD_DATA[0] ... TD_DATA[7]
        Subsignal("hs",     Pins("A5")),                        # TD_HS
        Subsignal("vs",     Pins("A3")),                        # TD_VS
        Subsignal("clk27",  Pins("H15")),                       # TD_CLK27
        Subsignal("rst_n",  Pins("F6")),                        # TD_RESET_N
        IOStandard("3.3-V LVTTL")
    ),

    ("ir", 0,
        Subsignal("rx", Pins("AA30")),   # IRDA_RXD
        Subsignal("tx", Pins("AB30")),   # IRDA_TXD
        IOStandard("3.3-V LVTTL")
    ),

    ("ps2", 0,
        Subsignal("clk", Pins("AD7")), # PS2_CLK
        Subsignal("dat", Pins("AE7")), # PS2_DAT
        IOStandard("3.3-V LVTTL")
    ),

    ("ps2", 1,
        Subsignal("clk", Pins("AD9")), # PS2_CLK2
        Subsignal("dat", Pins("AE9")), # PS2_DAT2
        IOStandard("3.3-V LVTTL")
    ),

    ("adc", 0,
        Subsignal("cs_n", Pins("AJ4")), # ADC_CS_N
        Subsignal("dout", Pins("AK3")), # ADC_DOUT
        Subsignal("din",  Pins("AK4")), # ADC_DIN
        Subsignal("sclk", Pins("AK2")), # ADC_SCLK
        IOStandard("3.3-V LVTTL")
    ),

    ("serial", 0,
        Subsignal("tx", Pins("AC18")), # JP1 GPIO[0]
        Subsignal("rx", Pins(" Y17")), # JP1 GPIO[1]
        IOStandard("3.3-V LVTTL")
    ),

    ("epcq", 0,
        Subsignal("dclk", Pins(" U7")),             # EPCQ_DCLK
        Subsignal("data", Pins("AE6 AE5 AE8 AC7")), # EPCQ_AS_DATA[0:3]
        Subsignal("ncso", Pins("AB8")),             # EPCQ_NCSO
        IOStandard("3.3-V LVTTL")
    ),

    ("jtag", 0,
        Subsignal("tck", Pins("AC5")), # JTAG_TCK
        Subsignal("tms", Pins(" V9")), # JTAG_TMS
        Subsignal("tdo", Pins("AB9")), # FPGA_TDO
        Subsignal("tdi", Pins(" U8")), # FPGA_TDI
        IOStandard("3.3-V LVTTL")
    ),

    ("sdram_clock", 0, Pins("AH12"), IOStandard("3.3-V LVTTL")),                                        # DRAM_CLK
    ("sdram", 0,
        Subsignal("a", Pins("AK14 AH14 AG15 AE14 AB15 AC14 AD14 AF15 AH15 AG13 AG12 AH13 AJ14")),       # DRAM_ADDR[0:12]
        Subsignal("ba", Pins("AF13 AJ12")),                                                             # DRAM_BA[0:1]
        Subsignal("cs_n", Pins("AG11")),                                                                # DRAM_CS_N
        Subsignal("cke", Pins("AK13")),                                                                 # DRAM_CKE
        Subsignal("ras_n", Pins("AE13")),                                                               # DRAM_RAS_N
        Subsignal("cas_n", Pins("AF11")),                                                               # DRAM_CAS_M
        Subsignal("we_n", Pins("AA13")),                                                                # DRAM_WE_N
        Subsignal("dq", Pins("AK6 AJ7 AK7 AK8 AK9 AG10 AK11 AJ11 AH10 AJ10 AJ9 AH9 AH8 AH7 AJ6 AJ5")),  # DRAM_DQ[0:15]
        Subsignal("dm", Pins("AB13 AK12")),                                                             # DRAM_LDQM DRAM_UDQM
        IOStandard("3.3-V LVTTL")
    ),


    ("hps_osc", 0, Pins("D25"), IOStandard("3.3-V LVTTL")), # HPS_CLK1 TODO: these are only for reference for the pll not for the AXI interfaces
    ("hps_osc", 1, Pins("F25"), IOStandard("3.3-V LVTTL")), # HPS_CLK2

    ("bootsel", 0, Pins("H20 A18 D20"), IOStandard("3.3-V LVTTL")),  # HPS_BOOTSEL[0:2]

    ("hps_rst", 0,
        Subsignal("nrst",        Pins("C27")),          # KEY7 (HPS_WARM_RST_n)
        Subsignal("npor",        Pins("F23")),          # KEY5 (HPS_RESET_n)
        Subsignal("trst",        Pins("A28")),          # HPS_TRST
        Subsignal("porsel",      Pins("F24")),          # HPS_PORSEL
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_ios", 0,
        Subsignal("conv_usb_n",  Pins("B15")),   # HPS_CONV_USB_N
        Subsignal("enet_int_n",  Pins("C19")),   # HPS_ENET_INT_N       Interrupt Open Drain Output
        Subsignal("ltc_gpio",    Pins("H17")),   # HPS_LTC_GPIO
        Subsignal("i2c_control", Pins("B26")),   # HPS_I2C_CONTROL
        Subsignal("led",         Pins("A24")),   # HPS_LED
        Subsignal("key",         Pins("G21")),   # HPS_KEY
        Subsignal("gsensor_int", Pins("B22")),   # HPS_GSENSOR_INT
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_enet", 0,
        Subsignal("tx_en",   Pins("A20")),              # HPS_ENET_TX_EN GMII and MII transmit enable
        Subsignal("tx_data", Pins("F20 J19 F21 F19")),  # HPS_ENET_TX_DATA[0:3] MII transmit data[3]
        Subsignal("rx_dv",   Pins("K17")),              # HPS_RX_GMII and MII receive data valid
        Subsignal("rx_data", Pins("A21 B20 B18 D21")),  # HPS_ENET_RX_DATA[0:3] GMII and MII receive data[3]
        Subsignal("rx_clk",  Pins("G20")),              # HPS_ENET_RX_CLK      GMII and MII receive clock
        Subsignal("reset_n", Pins("E18")),              # HPS_ENET_RESET_N     Hardware Reset Signal
        Subsignal("mdio",    Pins("E21")),              # HPS_ENET_MDIO        Management Data
        Subsignal("mdc",     Pins("B21")),              # HPS_ENET_MDC         Management Data Clock Reference
        Subsignal("gtx_clk", Pins("H19")),              # HPS_ENET_GTX_CLK     GMII Transmit Clock 3.3V
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_uart", 0,
        Subsignal("rx",         Pins("B25")),   # HPS_UART_RX
        Subsignal("tx",         Pins("C25")),   # HPS_UART_TX
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_ddram", 0,
        Subsignal("a",          Pins("F26 G30 F28 F30 J25 J27 F29 E28 H27 G26 D29 C30 B30 C29 H25"), IOStandard("SSTL-15 Class I")),    # HPS_DDR3_A[0:14]
        Subsignal("ba",         Pins("E29 J24 J23"), IOStandard("SSTL-15 Class I")),                                                    # HPS_DDR3_BA[0:2]
        Subsignal("cas_n",      Pins("E27"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_CAS_n
        Subsignal("cke",        Pins("L29"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_CKE
        Subsignal("ck_n",       Pins("L23"), IOStandard("Differential 1.5V SSTL Class I")),                                             # HPS_DDR3_CK_n
        Subsignal("ck_p",       Pins("M23"), IOStandard("Differential 1.5V SSTL Class I")),                                             # HPS_DDR3_CK_p
        Subsignal("cs_n",       Pins("H24"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_CS_n
        Subsignal("dm",         Pins("K28 M28 R28 W30"), IOStandard("SSTL-15 Class I")),                                                # HPS_DDR3_DM[0:3]
        Subsignal("dq",         Pins("K23 K22 H30 G28 L25 L24 J30 J29 K26 L26 K29 K27 M26 M27 L28 M30 U26 T26 N29 N28 P26 P27 N27 R29 P24 P25 T29 T28 R27 R26 V30 W29"), IOStandard("SSTL-15 Class I")), # HPS_DDR3_DQ[0:31]
        Subsignal("dqs_n",      Pins("M19 N24 R18 R21"), IOStandard("Differential 1.5V SSTL Class I")),                                 # HPS_DDR3_DQS_n
        Subsignal("dqs_p",      Pins("N18 N25 R19 R22"), IOStandard("Differential 1.5V SSTL Class I")),                                 # HPS_DDR3_DQS_p
        Subsignal("odt",        Pins("H28"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_ODT
        Subsignal("ras_n",      Pins("D30"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_RAS_n
        Subsignal("reset_n",    Pins("P30"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_RESET_n
        Subsignal("we_n",       Pins("C28"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_WE_n
        Subsignal("rzq",        Pins("D27"), IOStandard("SSTL-15 Class I")),                                                            # HPS_DDR3_RZQ
    ),

    ("hps_sd", 0,
        Subsignal("clk",  Pins("A16")),             # HPS_SD CLK
        Subsignal("cmd",  Pins("F18")),             # HPS_SD_CMD
        Subsignal("data", Pins("G18 C17 D17 B16")), # HPS_SD_DATA[0:3]
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_usb", 0,
        Subsignal("clkout", Pins("N16")),                               # HPS_USB_CLKOUT
        Subsignal("data",   Pins("E16 G16 D16 D14 A15 C14 D15 M17")),   # HPS_USB_DATA[0:7]
        Subsignal("dir",    Pins("E14")),                               # HPS_USB_DIR
        Subsignal("nxt",    Pins("A14")),                               # HPS_USB_NXT
        Subsignal("reset",  Pins("G17")),                               # HPS_USB_RESET
        Subsignal("stp",    Pins("C15")),                               # HPS_USB_STP
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_spim", 0,
        Subsignal("clk",    Pins("C23")),   # HPS_SPIM_CLK
        Subsignal("miso",   Pins("E24")),   # HPS_SPIM_MISO
        Subsignal("mosi",   Pins("D22")),   # HPS_SPIM_MOSI
        Subsignal("ss",     Pins("D24")),   # HPS_SPIM_SS
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_i2c", 0,
        Subsignal("sclk", Pins("E23")), # HPS_I2C1_SCLK
        Subsignal("sdat", Pins("C24")), # HPS_I2C1_SDAT
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_i2c", 1,
        Subsignal("sclk", Pins("H23")), # HPS_I2C2_SCLK
        Subsignal("sdat", Pins("A25")), # HPS_I2C2_SDAT
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_flash", 0,
        Subsignal("dclk", Pins("D19")),             # HPS_FLASH_DCLK
        Subsignal("data", Pins("C20 H18 A19 E19")), # HPS_FLASH_DATA[0:3]
        Subsignal("ncso", Pins("A18")),             # HPS_FLASH_NCSO
        IOStandard("3.3-V LVTTL")
    ),

    ("hps_jtag", 0,
        Subsignal("tck", Pins("H22")), # HPS_TCK
        Subsignal("tms", Pins("A29")), # HPS_TMS
        Subsignal("tdo", Pins("B28")), # HPS_TDO
        Subsignal("tdi", Pins("B27")), # HPS_TDI
        IOStandard("3.3-V LVTTL")
    ),

]

# Platform -------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name = "clk_50"
    default_clk_period = 1e9/50e6

    def __init__(self):
        super().__init__("5CSEMA5F31C6", _io)
        self.add_ip(os.path.join(os.path.abspath(os.path.dirname(__file__)), f"{self.name}.qsys"))
