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

        self.CCON      = SFRModel('CCON',      0xD8, 0, 0x00, dict(en='PCA Control', cn='PCA控制寄存器'))
        self.CMOD      = SFRModel('CMOD',      0xD9, 0, 0x00, dict(en='PCA Mode', cn='PCA模式寄存器'))
        self.CCAPM0    = SFRModel('CCAPM0',    0xDA, 0, 0x00, dict(en='PCA Module0 Mode Control', cn='PCA模块0模式控制寄存器'))
        self.CCAPM1    = SFRModel('CCAPM1',    0xDB, 0, 0x00, dict(en='PCA Module1 Mode Control', cn='PCA模块1模式控制寄存器'))
        self.CCAPM2    = SFRModel('CCAPM2',    0xDC, 0, 0x00, dict(en='PCA Module2 Mode Control', cn='PCA模块2模式控制寄存器'))
        self.CCAPM3    = SFRModel('CCAPM3',    0xDD, 0, 0x00, dict(en='PCA Module3 Mode Control', cn='PCA模块3模式控制寄存器'))
        self.CL        = SFRModel('CL',        0xE9, 0, 0x00, dict(en='PCA Counter Low Byte', cn='PCA计数器低字节'))
        self.CH        = SFRModel('CH',        0xF9, 0, 0x00, dict(en='PCA Counter High Byte', cn='PCA计数器高字节'))
        self.CCAP0L    = SFRModel('CCAP0L',    0xEA, 0, 0x00, dict(en='PCA Module0 Low Byte', cn='PCA模块0低字节'))
        self.CCAP1L    = SFRModel('CCAP1L',    0xEB, 0, 0x00, dict(en='PCA Module1 Low Byte', cn='PCA模块1低字节'))
        self.CCAP2L    = SFRModel('CCAP2L',    0xEC, 0, 0x00, dict(en='PCA Module2 Low Byte', cn='PCA模块2低字节'))
        self.CCAP3L    = SFRModel('CCAP3L',    0xED, 0, 0x00, dict(en='PCA Module3 Low Byte', cn='PCA模块3低字节'))
        self.PCA_PWM0  = SFRModel('PCA_PWM0',  0xF2, 0, 0x00, dict(en='PCA Module0 PWM Mode Control', cn='PCA模块0 PWM模式寄存器'))
        self.PCA_PWM1  = SFRModel('PCA_PWM1',  0xF3, 0, 0x00, dict(en='PCA Module1 PWM Mode Control', cn='PCA模块1 PWM模式寄存器'))
        self.PCA_PWM2  = SFRModel('PCA_PWM2',  0xF4, 0, 0x00, dict(en='PCA Module2 PWM Mode Control', cn='PCA模块2 PWM模式寄存器'))
        self.PCA_PWM3  = SFRModel('PCA_PWM3',  0xF5, 0, 0x00, dict(en='PCA Module3 PWM Mode Control', cn='PCA模块3 PWM模式寄存器'))
        self.CCAP0H    = SFRModel('CCAP0H',    0xFA, 0, 0x00, dict(en='PCA Module0 High Byte', cn='PCA模块0高字节'))
        self.CCAP1H    = SFRModel('CCAP1H',    0xFB, 0, 0x00, dict(en='PCA Module1 High Byte', cn='PCA模块1高字节'))
        self.CCAP2H    = SFRModel('CCAP2H',    0xFC, 0, 0x00, dict(en='PCA Module2 High Byte', cn='PCA模块2高字节'))
        self.CCAP3H    = SFRModel('CCAP3H',    0xFD, 0, 0x00, dict(en='PCA Module3 High Byte', cn='PCA模块3高字节'))


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

        self.CR = SFRBitsModel(
            self.CCON, "CR", 6,
            {
                'en': "PCA Run Control",
                'cn': "PCA运行控制",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Stop', 'cn': '停止'},
                '1': {'en': 'Run', 'cn': '运行'},
            }
        )
        """PCA运行控制"""

        self.CIDL = SFRBitsModel(
            self.CMOD, "CIDL", 7,
            {
                'en': "PCA Stop Counting When Idel",
                'cn': "PCA 空闲时停止计数",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Count', 'cn': '计数'},
                '1': {'en': 'Stop Counting', 'cn': '停止计数'},
            }
        )
        """PCA运行控制"""

        self.CPS = SFRBitsModel(
            self.CMOD, "CPS", 1,
            {
                'en': "PCA Clock Source",
                'cn': "PCA计数时钟源/脉冲源",
            },
            len=3,
            values={
                '0': 0B000, '1': 0B001, '2': 0B010, '3': 0B011,
                '4': 0B100, '5': 0B101, '6': 0B110, '7': 0B111
            },
            options={
                '0': {'en': 'SYSCLK/12', 'cn': 'SYSCLK/12'},
                '1': {'en': 'SYSCLK/2', 'cn': 'SYSCLK/2'},
                '2': {'en': 'Timer0 Overflow', 'cn': '定时器1溢出脉冲'},
                '3': {'en': 'ECI Pin External Clock', 'cn': 'ECI脚外部时钟'},
                '4': {'en': 'SYSCLK', 'cn': 'SYSCLK'},
                '5': {'en': 'SYSCLK/4', 'cn': 'SYSCLK/4'},
                '6': {'en': 'SYSCLK/6', 'cn': 'SYSCLK/6'},
                '7': {'en': 'SYSCLK/8', 'cn': 'SYSCLK/8'},
            }
        )
        """PCA计数时钟源选择"""

        self.ECF = SFRBitsModel(
            self.CMOD, "ECF", 0,
            {
                'en': "PCA Counter Overflow Interrupt",
                'cn': "PCA计数溢出中断",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """PCA计数溢出中断"""

        self.ECOM0 = SFRBitsModel(
            self.CCAPM0, "ECOM0", 6,
            {
                'en': "PCA Module0 Comparison",
                'cn': "PCA模块0比较功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块0比较功能"""

        self.ECOM1 = SFRBitsModel(
            self.CCAPM1, "ECOM1", 6,
            {
                'en': "PCA Module1 Comparison",
                'cn': "PCA模块1比较功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块1比较功能"""

        self.ECOM2 = SFRBitsModel(
            self.CCAPM2, "ECOM2", 6,
            {
                'en': "PCA Module2 Comparison",
                'cn': "PCA模块2比较功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块2比较功能"""

        self.ECOM3 = SFRBitsModel(
            self.CCAPM3, "ECOM3", 6,
            {
                'en': "PCA Module3 Comparison",
                'cn': "PCA模块3比较功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块3比较功能"""

        self.CCAPP0 = SFRBitsModel(
            self.CCAPM0, "CCAPP0", 5,
            {
                'en': "PCA Module0 Rising Capture",
                'cn': "PCA模块0上升沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块0上升沿捕获"""

        self.CCAPP1 = SFRBitsModel(
            self.CCAPM1, "CCAPP1", 5,
            {
                'en': "PCA Module1 Rising Capture",
                'cn': "PCA模块1上升沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块1上升沿捕获"""

        self.CCAPP2 = SFRBitsModel(
            self.CCAPM2, "CCAPP2", 5,
            {
                'en': "PCA Module2 Rising Capture",
                'cn': "PCA模块2上升沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块2上升沿捕获"""

        self.CCAPP3 = SFRBitsModel(
            self.CCAPM3, "CCAPP3", 5,
            {
                'en': "PCA Module3 Rising Capture",
                'cn': "PCA模块3上升沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块3上升沿捕获"""

        self.CCAPN0 = SFRBitsModel(
            self.CCAPM0, "CCAPN0", 4,
            {
                'en': "PCA Module0 Falling Capture",
                'cn': "PCA模块0下降沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块0下降沿捕获"""

        self.CCAPN1 = SFRBitsModel(
            self.CCAPM1, "CCAPN1", 4,
            {
                'en': "PCA Module1 Falling Capture",
                'cn': "PCA模块1下降沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块1下降沿捕获"""

        self.CCAPN2 = SFRBitsModel(
            self.CCAPM2, "CCAPN2", 4,
            {
                'en': "PCA Module2 Falling Capture",
                'cn': "PCA模块2下降沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块2下降沿捕获"""

        self.CCAPN3 = SFRBitsModel(
            self.CCAPM3, "CCAPN3", 4,
            {
                'en': "PCA Module3 Falling Capture",
                'cn': "PCA模块3下降沿捕获",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块3下降沿捕获"""

        self.MAT0 = SFRBitsModel(
            self.CCAPM0, "MAT0", 3,
            {
                'en': "PCA Module0 Match",
                'cn': "PCA模块0匹配功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块0匹配功能"""

        self.MAT1 = SFRBitsModel(
            self.CCAPM1, "MAT1", 3,
            {
                'en': "PCA Module1 Match",
                'cn': "PCA模块1匹配功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块1匹配功能"""

        self.MAT2 = SFRBitsModel(
            self.CCAPM2, "MAT2", 3,
            {
                'en': "PCA Module2 Match",
                'cn': "PCA模块2匹配功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块2匹配功能"""

        self.MAT3 = SFRBitsModel(
            self.CCAPM3, "MAT3", 3,
            {
                'en': "PCA Module3 Match",
                'cn': "PCA模块3匹配功能",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块3匹配功能"""

        self.TOG0 = SFRBitsModel(
            self.CCAPM0, "TOG0", 2,
            {
                'en': "PCA Module0 Pulse Output",
                'cn': "PCA模块0脉冲输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块0脉冲输出"""

        self.TOG1 = SFRBitsModel(
            self.CCAPM1, "TOG1", 2,
            {
                'en': "PCA Module1 Pulse Output",
                'cn': "PCA模块1脉冲输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块1脉冲输出"""

        self.TOG2 = SFRBitsModel(
            self.CCAPM2, "TOG2", 2,
            {
                'en': "PCA Module2 Pulse Output",
                'cn': "PCA模块2脉冲输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块2脉冲输出"""

        self.TOG3 = SFRBitsModel(
            self.CCAPM3, "TOG3", 2,
            {
                'en': "PCA Module3 Pulse Output",
                'cn': "PCA模块3脉冲输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块3脉冲输出"""

        self.PWM0 = SFRBitsModel(
            self.CCAPM0, "PWM0", 1,
            {
                'en': "PCA Module0 PWM Output",
                'cn': "PCA模块0 PWM输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块0 PWM输出"""

        self.PWM1 = SFRBitsModel(
            self.CCAPM1, "PWM1", 1,
            {
                'en': "PCA Module1 PWM Output",
                'cn': "PCA模块1 PWM输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块1 PWM输出"""

        self.PWM2 = SFRBitsModel(
            self.CCAPM2, "PWM2", 1,
            {
                'en': "PCA Module2 PWM Output",
                'cn': "PCA模块2 PWM输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块2 PWM输出"""

        self.PWM3 = SFRBitsModel(
            self.CCAPM3, "PWM3", 1,
            {
                'en': "PCA Module3 PWM Output",
                'cn': "PCA模块3 PWM输出",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'OFF', 'cn': '关闭'},
                '1': {'en': 'ON', 'cn': '开启'},
            }
        )
        """PCA模块3 PWM输出"""

        self.ECCF0 = SFRBitsModel(
            self.CCAPM0, "ECCF0", 0,
            {
                'en': "PCA Module0 Match/Capture Interrupt",
                'cn': "PCA模块0 匹配捕获中断",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """PCA模块0 匹配捕获中断"""

        self.ECCF1 = SFRBitsModel(
            self.CCAPM1, "ECCF1", 0,
            {
                'en': "PCA Module1 Match/Capture Interrupt",
                'cn': "PCA模块1 匹配捕获中断",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """PCA模块1 匹配捕获中断"""

        self.ECCF2 = SFRBitsModel(
            self.CCAPM2, "ECCF2", 0,
            {
                'en': "PCA Module2 Match/Capture Interrupt",
                'cn': "PCA模块2 匹配捕获中断",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """PCA模块2 匹配捕获中断"""

        self.ECCF3 = SFRBitsModel(
            self.CCAPM3, "ECCF3", 0,
            {
                'en': "PCA Module3 Match/Capture Interrupt",
                'cn': "PCA模块3 匹配捕获中断",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'Disallow', 'cn': '禁止'},
                '1': {'en': 'Allow', 'cn': '允许'},
            }
        )
        """PCA模块3 匹配捕获中断"""

        self.EBS0 = SFRBitsModel(
            self.PCA_PWM0, "EBS0", 6,
            {
                'en': "PCA Module0 PWM Bits Width Control",
                'cn': "PCA模块0 PWM位数控制",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '8-bit', 'cn': '8-bit'},
                '1': {'en': '7-bit', 'cn': '7-bit'},
                '2': {'en': '6-bit', 'cn': '6-bit'},
                '3': {'en': '10-bit', 'cn': '10-bit'},
            }
        )
        """PCA模块0 PWM位数控制"""

        self.EBS1 = SFRBitsModel(
            self.PCA_PWM1, "EBS1", 6,
            {
                'en': "PCA Module1 PWM Bits Width Control",
                'cn': "PCA模块1 PWM位数控制",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '8-bit', 'cn': '8-bit'},
                '1': {'en': '7-bit', 'cn': '7-bit'},
                '2': {'en': '6-bit', 'cn': '6-bit'},
                '3': {'en': '10-bit', 'cn': '10-bit'},
            }
        )
        """PCA模块1 PWM位数控制"""

        self.EBS2 = SFRBitsModel(
            self.PCA_PWM2, "EBS2", 6,
            {
                'en': "PCA Module2 PWM Bits Width Control",
                'cn': "PCA模块2 PWM位数控制",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '8-bit', 'cn': '8-bit'},
                '1': {'en': '7-bit', 'cn': '7-bit'},
                '2': {'en': '6-bit', 'cn': '6-bit'},
                '3': {'en': '10-bit', 'cn': '10-bit'},
            }
        )
        """PCA模块2 PWM位数控制"""

        self.EBS3 = SFRBitsModel(
            self.PCA_PWM3, "EBS3", 6,
            {
                'en': "PCA Module3 PWM Bits Width Control",
                'cn': "PCA模块3 PWM位数控制",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': '8-bit', 'cn': '8-bit'},
                '1': {'en': '7-bit', 'cn': '7-bit'},
                '2': {'en': '6-bit', 'cn': '6-bit'},
                '3': {'en': '10-bit', 'cn': '10-bit'},
            }
        )
        """PCA模块3 PWM位数控制"""


        # __init__ end
