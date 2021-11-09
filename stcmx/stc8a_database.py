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
        self.ADC_CONTR = SFRModel('ADC_CONTR', 0xBC, 0, 0x00, dict(en='ADC Control', cn='ADC控制寄存器'))
        self.ADC_RES   = SFRModel('ADC_RES',   0xBD, 0, 0x00, dict(en='ADC Result High Bits', cn='ADC结果高位寄存器'))
        self.ADC_RESL  = SFRModel('ADC_RESL',  0xBE, 0, 0x00, dict(en='ADC Result Low Bits', cn='ADC结果低位寄存器'))
        self.ADCCFG    = SFRModel('ADCCFG',    0xDE, 0, 0x00, dict(en='ADC Config', cn='ADC配置寄存器'))

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

        self.ADC_POWER = SFRBitsModel(
            self.ADC_CONTR, "ADC_POWER", 7,
            {
                'en': "ADC Power Control",
                'cn': "ADC电源控制",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """ADC电源控制"""

        self.ADC_START = SFRBitsModel(
            self.ADC_CONTR, "ADC_START", 6,
            {
                'en': "AD Conversion Start Control, This bit will be reset once conversion is finished",
                'cn': "ADC转换启动控制, 转换完成后此位自动清零",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'NO', 'cn': '无'},
                '1': {'en': 'Start', 'cn': '启动'},
            }
        )
        """ADC电源控制"""

        self.ADC_CHS = SFRBitsModel(
            self.ADC_CONTR, 'ADC_CHS', 0,
            {
                'en': "ADC channels selection",
                'cn': "ADC通道选择",
            },
            len=4,
            values={
                '0': 0B0000,
                '1': 0B0001,
                '2': 0B0010,
                '3': 0B0011,
                '4': 0B0100,
                '5': 0B0101,
                '6': 0B0110,
                '7': 0B0111,
                '8': 0B1000,
                '9': 0B1001,
                '10': 0B1010,
                '11': 0B1011,
                '12': 0B1100,
                '13': 0B1101,
                '14': 0B1110,
                '15': 0B1111,

            },
            options={
                '0': {'en': 'P1.0 ADC0', 'cn': 'P1.0 ADC0'},
                '1': {'en': 'P1.1 ADC1', 'cn': 'P1.1 ADC1'},
                '2': {'en': 'P1.2 ADC2', 'cn': 'P1.2 ADC2'},
                '3': {'en': 'P1.3 ADC3', 'cn': 'P1.3 ADC3'},
                '4': {'en': 'P1.4 ADC4', 'cn': 'P1.4 ADC4'},
                '5': {'en': 'P1.5 ADC5', 'cn': 'P1.5 ADC5'},
                '6': {'en': 'P1.6 ADC6', 'cn': 'P1.6 ADC6'},
                '7': {'en': 'P1.7 ADC7', 'cn': 'P1.7 ADC7'},
                '8': {'en': 'P0.0 ADC8', 'cn': 'P0.0 ADC8'},
                '9': {'en': 'P0.1 ADC9', 'cn': 'P0.1 ADC9'},
                '10': {'en': 'P0.2 ADC10', 'cn': 'P0.2 ADC10'},
                '11': {'en': 'P0.3 ADC11', 'cn': 'P0.3 ADC11'},
                '12': {'en': 'P0.4 ADC12', 'cn': 'P0.4 ADC12'},
                '13': {'en': 'P0.5 ADC13', 'cn': 'P0.5 ADC13'},
                '14': {'en': 'P0.6 ADC14', 'cn': 'P0.6 ADC14'},
                '15': {'en': 'REFV ADC', 'cn': 'REFV ADC'},
            }
        )
        """ADC通道选择"""

        self.ADC_RESFMT = SFRBitsModel(
            self.ADCCFG, "ADC_RESFMT", 5,
            {
                'en': "ADC Data Alignment",
                'cn': "ADC结果对齐",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Left Alignment', 'cn': '左对齐'},
                '1': {'en': 'Right Alignment', 'cn': '右对齐'},
            }
        )
        """ADC结果对齐方式"""

        self.ADC_SPEED = SFRBitsModel(
            self.ADCCFG, "ADC_SPEED", 0,
            {
                'en': "ADC Clock Prescaler",
                'cn': "ADC时钟预分频",
            },
            values={
                '0': 0B0000,
                '1': 0B0001,
                '2': 0B0010,
                '3': 0B0011,
                '4': 0B0100,
                '5': 0B0101,
                '6': 0B0110,
                '7': 0B0111,
                '8': 0B1000,
                '9': 0B1001,
                '10': 0B1010,
                '11': 0B1011,
                '12': 0B1100,
                '13': 0B1101,
                '14': 0B1110,
                '15': 0B1111,

            },
            options={
                '0': {'en': 'SYSCLK/32', 'cn': 'SYSCLK/32'},
                '1': {'en': 'SYSCLK/64', 'cn': 'SYSCLK/64'},
                '2': {'en': 'SYSCLK/96', 'cn': 'SYSCLK/96'},
                '3': {'en': 'SYSCLK/128', 'cn': 'SYSCLK/128'},
                '4': {'en': 'SYSCLK/160', 'cn': 'SYSCLK/160'},
                '5': {'en': 'SYSCLK/192', 'cn': 'SYSCLK/192'},
                '6': {'en': 'SYSCLK/224', 'cn': 'SYSCLK/224'},
                '7': {'en': 'SYSCLK/256', 'cn': 'SYSCLK/256'},
                '8': {'en': 'SYSCLK/288', 'cn': 'SYSCLK/288'},
                '9': {'en': 'SYSCLK/320', 'cn': 'SYSCLK/320'},
                '10': {'en': 'SYSCLK/352', 'cn': 'SYSCLK/352'},
                '11': {'en': 'SYSCLK/384', 'cn': 'SYSCLK/384'},
                '12': {'en': 'SYSCLK/416', 'cn': 'SYSCLK/416'},
                '13': {'en': 'SYSCLK/448', 'cn': 'SYSCLK/448'},
                '14': {'en': 'SYSCLK/480', 'cn': 'SYSCLK/480'},
                '15': {'en': 'SYSCLK/512', 'cn': 'SYSCLK/512'},
            }
        )
        """ADC时钟预分频"""

        # __init__ end
