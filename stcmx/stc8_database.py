from stcmx.sfr_model import SFRModel
from stcmx.sfrbits_model import SFRBitsModel
from stcmx.selection_model import SelectionModel

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

        self.MX_LANG = SelectionModel(
            'MX_LANG', '0',
            {
                'en': "Select language",
                'cn': "选择语言",
            },
            {
                '0': {'en': 'English', 'cn': 'English'},
                '1': {'en': '中文', 'cn': '中文'},
            },
            {
                '0': 'en',
                '1': 'cn',
            }
        )

        # Basic SFR
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
        self.LIRTRIM = SFRModel('LIRTRIM', 0x9E, 0, 0x00, dict(en='Internal OSC Frequency Adjust, May Be Predefined by ISP', cn='IRC频率微调寄存器, ISP可能写入预设值'))
        self.IRTRIM  = SFRModel('IRTRIM',  0x9F, 0, 0x00, dict(en='Internal OSC Frequency Control, May Be Predefined by ISP', cn='IRC频率调整寄存器, ISP可能写入预设值'))
        self.IE      = SFRModel('IE',      0xA8, 0, 0x00, dict(en='Interrupt Enable/Disable Controller', cn='中断使能寄存器'))
        self.SADDR   = SFRModel('SADDR',   0xA9, 0, 0x00, dict(en='UART1 Slave Address', cn='串口1从机地址寄存器'))
        self.WKTCL   = SFRModel('WKTCL',   0xAA, 0, 0x00, dict(en='Wakup Timer Low Byte', cn='掉电唤醒定时器低字节'))
        self.WKTCH   = SFRModel('WKTCL',   0xAB, 0, 0x00, dict(en='Wakeup Timer High Byte', cn='掉电唤醒定时器高字节'))
        self.S3CON   = SFRModel('S3CON',   0xAC, 0, 0x00, dict(en='UART3 Control', cn='串口3控制寄存器'))
        self.S3BUF   = SFRModel('S3BUF',   0xAD, 0, 0x00, dict(en='UART3 Data', cn='串口3数据寄存器'))
        self.IE2     = SFRModel('IE2',     0xAF, 0, 0x00, dict(en='Interrupt Enable/Disable Controller 2', cn='中断使能寄存器2'))
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
        self.CLKDIV  = SFRModel('CLKDIV',    0xFE01, 1, 0x00, dict(en='System Clock Division Select, May Be Predefined by ISP', cn='时钟分频寄存器,ISP可能写入预设值'))
        self.XOSCCR  = SFRModel('XOSCCR',    0xFE03, 1, 0x00, dict(en='External OSC Control', cn='外部晶振控制寄存器'))
        self.IRC32KCR = SFRModel('IRC32KCR', 0xFE04, 1, 0x00, dict(en='Internal Low Frequency OSC Control', cn='内部32K振荡器控制寄存器'))

        # SFR Bits
        self.MCKSEL = SFRBitsModel(
            self.CKSEL, "MCKSEL", 0,
            {
                'en': "MCU Clock Source",
                'cn': "MCU时钟源",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B11},
            options={
                '0': {'en': 'Internal High Frequency RC OSC', 'cn': '内置高频震荡器'},
                '1': {'en': 'External Clock or Crystal OSC', 'cn': '外部时钟或外置晶振'},
                '2': {'en': 'Internal 32KHz Oscillator', 'cn': '内置32KHz低频晶振'},
            }
        )
        """时钟源选择"""

        self.ENXOSC = SFRBitsModel(
            self.XOSCCR, 'ENXOSC', 7,
            {
                'en': "External OSC Switch",
                'cn': "外部时钟源开关",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '打开'},
            }
        )
        """外部时钟源开关"""

        self.XITYPE = SFRBitsModel(
            self.XOSCCR, 'XITYPE', 6,
            {
                'en': "External OSC Type",
                'cn': "外部时钟源类型",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'External Clock, Need To Use P1.7', 'cn': '外部时钟源或有源晶振,需要占用P1.7'},
                '1': {'en': 'External Crystal OSC, Need P1.6&P1.7', 'cn': '无源晶振, 需要占用P1.6和P1.7'},
            }
        )
        """外部时钟源类型:时钟输入或有源/无源晶振"""

        self.ENIRC32K = SFRBitsModel(
            self.IRC32KCR, 'ENIRC32K', 7,
            {
                'en': "Internal 32K OSC Switch",
                'cn': "内部32K振荡源开关",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '打开'},
            }
        )
        """内部32K低频振荡器开关"""

        self.IRTRIM_S = SFRBitsModel(
            self.IRTRIM, "IRTRIM_S", 0,
            {
                'en': "Internal RC Frequency Trimming, value in range [0, 255], maximum frequency is around "
                      "two times of minimum frequency, hex input (0x??) is supported",
                'cn': "内部时钟振荡器频率调节, 取值范围[0, 255], 频率上限约为下限的2倍. 支持输入十六进制数 0X??",
            },
            len=8,
        )
        """频率微调级别"""

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

        self.TR0 = SFRBitsModel(
            self.TCON, 'TR0', 4,
            {
                'en': "Timer0 Running",
                'cn': "定时器0运行状态",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Stop', 'cn': '停止'},
                '1': {'en': 'Run', 'cn': '运行'},
            },
            sbit=True
        )
        """时钟0是否开启"""

        self.TR1 = SFRBitsModel(
            self.TCON, 'TR1', 6,
            {
                'en': "Timer1 running",
                'cn': "定时器1运行状态",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Stop', 'cn': '停止'},
                '1': {'en': 'Run', 'cn': '运行'},
            },
            sbit=True
        )
        """时钟1是否开启"""

        self.T2R = SFRBitsModel(
            self.AUXR, 'T2R', 4,
            {
                'en': "Timer2 Run/Stop",
                'cn': "定时器2运行状态",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Stop', 'cn': '停止'},
                '1': {'en': 'Run', 'cn': '运行'},
            },
        )
        """时钟2是否开启"""

        self.T0x12 = SFRBitsModel(
            self.AUXR, 'T0x12', 7,
            {
                'en': "Timer0 1T or 12T Mode",
                'cn': "定时器0 1T模式/12T模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': '12T Mode', 'cn': '12T模式'},
                '1': {'en': '1T Mode', 'cn': '1T模式'},
            },
        )
        """定时器0是否使用1T模式"""

        self.T1x12 = SFRBitsModel(
            self.AUXR, 'T1x12', 6,
            {
                'en': "Timer1 1T or 12T Mode",
                'cn': "定时器1 1T模式/12T模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': '12T Mode', 'cn': '12T模式'},
                '1': {'en': '1T Mode', 'cn': '1T模式'},
            },
        )
        """定时器1是否使用1T模式"""

        self.T2x12 = SFRBitsModel(
            self.AUXR, 'T2x12', 2,
            {
                'en': "Timer2 1T or 12T Mode",
                'cn': "定时器2 1T模式/12T模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': '12T Mode', 'cn': '12T模式'},
                '1': {'en': '1T Mode', 'cn': '1T模式'},
            },
        )
        """定时器2是否使用1T模式"""

        self.T0_CT = SFRBitsModel(
            self.TMOD, 'T0_CT', 2,
            {
                'en': "Timer0 function",
                'cn': "定时器0功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Timer', 'cn': '定时'},
                '1': {'en': 'Counter', 'cn': '计数'},
            },
        )
        """定时器0功能选择"""

        self.T1_CT = SFRBitsModel(
            self.TMOD, 'T1_CT', 6,
            {
                'en': "Timer1 function",
                'cn': "定时器1功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Timer', 'cn': '定时'},
                '1': {'en': 'Counter', 'cn': '计数'},
            },
        )
        """定时器1功能选择"""

        self.T2_CT = SFRBitsModel(
            self.AUXR, 'T2_CT', 3,
            {
                'en': "Timer2 function",
                'cn': "定时器2功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Timer', 'cn': '定时'},
                '1': {'en': 'Counter', 'cn': '计数'},
            },
        )
        """定时器2功能选择"""

        self.T0CLKO = SFRBitsModel(
            self.INTCLKO, 'T0CLKO', 0,
            {
                'en': "Timer0 Clock Output",
                'cn': "定时器0时钟输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No output', 'cn': '关闭'},
                '1': {'en': 'Output to P3.5', 'cn': '输出至P3.5'},
            },
        )
        """定时器0时钟输出"""

        self.T1CLKO = SFRBitsModel(
            self.INTCLKO, 'T1CLKO', 1,
            {
                'en': "Timer1 Clock Output",
                'cn': "定时器1时钟输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No output', 'cn': '关闭'},
                '1': {'en': 'Output to P3.4', 'cn': '输出至P3.4'},
            },
        )
        """定时器1时钟输出"""

        self.T2CLKO = SFRBitsModel(
            self.INTCLKO, 'T2CLKO', 2,
            {
                'en': "Timer2 Clock Output",
                'cn': "定时器2时钟输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No output', 'cn': '关闭'},
                '1': {'en': 'Output to P1.3', 'cn': '输出至P1.3'},
            },
        )
        """定时器2时钟输出"""

        self.T0_GATE = SFRBitsModel(
            self.TMOD, 'T0_GATE', 3,
            {
                'en': "Timer0 Work Mode",
                'cn': "定时器0打开条件",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Run Timer0 when RT0 is high', 'cn': 'TR0为高即运行定时器/计数器0'},
                '1': {'en': 'Run Timer0 when INT0 and RT0 are both high', 'cn': '只有在INT0脚为高时, TR0为高才运行定时器/计数器0'},
            },
        )
        """定时器0运行由INT0控制"""

        self.T1_GATE = SFRBitsModel(
            self.TMOD, 'T1_GATE', 7,
            {
                'en': "Timer1 work mode",
                'cn': "定时器1打开条件",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Run Timer1 when RT1 is high', 'cn': 'TR1为高即运行定时器/计数器1'},
                '1': {'en': 'Run Timer1 when INT1 and RT1 are both high', 'cn': '只有在INT1脚为高时, TR1为高才运行定时器/计数器1'},
            },
        )
        """定时器1运行由INT1控制"""

        self.T0_MODE = SFRBitsModel(
            self.TMOD, 'T0_MODE', 0,
            {
                'en': "Timer0 timer mode",
                'cn': "定时器0的定时器模式",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '16bit auto-reload, [TH0,TL0] auto-reloads when overflow',
                      'cn': '16位自动重载模式, 当[TH0,TL0]中的16位计数值溢出时，系统会自动将内部16位重载寄存器中的重载值装入[TH0,TL0]中'},
                '1': {'en': '16bit no-auto-reload, [TH0,TL0] restart from 0 when overflow',
                      'cn': '16位不自动重载模式, 当[TH0,TL0]中的16位计数值溢出时，定时器将从0开始计数'},
                '2': {'en': '8bit auto-reload, TL0 auto-reloads from TH0 when overflow',
                      'cn': '8位自动重载模式, 当TL0中的8位计数值溢出时，系统会自动将TH0中的重载值装入TL0中'},
                '3': {'en': 'Non-interruptable 16bit auto-reload, highest priority',
                      'cn': '不可屏蔽中断的16位自动重载模式, 与模式0相同，不可屏蔽, 中断优先级最高且不可关闭, 可用作操作系统的系统节拍定时器或系统监控定时器'},
            }
        )
        """T0计数模式选择"""

        self.T1_MODE = SFRBitsModel(
            self.TMOD, 'T1_MODE', 4,
            {
                'en': "Timer1 timer mode",
                'cn': "定时器1的定时器模式",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '16bit auto-reload, [TH1,TL1] auto-reloads when overflow',
                      'cn': '16位自动重载模式, 当[TH1,TL1]中的16位计数值溢出时，系统会自动将内部16位重载寄存器中的重载值装入[TH1,TL1]中'},
                '1': {'en': '16bit no-auto-reload, [TH1,TL1] restart from 0 when overflow',
                      'cn': '16位不自动重载模式, 当[TH1,TL1]中的16位计数值溢出时，定时器1将从0开始计数'},
                '2': {'en': '8bit auto-reload, TL1 auto-reloads from TH1 when overflow',
                      'cn': '8位自动重载模式, 当TL1中的8位计数值溢出时，系统会自动将TH1中的重载值装入TL1中'},
                '3': {'en': 'Timer1 stop', 'cn': 'T1停止工作'},
            }
        )
        """T1计数模式选择"""

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

        self.SM2 = SFRBitsModel(
            self.SCON, 'SM2', 5,
            {
                'en': "UART1 Mode2/3 multi-node-communication filter control",
                'cn': "串口1模式2/3多机通信地址帧筛选控制",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No address frame filter', 'cn': '无帧筛选'},
                '1': {'en': 'Enable address frame filter', 'cn': '启用地址帧筛选'},
            }
        )
        """串口1模式2/3多机通信地址帧筛选控制位"""

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
                'en': "UART1(mode1,2,3) double baud rate mode",
                'cn': "串口1模式1/2/3 双倍波特率模式",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '不使用'},
                '1': {'en': 'ON, double baud rate', 'cn': '双倍波特率模式'},
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

        self.EA = SFRBitsModel(
            self.IE, "EA", 7,
            {'en': "Global Interrupt Enable/Disable", 'cn': "总中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """总中断允许控制"""

        self.ELVD = SFRBitsModel(
            self.IE, "ELVD", 6,
            {'en': "Low Voltage Detected Interrupt Enable/Disable", 'cn': "低压检测中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """低压检测中断允许控制"""

        self.EADC = SFRBitsModel(
            self.IE, "EADC", 5,
            {'en': "ADC Interrupt Enable/Disable", 'cn': "ADC转换中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """ADC转换中断允许控制"""

        self.ES = SFRBitsModel(
            self.IE, "ES", 4,
            {'en': "UART1 Interrupt Enable/Disable", 'cn': "串口1中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """串口1中断允许控制"""

        self.ET1 = SFRBitsModel(
            self.IE, "ET1", 3,
            {'en': "Timer1 Interrupt Enable/Disable", 'cn': "定时器1中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """定时器1中断允许控制"""

        self.EX1 = SFRBitsModel(
            self.IE, "EX1", 2,
            {'en': "INT1 Interrupt Enable/Disable", 'cn': "外部中断1中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """外部中断1中断允许控制"""

        self.ET0 = SFRBitsModel(
            self.IE, "ET0", 1,
            {'en': "Timer0 Interrupt Enable/Disable", 'cn': "定时器0中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """定时器0中断允许控制"""

        self.EX0 = SFRBitsModel(
            self.IE, "EX0", 0,
            {'en': "INT0 Interrupt Enable/Disable", 'cn': "外部中断0中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """外部中断0中断允许控制"""

        self.ET4 = SFRBitsModel(
            self.IE2, "ET4", 6,
            {'en': "Timer4 Interrupt Enable/Disable", 'cn': "定时器4中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """定时器4中断允许控制"""

        self.ET3 = SFRBitsModel(
            self.IE2, "ET3", 5,
            {'en': "Timer3 Interrupt Enable/Disable", 'cn': "定时器3中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """定时器3中断允许控制"""

        self.ES4 = SFRBitsModel(
            self.IE2, "ES4", 4,
            {'en': "UART4 Interrupt Enable/Disable", 'cn': "串口4中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """串口4中断允许控制"""

        self.ES3 = SFRBitsModel(
            self.IE2, "ES3", 3,
            {'en': "UART3 Interrupt Enable/Disable", 'cn': "串口3中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """串口3中断允许控制"""

        self.ET2 = SFRBitsModel(
            self.IE2, "ET2", 2,
            {'en': "Timer2 Interrupt Enable/Disable", 'cn': "定时器2中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """定时器2中断允许控制"""

        self.ESPI = SFRBitsModel(
            self.IE2, "ESPI", 1,
            {'en': "SPI Interrupt Enable/Disable", 'cn': "SPI中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """SPI中断允许控制"""

        self.ES2 = SFRBitsModel(
            self.IE2, "ES2", 1,
            {'en': "UART2 Interrupt Enable/Disable", 'cn': "串口2中断允许控制"},
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """串口2中断允许控制"""

    def define_lang(self):
        v = self.MX_LANG.select(self.lang)
        self.lang = v

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
