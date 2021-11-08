from stcmx.sfr_model import SFRModel
from stcmx.sfrbits_model import SFRBitsModel
from stcmx.selection_model import SelectionModel
from stcmx.value_model import ValueModel
from stcmx.stc8_config import Stc8Config


class Stc8dDatabase(Stc8Config):
    """Database that holds STC8D SFR information."""

    # Special Address in ROM, store chip related info, including UUID, 32KHz wakeup clock, 1.344V ref and Internal RC OSC value
    CPUIDBASE: dict = {
        '0': 0x3FE7,  # STC8A8K16D4
        '1': 0x7FE7,  # STC8A8K32D4
        '2': 0xEFE7,  # STC8A8K60D4
        '3': 0xFDE7,  # STC8A8K64D4
    }

    def __init__(self):
        super().__init__()
        self.name = "STC8A8KxxDx Series"

        # Basic SFR
        self.IRCBAND = SFRModel('IRCBAND', 0x9D, 0, 0x00, dict(en='Internal OSC Band Select', cn='IRC频段选择'))
        """IRC频段选择"""
        self.VRTRIM = SFRModel('VRTRIM', 0xA6, 0, 0x00, dict(en='Internal OSC Band Frequency Adjust', cn='IRC频段频率调节'))
        """IRC频段频率调节"""

        # Extend RAM SFR
        self.HIRCCR = SFRModel('HIRCCR', 0xFE02, 1, 0x80, dict(en='Internal High Speed OSC Control', cn='内部高速振荡器控制寄存器'))
        """内部高速振荡器控制寄存器"""
        self.MCLKOCR = SFRModel('MCLKOCR', 0xFE05, 1, 0x00, dict(en='Clock Output Control', cn='主时钟输出控制寄存器'))
        """主时钟输出控制寄存器"""
        self.IRCDB = SFRModel('IRCDB', 0xFE06, 1, 0x80, dict(en='Internal OSC Calibration Control', cn='内部IRC起振去抖控制'))
        """内部IRC起振去抖控制"""
        self.TM2PS = SFRModel('TM2PS', 0xFEA2, 1, 0x00, dict(en='Timer2 prescale', cn='定时器2时钟预分频寄存器'))
        self.TM3PS = SFRModel('TM3PS', 0xFEA3, 1, 0x00, dict(en='Timer3 prescale', cn='定时器3时钟预分频寄存器'))
        self.TM4PS = SFRModel('TM4PS', 0xFEA4, 1, 0x00, dict(en='Timer4 prescale', cn='定时器4时钟预分频寄存器'))

        # Shadow Configs

        self.MX_FOSC = ValueModel(
            'MX_FOSC',
            24000000,
            {
                'en': "OSC/CLK frequency, value in range [4000000, 55000000]",
                'cn': "振荡源或时钟频率, 值在[4000000, 55000000]区间内",
            },
            valid=lambda a: 4000000 <= a <= 53000000,
        )

        self.MX_CLOCK = SelectionModel(
            'MX_CLOCK',
            '1',
            {
                'en': 'Select frequency',
                'cn': '选择频率',
            },
            {
                '0': {'en': '20MHz', 'cn': '20MHz'},
                '1': {'en': '22.1184MHz', 'cn': '22.1184MHz'},
                '2': {'en': '24MHz', 'cn': '24MHz'},
                '3': {'en': '27MHz', 'cn': '27MHz'},
                '4': {'en': '30MHz', 'cn': '30MHz'},
                '5': {'en': '33.1776MHz', 'cn': '33.1776MHz'},
                '6': {'en': '35MHz', 'cn': '35MHz'},
                '7': {'en': '36.864MHz', 'cn': '36.864MHz'},
                '8': {'en': '40MHz', 'cn': '40MHz'},
                '9': {'en': '45MHz', 'cn': '45MHz'},
            },
            {
                '0': ['T20M_ADDR', 20000000],
                '1': ['T22M_ADDR', 22118400],
                '2': ['T24M_ADDR', 24000000],
                '3': ['T27M_ADDR', 27000000],
                '4': ['T30M_ADDR', 30000000],
                '5': ['T33M_ADDR', 33177600],
                '6': ['T35M_ADDR', 35000000],
                '7': ['T36M_ADDR', 36864000],
                '8': ['T40M_ADDR', 40000000],
                '9': ['T45M_ADDR', 45000000],
            }
        )

        # SFR Bits
        self.ENHIRC = SFRBitsModel(
            self.HIRCCR, 'ENHIRC', 7,
            {
                'en': "Internal High Frequency RC OSC",
                'cn': "内部高频RC振荡器",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '打开'},
            }
        )

        self.ENXOSC = SFRBitsModel(
            self.XOSCCR, 'ENXOSC', 7,
            {
                'en': "External OSC",
                'cn': "外部时钟源",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '打开'},
            }
        )

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

        self.NMXCG = SFRBitsModel(
            self.XOSCCR, 'NMXCG', 3,
            {
                'en': "External Crystal OSC Gain",
                'cn': "外部晶体振荡器增益",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Low', 'cn': '低增益'},
                '1': {'en': 'High', 'cn': '高增益'},
            }
        )

        self.ENIRC32K = SFRBitsModel(
            self.IRC32KCR, 'ENIRC32K', 7,
            {
                'en': "Internal 32K OSC",
                'cn': "内部32K振荡源",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '打开'},
            }
        )
        """内部32K低频振荡器开关"""

        self.IRCBAND_SEL = SFRBitsModel(
            self.IRCBAND, 'IRCBAND_SEL', 0,
            {
                'en': "IRC Frequency Band",
                'cn': "频段选择",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '6MHz', 'cn': '6MHz'},
                '1': {'en': '10MHz', 'cn': '10MHz'},
                '2': {'en': '27MHz', 'cn': '27MHz'},
                '3': {'en': '44MHz', 'cn': '44MHz'},
            }
        )
        """内部时钟振荡器频段选择"""

        self.IRTRIM_S = SFRBitsModel(
            self.IRTRIM, "IRTRIM_S", 0,
            {
                'en': "Internal OSC Frequency Adjust, value in range [0, 255], each step increase by around 0.24%",
                'cn': "内部时钟振荡器频率调整, 取值范围[0, 255], 每级增加大约0.24%",
            },
            len=8,
        )
        """频率微调级别"""

        self.MCLKOCRDIV = SFRBitsModel(
            self.MCLKOCR, 'MCLKOCRDIV', 0,
            {
                'en': "Clock output division, value in range [0, 127], 0 means no output, for other values, output = SYSCLK/division",
                'cn': "时钟输出的分频系数, 取值范围[0, 127], 0表示不输出, 其他值, 则输出频率为SYSCLK/分频系数",
            },
            len=7,
        )
        """时钟输出分频系数, 0:不输出"""

        self.MCLKO_S = SFRBitsModel(
            self.MCLKOCR, 'MCLKO_S', 7,
            {
                'en': "Clock output pin",
                'cn': "时钟输出PIN脚",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'P5.4', 'cn': 'P5.4'},
                '1': {'en': 'P1.6', 'cn': 'P1.6'},
            }
        )
        """时钟输出PIN脚选择"""

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
                'cn': "定时器0 1T模式/12T模式)",
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
                'cn': "定时器1 1T模式/12T模式)",
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
                'cn': "定时器2 1T模式/12T模式)",
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
                'en': "Timer0 Clock Ouput",
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
                'en': "Timer1 Clock Ouput",
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
                'en': "Timer2 Clock Ouput",
                'cn': "定时器2时钟输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'No output', 'cn': '关闭'},
                '1': {'en': 'Output to P1.3', 'cn': '输出至P1.3'},
            },
        )
        """定时器2时钟输出"""

        self.TM2PS_V = SFRBitsModel(
            self.TM2PS, 'TM2PS_V', 0,
            {
                'en': 'Timer2 Prescale',
                'cn': '定时器2 八位预分频系数'
            },
            len=8
        )
        """定时器2 八位预分频系数"""

        self.T0_GATE = SFRBitsModel(
            self.TMOD, 'T0_GATE', 3,
            {
                'en': "Timer0 work mode",
                'cn': "定时器0打开条件",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Normal', 'cn': '正常'},
                '1': {'en': 'Work only when INT0 and RT0 are high', 'cn': '只有在INT0脚为高及TR0控制位置1时才可打开定时器/计数器0'},
            },
        )

        self.T1_GATE = SFRBitsModel(
            self.TMOD, 'T1_GATE', 7,
            {
                'en': "Timer1 work mode",
                'cn': "定时器1打开条件",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Normal', 'cn': '正常'},
                '1': {'en': 'Work only when INT1 and RT1 are high', 'cn': '只有在INT1脚为高及TR1控制位置1时才可打开定时器/计数器1'},
            },
        )

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
