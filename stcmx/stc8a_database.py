from stcmx.sfr_model import SFRModel
from stcmx.sfrbits_model import SFRBitsModel
from stcmx.selection_model import SelectionModel
from stcmx.value_model import ValueModel
from stcmx.stc8_config import Stc8Config
import stcmx.util as util


class Stc8aDatabase(Stc8Config):
    """Database that holds STC8 SFR information."""

    OPTIONS:dict = {
        'cpuid': '0',
    }

    def __init__(self):
        super().__init__()
        self.name = "STC8A,STC8C,STC8F Series"

        # Basic SFR

        # Extend RAM SFR
        self.IRC24MCR = SFRModel('IRC24MCR', 0xFE02, 1, 0x80, dict(en='Internal High Speed OSC Control', cn='内部24M振荡器控制寄存器'))
        self.ADCTIM = SFRModel('ADCTIM', 0xFEA8, 1, 0x80, dict(en='ADC Time Sequence Control', cn='ADC时序控制寄存器'))

        # Shadow Configs

        self.MX_FOSC = ValueModel(
            'MX_FOSC',
            24000000,
            {
                'en': "OSC/CLK frequency, value in range [16000000, 28000000]",
                'cn': "振荡源或时钟频率, 值在[16000000, 28000000]区间内",
            },
            valid=lambda a: 16000000 <= a <= 28000000,
        )

        self.MX_CLOCK = SelectionModel(
            'MX_CLOCK',
            '1',
            {
                'en': 'Select frequency',
                'cn': '选择频率',
            },
            {
                '0': {'en': '22.1184MHz', 'cn': '22.1184MHz'},
                '1': {'en': '24MHz', 'cn': '24MHz'},
            },
            {
                '0': ['T22M1184', 22118400],
                '1': ['T24M', 24000000],
            }
        )

        # SFR Bits
        self.ENIRC24M = SFRBitsModel(
            self.IRC24MCR, 'ENIRC24M', 7,
            {
                'en': "Internal 24MHz RC OSC Switch",
                'cn': "内部24MHz振荡器开关",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """内部高速24MHz RC振荡器开关"""

        self.MCLKODIV = SFRBitsModel(
            self.CKSEL, "MCLKODIV", 4,
            {
                'en': "SYSCLK output division",
                'cn': "系统时钟输出分频系数",
            },
            len=4,
            values={'0': 0B0000, '1': 0B0001, '2': 0B0010, '3': 0B0100, '4': 0B0110, '5': 0B1000, '6': 0B1010, '7': 0B1100, '8': 0B1110},
            options={
                '0': {'en': 'No output', 'cn': '不输出'},
                '1': {'en': 'SYSCLK/1', 'cn': 'SYSCLK/1'},
                '2': {'en': 'SYSCLK/2', 'cn': 'SYSCLK/2'},
                '3': {'en': 'SYSCLK/4', 'cn': 'SYSCLK/4'},
                '4': {'en': 'SYSCLK/8', 'cn': 'SYSCLK/8'},
                '5': {'en': 'SYSCLK/16', 'cn': 'SYSCLK/16'},
                '6': {'en': 'SYSCLK/32', 'cn': 'SYSCLK/32'},
                '7': {'en': 'SYSCLK/64', 'cn': 'SYSCLK/64'},
                '8': {'en': 'SYSCLK/128', 'cn': 'SYSCLK/128'},
            }
        )
        """系统时钟输出分频系数"""

        self.MCLKO_S = SFRBitsModel(
            self.CKSEL, "MCLKO_S", 3,
            {
                'en': "SYSCLK output pin select",
                'cn': "系统时钟输出管脚选择",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'P5.4', 'cn': 'P5.4'},
                '1': {'en': 'P1.6', 'cn': 'P1.6'},
            }
        )
        """系统时钟输出管脚选择"""

        # __init__ end
