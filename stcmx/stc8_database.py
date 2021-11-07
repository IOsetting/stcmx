from stcmx.sfr_model import SFRModel
from stcmx.sfrbits_model import SFRBitsModel

class Stc8Database(object):
    """Database that holds SFR information."""

    def __init__(self):
        self.name:str = 'STC8 Generic'
        self.lang:str = 'en'
        self.verbose:bool = True
        # The frequency of internal or external oscillator, or external clock source
        self.FOSC:int = 11059200
        # System clock
        self.SYSCLK:int = 11059200

        # Basic SFR
        self.LIRTRIM = SFRModel('LIRTRIM', 0x9E, 0, 0x00, dict(en='Internal OSC Frequency Adjust', cn='IRC频率微调寄存器'))
        self.S4CON   = SFRModel('S4CON',   0x84, 0, 0x00, dict(en='UART4 Control', cn='串口4控制寄存器'))
        self.S4BUF   = SFRModel('S4BUF',   0x85, 0, 0x00, dict(en='UART4 Data', cn='串口4数据寄存器'))
        self.PCON    = SFRModel('PCON',    0x87, 0, 0x30, dict(en='Power Control', cn='电源控制寄存器'))
        self.TCON    = SFRModel('TCON',    0x88, 0, 0x00, dict(en='Timer Control', cn='定时器控制寄存器'))
        self.TMOD    = SFRModel('TMOD',    0x89, 0, 0x00, dict(en='Timer Mode', cn='定时器模式寄存器'))
        self.TL0     = SFRModel('TL0',     0x8A, 0, 0x00, dict(en='Timer0 Low 8bit', cn='定时器0低8位寄存器'))
        self.TL1     = SFRModel('TL1',     0x8B, 0, 0x00, dict(en='Timer1 Low 8bit', cn='定时器1低8位寄存器'))
        self.TH0     = SFRModel('TH0',     0x8C, 0, 0x00, dict(en='Timer0 High 8bit', cn='定时器0高8位寄存器'))
        self.TH1     = SFRModel('TH1',     0x8D, 0, 0x00, dict(en='Timer1 High 8bit', cn='定时器1高8位寄存器'))
        self.AUXR    = SFRModel('AUXR',    0x8E, 0, 0x01, dict(en='Auxr Control', cn='辅助寄存器'))
        self.INTCLKO = SFRModel('INTCLKO', 0x8F, 0, 0x00, dict(en='Timer output and Interrupt Control', cn='中断与时钟输出控制寄存器'))
        self.SCON    = SFRModel('SCON',    0x98, 0, 0x00, dict(en='UART1 Control', cn='串口1控制寄存器'))
        self.SBUF    = SFRModel('SBUF',    0x99, 0, 0x00, dict(en='UART1 Data', cn='串口1数据寄存器'))
        self.S2CON   = SFRModel('S2CON',   0x9A, 0, 0x40, dict(en='UART2 Control', cn='串口2控制寄存器'))
        self.S2BUF   = SFRModel('S2BUF',   0x9B, 0, 0x00, dict(en='UART2 Data', cn='串口2数据寄存器'))
        self.IRTRIM  = SFRModel('IRTRIM',  0x9F, 0, 0x00, dict(en='Internal OSC Frequency Control', cn='IRC频率调整寄存器'))
        self.S3CON   = SFRModel('S3CON',   0xAC, 0, 0x00, dict(en='UART3 Control', cn='串口3控制寄存器'))
        self.S3BUF   = SFRModel('S3BUF',   0xAD, 0, 0x00, dict(en='UART3 Data', cn='串口3数据寄存器'))
        self.SADDR   = SFRModel('SADDR',   0xA9, 0, 0x00, dict(en='UART1 Slave Address', cn='串口1从机地址寄存器'))
        self.WKTCL   = SFRModel('WKTCL',   0xAA, 0, 0x00, dict(en='Wakup Timer Low Byte', cn='掉电唤醒定时器低字节'))
        self.WKTCH   = SFRModel('WKTCL',   0xAB, 0, 0x00, dict(en='Wakeup Timer High Byte', cn='掉电唤醒定时器高字节'))
        self.SADEN   = SFRModel('SADEN',   0xB9, 0, 0x00, dict(en='UART1 Slave Deny Address', cn='串口1从机地址屏蔽寄存'))
        self.P_SW2   = SFRModel('P_SW2',   0xBA, 0, 0x00, dict(en='Peripheral Port Switch', cn='外设端口切换寄存器2'))
        self.PSW     = SFRModel('PSW',     0xD0, 0, 0x00, dict(en='Program Status', cn='程序状态字寄存器'))
        self.T4T3M   = SFRModel('T4T3M',   0xD1, 0, 0x00, dict(en='Timer4/3 Control', cn='定时器4/3控制寄存器'))
        self.T4H     = SFRModel('T4H',     0xD2, 0, 0x00, dict(en='Timer4 High Byte', cn='定时器4高字节'))
        self.T4L     = SFRModel('T4L',     0xD3, 0, 0x00, dict(en='Timer4 Low Byte', cn='定时器4低字节'))
        self.T3H     = SFRModel('T3H',     0xD4, 0, 0x00, dict(en='Timer3 High Byte', cn='定时器3高字节'))
        self.T3L     = SFRModel('T3L',     0xD5, 0, 0x00, dict(en='Timer4 Low Byte', cn='定时器3低字节'))
        self.T2H     = SFRModel('T2H',     0xD6, 0, 0x00, dict(en='Timer3 High Byte', cn='定时器2高字节'))
        self.T2L     = SFRModel('T2L',     0xD7, 0, 0x00, dict(en='Timer4 Low Byte', cn='定时器2低字节'))
        self.P1M1    = SFRModel('P1M1',    0x91, 0, 0x00, dict(en='P1 Port Config 1', cn='P1口配置寄存器1'))
        self.P1M0    = SFRModel('P1M0',    0x92, 0, 0x00, dict(en='P1 Port Config 0', cn='P1口配置寄存器0'))
        self.P0M1    = SFRModel('P0M1',    0x93, 0, 0x00, dict(en='P0 Port Config 1', cn='P0口配置寄存器1'))
        self.P0M0    = SFRModel('P0M0',    0x94, 0, 0x00, dict(en='P0 Port Config 0', cn='P0口配置寄存器0'))
        self.P2M1    = SFRModel('P2M1',    0x95, 0, 0x00, dict(en='P2 Port Config 1', cn='P2口配置寄存器1'))
        self.P2M0    = SFRModel('P2M0',    0x96, 0, 0x00, dict(en='P2 Port Config 0', cn='P2口配置寄存器0'))
        self.P3M1    = SFRModel('P3M1',    0xB1, 0, 0x00, dict(en='P3 Port Config 1', cn='P3口配置寄存器1'))
        self.P3M0    = SFRModel('P3M0',    0xB2, 0, 0x00, dict(en='P3 Port Config 0', cn='P3口配置寄存器0'))
        self.P4M1    = SFRModel('P4M1',    0xB3, 0, 0x00, dict(en='P4 Port Config 1', cn='P4口配置寄存器1'))
        self.P4M0    = SFRModel('P4M0',    0xB4, 0, 0x00, dict(en='P4 Port Config 0', cn='P4口配置寄存器0'))
        self.P5M1    = SFRModel('P5M1',    0xC9, 0, 0x00, dict(en='P5 Port Config 1', cn='P5口配置寄存器1'))
        self.P5M0    = SFRModel('P5M0',    0xCA, 0, 0x00, dict(en='P5 Port Config 0', cn='P5口配置寄存器0'))
        self.P6M1    = SFRModel('P6M1',    0xCB, 0, 0x00, dict(en='P6 Port Config 1', cn='P6口配置寄存器1'))
        self.P6M0    = SFRModel('P6M0',    0xCC, 0, 0x00, dict(en='P6 Port Config 0', cn='P6口配置寄存器0'))
        self.P7M1    = SFRModel('P7M1',    0xE1, 0, 0x00, dict(en='P7 Port Config 1', cn='P7口配置寄存器1'))
        self.P7M0    = SFRModel('P7M0',    0xE2, 0, 0x00, dict(en='P7 Port Config 0', cn='P7口配置寄存器0'))

        # Extend RAM SFR
        self.CKSEL   = SFRModel('CKSEL',     0xFE00, 1, 0x00, dict(en='Clock Source Select', cn='时钟选择寄存器'))
        self.CLKDIV  = SFRModel('CLKDIV',    0xFE01, 1, 0x00, dict(en='System Clock Division Select', cn='时钟分频寄存器'))
        self.XOSCCR  = SFRModel('XOSCCR',    0xFE03, 1, 0x00, dict(en='External OSC Control', cn='外部晶振控制寄存器'))
        self.IRC32KCR = SFRModel('IRC32KCR', 0xFE04, 1, 0x00, dict(en='Internal Low Frequency OSC Control', cn='内部32K振荡器控制寄存器'))

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
                '1': {'en': '+0.01%', 'cn': '+0.01%'},
                '2': {'en': '+0.04%', 'cn': '+0.04%'},
                '3': {'en': '+0.10%', 'cn': '+0.10%'},
            }
        )
        """频率微调级别"""

        self.CLKDIV_0 = SFRBitsModel(
            self.CLKDIV, "CLKDIV_0", 0,
            {
                'en': "SYSCLK division number, value in range [0, 255], SYSCLK = FOSC / division",
                'cn': "系统时钟 SYSCLK 的分频系数, 取值在[0, 255]区间内, 系统时钟(SYSCLK) = FOSC / 分频系数",
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
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
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
                '1': {'en': 'Enable error detection, then SM0/FE of SCON acts as FE',
                      'cn': '启用错误检测, 此时 SCON 的SM0/FE作为FE使用'},
            }
        )




    def define_lang(self):
        languages = {'0': 'en', '1': 'cn'}
        while True:
            arg = self.input({
                'en': "Please select lanuage, Currently [%r]\n0: English, 1: 中文\n:"%self.lang,
                'cn': "请选择语言, 当前设置[%r]:\n0: English, 1: 中文\n:"%self.lang,
            })
            if len(arg) > 0:
                if arg in languages.keys():
                    self.lang = languages[arg]
                    break

    def define_verbose(self):
        while True:
            arg = self.input({
                'en': "Enable debug output? Currently [%r]\n0: No, 1: Yes\n:"%self.verbose,
                'cn': "开启Debug输出? 当前设置[%r]\n0: 否, 1: 是\n:"%self.verbose,
            })
            if len(arg) > 0:
                self.verbose = False if arg == '0' else True
                break

    def print(self, content:dict):
        print(content[self.lang])

    def input(self, content:dict):
        return input(content[self.lang])
