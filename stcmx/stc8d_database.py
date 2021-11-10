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
            valid=lambda a: 4000000 <= a <= 55000000,
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

        self.MCLKOCRDIV = SFRBitsModel(
            self.MCLKOCR, 'MCLKOCRDIV', 0,
            {
                'en': "Clock output division, value range [0, 127], 0:no output, other values:SYSCLK/division",
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

        self.TM2PS_V = SFRBitsModel(
            self.TM2PS, 'TM2PS_V', 0,
            {
                'en': 'Timer2 Prescale',
                'cn': '定时器2 八位预分频系数'
            },
            len=8
        )
        """定时器2 八位预分频系数"""
