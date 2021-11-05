from stcmx.stc8_database import Stc8Database
from stcmx.sfrbits_model import SFRBitsModel


class Stc8Config(Stc8Database):
    """STC8 Base Configurations."""

    def __init__(self):
        super().__init__()
        # SFR Bits
        self.LIRTRIM_0 = SFRBitsModel(
            self.LIRTRIM, "LIRTRIM_0", 0,
            {
                'en': "Frequency adjust level",
                'cn': "频率微调级别",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': 'No adjust', 'cn': '无调整'},
                '1': {'en': '+0.01%%', 'cn': '+0.01%%'},
                '2': {'en': '+0.04%%', 'cn': '+0.04%%'},
                '3': {'en': '+0.10%%', 'cn': '+0.10%%'},
            }
        )
        """频率微调级别"""

        self.CLKDIV_0 = SFRBitsModel(
            self.CLKDIV, "CLKDIV_0", 0,
            {
                'en': "Please input the division number, value in range [0, 255], SYSCLK = FOSC / division",
                'cn': "请输入系统时钟 SYSCLK 的分频数字, 取值在[0, 255]区间内, 系统时钟(SYSCLK) = FOSC / 分频数",
            },
            len=8
        )
        """系统时钟分频数, 系统时钟(SYSCLK) = FOSC / 分频数"""

        self.MCKSEL = SFRBitsModel(
            self.CKSEL, "MCKSEL", 0,
            {
                'en': "MCU Clock Source",
                'cn': "MCU时钟源",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': 'Internal High Frequency Oscillator', 'cn': '内置高频震荡器'},
                '1': {'en': 'External Oscillator', 'cn': '外置晶振'},
                '2': {'en': 'External Clock Source', 'cn': '外部时钟源'},
                '3': {'en': 'Internal 32KHz Oscillator', 'cn': '内置32KHz低频晶振'},
            }
        )
        """时钟源选择"""

        self.PCON_PD = SFRBitsModel(
            self.PCON, "PCON_PD", 1,
            {
                'en': "Power-off mode",
                'cn': "时钟停振模式/掉电模式/停电模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No impact', 'cn': '无影响'},
                '1': {
                    'en': 'Stop CPU and all peripherals when entering power-off mode',
                    'cn': '单片机进入时钟停振模式/掉电模式/停电模式，CPU以及全部外设均停止工作, 唤醒后硬件自动清零'
                },
            }
        )
        """时钟停振模式/掉电模式/停电模式时的工作状态"""

        self.PCON_IDEL = SFRBitsModel(
            self.PCON, "PCON_IDEL", 0,
            {'en': "Idle mode", 'cn': "IDLE（空闲）模式"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No impact', 'cn': '无影响'},
                '1': {
                    'en': 'Stop CPU only, all peripherals still working',
                    'cn': '单片机进入 IDLE 模式, 只有 CPU 停止工作, 其他外设依然在运行. 唤醒后硬件自动清零'
                },
            }
        )
        """空闲模式时的工作状态"""

        self.SCON_MODE = SFRBitsModel(
            self.SCON, 'SCON_MODE', 6,
            {
                'en': "UART1 Mode",
                'cn': "串口计数模式",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2':0B10, '3':0B11},
            options={
                '0': {'en': 'Mode 0, synchronous shift serial mode, fixed baud-rate', 'cn': 'Mode 0, 同步移位串行方式'},
                '1': {'en': 'Mode 1, 8-bit UART, baud-rate is configurable', 'cn': 'Mode 1, 可变波特率8位数据方式'},
                '2': {'en': 'Mode 2, 9-bit UART, fixed baud-rate', 'cn': 'Mode 2, 固定波特率9位数据方式'},
                '3': {'en': 'Mode 3, 9-bit UART, baud-rate is configurable', 'cn': 'Mode 3, 可变波特率9位数据方式'},
            }
        )
        """串口1计数方式"""

        self.SCON_REN = SFRBitsModel(
            self.SCON, 'SCON_REN', 4,
            {
                'en': "UART1 RX mode",
                'cn': "开启 UART1 接收(RX mode)",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'RX Off', 'cn': 'RX 关闭'},
                '1': {'en': 'RX ON', 'cn': 'RX 开启'},
            }
        )
        """串口1是否开启RX"""

        self.S1ST2 = SFRBitsModel(
            self.AUXR, 'S1ST2', 0,
            {
                'en': "UART1 Baud Rate Source",
                'cn': "串口1波特率来源",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Timer1', 'cn': '定时器1'},
                '1': {'en': 'Timer2', 'cn': '定时器2'},
            }
        )
        """串口1时钟源, 仅对状态1和3有效"""

        self.UART_M0x6 = SFRBitsModel(
            self.AUXR, 'UART_M0x6', 5,
            {
                'en': "Baud Rate Mode of UART1 mode0",
                'cn': "UART1 模式0的波特率模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No multiple, Fixed Freq = FOSC/12', 'cn': '12分频, 固定频率 = FOSC/12'},
                '1': {'en': 'Multiple by 6, Fixed Freq = FOSC/2', 'cn': '2分频, 固定频率 = FOSC/2'},
            }
        )
        """波特率分频数, 仅对状态0有效"""

        self.SMOD = SFRBitsModel(
            self.PCON, 'SMOD', 7,
            {
                'en': "UART1(mode1,2,3) baud rate double mode",
                'cn': "串口1模式1/2/3 双倍波特率模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No double', 'cn': '不使用'},
                '1': {'en': 'Double baud rate', 'cn': '双倍波特率模式'},
            }
        )
        """双倍波特率模式, 仅对状态1/2/3有效"""

        self.SMOD0 = SFRBitsModel(
            self.PCON, 'SMOD0', 6,
            {
                'en': "UART frame error detect",
                'cn': "串口1帧错误检测",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No error detection', 'cn': '不作错误检测'},
                '1': {'en': 'Enable error detection, then SM0/FE of SCON acts as FE', 'cn': '启用错误检测, 此时 SCON 的SM0/FE作为FE使用'},
            }
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



