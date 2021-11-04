from stcmx.stc8_database import Stc8Database
from stcmx.sfrbits_model import SFRBitsModel


class Stc8Config(Stc8Database):

    def __init__(self):
        super().__init__()
        # SFR Bits
        self.LIRTRIM_0 = SFRBitsModel(
            self.LIRTRIM, "LIRTRIM_0", 0,
            {
                'en': "Please select adjust level\n  0:No adjust, 1:+0.01%%, 2:+0.04%%, 3:+0.10%%\n[%s]:",
                'cn': "请选择频率微调级别\n  0:无调整, 1:+0.01%%, 2:+0.04%%, 3:+0.10%%\n[%s]:",
            },
            len=2,
            options={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11}
        )

        self.CLKDIV_0 = SFRBitsModel(
            self.CLKDIV, "CLKDIV_0", 0,
            {
                'en': "Please input the division number, value in range [0, 255], SYSCLK = FOSC / division\n[%s]:",
                'cn': "请输入系统时钟 SYSCLK 的分频数字, 取值在[0, 255]区间内, 系统时钟(SYSCLK) = FOSC / 分频数\n[%s]:",
            },
            len=8
        )

        self.MCKSEL = SFRBitsModel(
            self.CKSEL, "MCKSEL", 0,
            {
                'en': "Please select MCU Clock Source:\n" +
                      "  0: Internal High Frequency Oscillator\n" +
                      "  1: External Oscillator\n" +
                      "  2: External Clock Source\n" +
                      "  3: Internal 32KHz Oscillator\n[%s]:",
                'cn': "请选择时钟源\n" +
                      "  0: 内置高频震荡器\n" +
                      "  1: 外置晶振\n" +
                      "  2: 外部时钟源\n" +
                      "  3: 内置32KHz低频晶振\n[%s]:",
            },
            len=2,
            options={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11}
        )

        self.PCON_PD = SFRBitsModel(
            self.PCON, "PCON_PD", 1,
            {
                'en': "Please select the power-off mode:\n  0:No impact, 1:Stop CPU and all peripherals when entering power-off mode\n[%s]:",
                'cn': "请选择时钟停振模式/掉电模式/停电模式\n  0:无影响, 1:单片机进入时钟停振模式/掉电模式/停电模式，CPU以及全部外设均停止工作, 唤醒后硬件自动清零\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.PCON_IDEL = SFRBitsModel(
            self.PCON, "PCON_IDEL", 0,
            {
                'en': "Please select the idle mode:\n  0:No impact, 1:Stop CPU only, all peripherals still working\n[%s]:",
                'cn': "IDLE（空闲）模式:\n  0:无影响, 1:单片机进入 IDLE 模式, 只有 CPU 停止工作, 其他外设依然在运行. 唤醒后硬件自动清零\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.SCON_MODE = SFRBitsModel(
            self.SCON, 'SCON_MODE', 6,
            {
                'en': "Please select UART1 mode:\n" +
                      "  0:Mode 0, synchronous shift serial mode, fixed baud-rate\n" +
                      "  1:Mode 1, 8-bit UART, baud-rate is configurable\n" +
                      "  2:Mode 2, 9-bit UART, fixed baud-rate\n" +
                      "  3:Mode 3, 9-bit UART, baud-rate is configurable\n[%s]:",
                'cn': "请选择串口工作模式:\n" +
                      "  0:Mode 0, 同步移位串行方式\n" +
                      "  1:Mode 1, 可变波特率8位数据方式\n" +
                      "  2:Mode 2, 固定波特率9位数据方式\n" +
                      "  3:Mode 3, 可变波特率9位数据方式\n[%s]:",
            },
            len=2,
            options={'0': 0B00, '1': 0B01, '2':0B10, '3':0B11},
        )

        self.SCON_REN = SFRBitsModel(
            self.SCON, 'SCON_REN', 4,
            {
                'en': "Enable UART1 RX mode?\n  0:RX disabled, 1:RX enabled\n[%s]:",
                'cn': "是否开启 UART1 接收(RX mode):\n  0:RX 关闭, 1:RX 开启\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.S1ST2 = SFRBitsModel(
            self.AUXR, 'S1ST2', 0,
            {
                'en': "Please select UART1 baud generator: 0:Timer1, 1:Timer2\n[%s]:",
                'cn': "请选择串口1波特率来源: 0:定时器1, 1:定时器2\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.UART_M0x6 = SFRBitsModel(
            self.AUXR, 'UART_M0x6', 5,
            {
                'en': "Please select baud rate for UART1 mode0:\n" +
                      "  0:No multiple, Fixed Freq = FOSC/12\n" +
                      "  1:Multiple by 6, Fixed Freq = FOSC/2\n[%s]:",
                'cn': "请选择UART1 模式0的波特率:\n" +
                      "  0:12分频, 固定频率 = FOSC/12\n" +
                      "  1:2分频, 固定频率 = FOSC/2\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.SMOD = SFRBitsModel(
            self.PCON, 'SMOD', 7,
            {
                'en': "Please select UART1(mode1,2,3) baud double mode:\n  0:No double, 1:Double baud rate\n[%s]:",
                'cn': "启用串口1模式1/2/3的双倍波特率模式:\n  0:不使用, 1:双倍波特率模式\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.SMOD0 = SFRBitsModel(
            self.PCON, 'SMOD0', 6,
            {
                'en': "Please select UART frame error detect mode:\n" +
                      "  0:No error detection,\n" +
                      "  1:Enable error detection, then SM0/FE of SCON acts as FE\n[%s]:",
                'cn': "请选择串口1帧错误检测模式:\n" +
                      "  0:不作错误检测, 1:启用错误检测, 此时 SCON 的SM0/FE作为FE使用\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        # __init__ end

    def frequency_adjust(self):
        """Adjust frequency"""
        if self.MCKSEL.get_value() == 0B01 or self.MCKSEL.get_value() == 0B10:
            self.print({
                'en': "External clock source, skip frequency adjust",
                'cn': "外部震荡源/时钟源, 跳过频率调节",
            })
            return
        elif self.MCKSEL.get_value() == 0B11:
            self.print({
                'en': "Internal low frequency OSC, skip frequency adjust",
                'cn': "内部低频晶振, 跳过频率调节",
            })
            return
        value = self.LIRTRIM_0.select(self.lang)
        if value == 0B01:
            self.FOSC = int(self.FOSC * 1.0001)
        elif value == 0B10:
            self.FOSC = int(self.FOSC * 1.0004)
        elif value == 0B11:
            self.FOSC = int(self.FOSC * 1.001)

    def set_sysclock_division(self):
        value = self.CLKDIV_0.select(self.lang)
        self.SYSCLK = self.FOSC if value == 0 else int(self.FOSC / value)

    def uart1_mode_select(self):
        value = self.SCON_MODE.select(self.lang)
        # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
        if value == 0B00 or value == 0B01:
            self.SCON.set_bit(0B0, 5)

    def uart1_mode1_mode3_baud_rate_source_select(self):
        """Select baud rate generator for UART1 mode1 and mode3"""
        if self.SCON_MODE.get_value() == 0B00 or self.SCON_MODE.get_value() == 0B10:
            self.print({
                'en': "UART1 is in Mode0 or Mode2, skip",
                'cn': "串口1为模式0或模式2, 跳过波特率来源设置"
            })
            return

        self.S1ST2.select(self.lang)

    def uart1_mode0_baud_rate_control(self):
        if self.SCON_MODE.get_value() != 0B00:
            self.print({
                'en': "UART1 is not in Mode0, skip",
                'cn': "串口1不是模式0, 跳过波特率设置"
            })
            return
        self.UART_M0x6.select(self.lang)

    def uart1_mode123_double_baud_rate_control(self, val = '0'):
        if self.SCON_MODE.get_value() == 0B00:
            self.print({
                'en': "UART1 is in Mode0, skip",
                'cn': "UART1处于模式0, 跳过双倍模式配置"
            })
            return
        self.SMOD.select(self.lang)

    def uart1_frame_err_detect_control(self):
        self.SMOD0.select(self.lang)
