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
        self.P_SW1     = SFRModel('P_SW1',     0xA2, 0, 0x00, dict(en='Peripheral Port Switch: UART1,CCP/PWM,SPI', cn='外设端口切换控制寄存器1,串口1,CCP/PWM,SPI'))
        self.P_SW2     = SFRModel('P_SW2',     0xBA, 0, 0x00, dict(en='Peripheral Port Switch Control: UART2/3/4,I2C,COMP', cn='外设端口切换控制寄存器2,串口2/3/4,I2C,比较器'))
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

        self.MX_PWM0_DUTY_CYCLE = ValueModel(
            'MX_PWM0_DUTY_CYCLE',
            50.0,
            {
                'en': "PCA Module0 PWM Duty Cycle, Value Between [0.0, 100.0]",
                'cn': "PCA模块0 PWM 占空比, 取值[0.0, 100.0]",
            },
            type='float',
            valid=lambda a: 0.0 <= a <= 100.0,
        )
        """PCA模块0 PWM占空比"""

        self.MX_PWM1_DUTY_CYCLE = ValueModel(
            'MX_PWM1_DUTY_CYCLE',
            50.0,
            {
                'en': "PCA Module1 PWM Duty Cycle, Value Between [0.0, 100.0]",
                'cn': "PCA模块1 PWM 占空比, 取值[0.0, 100.0]",
            },
            type='float',
            valid=lambda a: 0.0 <= a <= 100.0,
        )
        """PCA模块1 PWM占空比"""

        self.MX_PWM2_DUTY_CYCLE = ValueModel(
            'MX_PWM2_DUTY_CYCLE',
            50.0,
            {
                'en': "PCA Module2 PWM Duty Cycle, Value Between [0.0, 100.0]",
                'cn': "PCA模块2 PWM 占空比, 取值[0.0, 100.0]",
            },
            type='float',
            valid=lambda a: 0.0 <= a <= 100.0,
        )
        """PCA模块2 PWM占空比"""

        self.MX_PWM3_DUTY_CYCLE = ValueModel(
            'MX_PWM3_DUTY_CYCLE',
            50.0,
            {
                'en': "PCA Module3 PWM Duty Cycle, Value Between [0.0, 100.0]",
                'cn': "PCA模块3 PWM 占空比, 取值[0.0, 100.0]",
            },
            type='float',
            valid=lambda a: 0.0 <= a <= 100.0,
        )
        """PCA模块3 PWM占空比"""

        # SFR Bits

        self.S1_S = SFRBitsModel(
            self.P_SW1, 'S1_S', 6,
            {
                'en': "UART1 Port Select",
                'cn': "串口1管脚选择",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {'en': 'RX:P3.0, TX:P3.1', 'cn': 'RX:P3.0, TX:P3.1'},
                '1': {'en': 'RX:P3.6, TX:P3.7', 'cn': 'RX:P3.6, TX:P3.7'},
                '2': {'en': 'RX:P1.6, TX:P1.7', 'cn': 'RX:P1.6, TX:P1.7'},
                '3': {'en': 'RX:P4.3, TX:P4.4', 'cn': 'RX:P4.3, TX:P4.4'},
            }
        )
        """串口1管脚选择"""

        self.CCP_S = SFRBitsModel(
            self.P_SW1, 'CCP_S', 4,
            {
                'en': "PCA/PWM Port Select",
                'cn': "PCA/PWM管脚选择",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {
                    'en': 'ECI:P1.2, CCP0:P1.7, CCP1:P1.6, CCP2:P1.5, CCP3:P1.4',
                    'cn': 'ECI:P1.2, CCP0:P1.7, CCP1:P1.6, CCP2:P1.5, CCP3:P1.4'},
                '1': {
                    'en': 'ECI:P2.2, CCP0:P2.3, CCP1:P2.4, CCP2:P2.5, CCP3:P2.6',
                    'cn': 'ECI:P2.2, CCP0:P2.3, CCP1:P2.4, CCP2:P2.5, CCP3:P2.6'},
                '2': {
                    'en': 'ECI:P7.4, CCP0:P7.0, CCP1:P7.1, CCP2:P7.2, CCP3:P7.3',
                    'cn': 'ECI:P7.4, CCP0:P7.0, CCP1:P7.1, CCP2:P7.2, CCP3:P7.3'},
                '3': {
                    'en': 'ECI:P3.5, CCP0:P3.3, CCP1:P3.2, CCP2:P3.1, CCP3:P3.0',
                    'cn': 'ECI:P3.5, CCP0:P3.3, CCP1:P3.2, CCP2:P3.1, CCP3:P3.0'},
            }
        )
        """PCA/PWM管脚选择"""

        self.SPI_S = SFRBitsModel(
            self.P_SW1, 'SPI_S', 2,
            {
                'en': "SPI Port Select",
                'cn': "SPI管脚选择",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {
                    'en': 'SS:P1.2, MOSI:P1.3, MISO:P1.4, SCLK:P1.5',
                    'cn': 'SS:P1.2, MOSI:P1.3, MISO:P1.4, SCLK:P1.5'},
                '1': {
                    'en': 'SS:P2.2, MOSI:P2.3, MISO:P2.4, SCLK:P2.5',
                    'cn': 'SS:P2.2, MOSI:P2.3, MISO:P2.4, SCLK:P2.5'},
                '2': {
                    'en': 'SS:P7.4, MOSI:P7.5, MISO:P7.6, SCLK:P7.7',
                    'cn': 'SS:P7.4, MOSI:P7.5, MISO:P7.6, SCLK:P7.7'},
                '3': {
                    'en': 'SS:P3.5, MOSI:P3.4, MISO:P3.3, SCLK:P3.2',
                    'cn': 'SS:P3.5, MOSI:P3.4, MISO:P3.3, SCLK:P3.2'},
            }
        )
        """SPI管脚选择"""

        self.I2C_S = SFRBitsModel(
            self.P_SW2, 'I2C_S', 4,
            {
                'en': "I2C Port Select",
                'cn': "I2C管脚选择",
            },
            len=2,
            values={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
            options={
                '0': {
                    'en': 'SCL:P1.5, SDA:P1.4',
                    'cn': 'SCL:P1.5, SDA:P1.4'},
                '1': {
                    'en': 'SCL:P2.5, SDA:P2.4',
                    'cn': 'SCL:P2.5, SDA:P2.4'},
                '2': {
                    'en': 'SCL:P7.7, SDA:P7.6',
                    'cn': 'SCL:P7.7, SDA:P7.6'},
                '3': {
                    'en': 'SCL:P3.2, SDA:P3.3',
                    'cn': 'SCL:P3.2, SDA:P3.3'},
            }
        )
        """I2C管脚选择"""

        self.CMPO_S = SFRBitsModel(
            self.P_SW2, 'CMPO_S', 3,
            {
                'en': "COMP Output Port Select",
                'cn': "比较器输出脚选择",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': { 'en': 'P3.4', 'cn': 'P3.4'},
                '1': { 'en': 'P4.1', 'cn': 'P4.1'},
            }
        )
        """比较器输出脚选择"""

        self.S4_S = SFRBitsModel(
            self.P_SW2, 'S4_S', 2,
            {
                'en': "UART4 Port Select",
                'cn': "串口4管脚选择",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'RX:P0.2, TX:P0.3', 'cn': 'RX:P0.2, TX:P0.3'},
                '1': {'en': 'RX:P5.2, TX:P5.3', 'cn': 'RX:P5.2, TX:P5.3'},
            }
        )
        """串口4管脚选择"""

        self.S3_S = SFRBitsModel(
            self.P_SW2, 'S3_S', 1,
            {
                'en': "UART3 Port Select",
                'cn': "串口3管脚选择",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'RX:P0.0, TX:P0.1', 'cn': 'RX:P0.0, TX:P0.1'},
                '1': {'en': 'RX:P5.0, TX:P5.1', 'cn': 'RX:P5.0, TX:P5.1'},
            }
        )
        """串口3管脚选择"""

        self.S2_S = SFRBitsModel(
            self.P_SW2, 'S2_S', 0,
            {
                'en': "UART2 Port Select",
                'cn': "串口2管脚选择",
            },
            values={'0': 0B0, '1': 0B1},
            options={
                '0': {'en': 'RX:P1.0, TX:P1.1', 'cn': 'RX:P1.0, TX:P1.1'},
                '1': {'en': 'RX:P4.0, TX:P4.2', 'cn': 'RX:P4.0, TX:P4.2'},
            }
        )
        """串口2管脚选择"""

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
            },
            sbit=True
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
                'cn': "PCA模块0 比较功能",
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
                'cn': "PCA模块1 比较功能",
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
                'cn': "PCA模块2 比较功能",
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
                'cn': "PCA模块3 比较功能",
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
                'cn': "PCA模块0 上升沿捕获",
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
                'cn': "PCA模块1 上升沿捕获",
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
                'cn': "PCA模块2 上升沿捕获",
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
                'cn': "PCA模块3 上升沿捕获",
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
                'cn': "PCA模块0 下降沿捕获",
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
                'cn': "PCA模块1 下降沿捕获",
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
                'cn': "PCA模块2 下降沿捕获",
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
                'cn': "PCA模块3 下降沿捕获",
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
                'cn': "PCA模块0 匹配功能",
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
                'cn': "PCA模块1 匹配功能",
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
                'cn': "PCA模块2 匹配功能",
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
                'cn': "PCA模块3 匹配功能",
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
                'cn': "PCA模块0 脉冲输出",
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
                'cn': "PCA模块1 脉冲输出",
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
                'cn': "PCA模块2 脉冲输出",
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
                'cn': "PCA模块3 脉冲输出",
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
                '0': {
                    'en': '8-bit, reload:{EPC0H, CCAP0H[7:0]}, compare:{EPC0L, CCAP0L[7:0]}',
                    'cn': '8-bit, 重载:{EPC0H, CCAP0H[7:0]}, 比较值:{EPC0L, CCAP0L[7:0]}'},
                '1': {
                    'en': '7-bit, reload:{EPC0H, CCAP0H[6:0]}, compare:{EPC0L, CCAP0L[6:0]}',
                    'cn': '7-bit, 重载:{EPC0H, CCAP0H[6:0]}, 比较值:{EPC0L, CCAP0L[6:0]}'},
                '2': {
                    'en': '6-bit, reload:{EPC0H, CCAP0H[5:0]}, compare:{EPC0L, CCAP0L[5:0]}',
                    'cn': '6-bit, 重载:{EPC0H, CCAP0H[5:0]}, 比较值:{EPC0L, CCAP0L[5:0]}'},
                '3': {
                    'en': '10-bit, reload:{EPC0H XCCAP0H[1:0] CCAP0H[7:0]}, compare:{EPC0L XCCAP0L[1:0] CCAP0L[7:0]}',
                    'cn': '10-bit, 重载:{EPC0H, XCCAP0H[1:0], CCAP0H[7:0]}, 比较值:{EPC0L, XCCAP0L[1:0], CCAP0L[7:0]}'
                },
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
                '0': {
                    'en': '8-bit, reload:{EPC1H, CCAP1H[7:0]}, compare:{EPC1L, CCAP1L[7:0]}',
                    'cn': '8-bit, 重载:{EPC1H, CCAP1H[7:0]}, 比较值:{EPC1L, CCAP1L[7:0]}'},
                '1': {
                    'en': '7-bit, reload:{EPC1H, CCAP1H[6:0]}, compare:{EPC1L, CCAP1L[6:0]}',
                    'cn': '7-bit, 重载:{EPC1H, CCAP1H[6:0]}, 比较值:{EPC1L, CCAP1L[6:0]}'},
                '2': {
                    'en': '6-bit, reload:{EPC1H, CCAP1H[5:0]}, compare:{EPC1L, CCAP1L[5:0]}',
                    'cn': '6-bit, 重载:{EPC1H, CCAP1H[5:0]}, 比较值:{EPC1L, CCAP1L[5:0]}'},
                '3': {
                    'en': '10-bit, reload:{EPC1H XCCAP1H[1:0] CCAP1H[7:0]}, compare:{EPC1L XCCAP1L[1:0] CCAP1L[7:0]}',
                    'cn': '10-bit, 重载:{EPC1H, XCCAP1H[1:0], CCAP1H[7:0]}, 比较值:{EPC1L, XCCAP1L[1:0], CCAP1L[7:0]}'
                },
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
                '0': {
                    'en': '8-bit, reload:{EPC2H, CCAP2H[7:0]}, compare:{EPC2L, CCAP2L[7:0]}',
                    'cn': '8-bit, 重载:{EPC2H, CCAP2H[7:0]}, 比较值:{EPC2L, CCAP2L[7:0]}'},
                '1': {
                    'en': '7-bit, reload:{EPC2H, CCAP2H[6:0]}, compare:{EPC2L, CCAP2L[6:0]}',
                    'cn': '7-bit, 重载:{EPC2H, CCAP2H[6:0]}, 比较值:{EPC2L, CCAP2L[6:0]}'},
                '2': {
                    'en': '6-bit, reload:{EPC2H, CCAP2H[5:0]}, compare:{EPC2L, CCAP2L[5:0]}',
                    'cn': '6-bit, 重载:{EPC2H, CCAP2H[5:0]}, 比较值:{EPC2L, CCAP0L[5:0]}'},
                '3': {
                    'en': '10-bit, reload:{EPC2H XCCAP2H[1:0] CCAP2H[7:0]}, compare:{EPC2L XCCAP2L[1:0] CCAP2L[7:0]}',
                    'cn': '10-bit, 重载:{EPC2H, XCCAP2H[1:0], CCAP2H[7:0]}, 比较值:{EPC2L, XCCAP2L[1:0], CCAP2L[7:0]}'
                },
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
                '0': {
                    'en': '8-bit, reload:{EPC3H, CCAP3H[7:0]}, compare:{EPC3L, CCAP3L[7:0]}',
                    'cn': '8-bit, 重载:{EPC3H, CCAP3H[7:0]}, 比较值:{EPC3L, CCAP3L[7:0]}'},
                '1': {
                    'en': '7-bit, reload:{EPC3H, CCAP3H[6:0]}, compare:{EPC3L, CCAP3L[6:0]}',
                    'cn': '7-bit, 重载:{EPC3H, CCAP3H[6:0]}, 比较值:{EPC3L, CCAP3L[6:0]}'},
                '2': {
                    'en': '6-bit, reload:{EPC3H, CCAP3H[5:0]}, compare:{EPC3L, CCAP3L[5:0]}',
                    'cn': '6-bit, 重载:{EPC3H, CCAP3H[5:0]}, 比较值:{EPC3L, CCAP3L[5:0]}'},
                '3': {
                    'en': '10-bit, reload:{EPC3H XCCAP3H[1:0] CCAP3H[7:0]}, compare:{EPC3L XCCAP3L[1:0] CCAP3L[7:0]}',
                    'cn': '10-bit, 重载:{EPC3H, XCCAP3H[1:0], CCAP3H[7:0]}, 比较值:{EPC3L, XCCAP3L[1:0], CCAP3L[7:0]}'
                },
            }
        )
        """PCA模块3 PWM位数控制"""

        self.CCAP0LV = SFRBitsModel(
            self.CCAP0L, 'CCAP0LV', 0,
            {
                'en': 'PCA Module0 Comparison Value',
                'cn': 'PCA模块0 比较值'
            },
            len=8
        )
        """PCA模块0 比较值"""

        self.CCAP1LV = SFRBitsModel(
            self.CCAP1L, 'CCAP1LV', 0,
            {
                'en': 'PCA Module1 Comparison Value',
                'cn': 'PCA模块1 比较值'
            },
            len=8
        )
        """PCA模块1 比较值"""

        self.CCAP2LV = SFRBitsModel(
            self.CCAP2L, 'CCAP2LV', 0,
            {
                'en': 'PCA Module2 Comparison Value',
                'cn': 'PCA模块2 比较值'
            },
            len=8
        )
        """PCA模块2 比较值"""

        self.CCAP3LV = SFRBitsModel(
            self.CCAP3L, 'CCAP3LV', 0,
            {
                'en': 'PCA Module3 Comparison Value',
                'cn': 'PCA模块3 比较值'
            },
            len=8
        )
        """PCA模块3 比较值"""

        self.CCAP0HV = SFRBitsModel(
            self.CCAP0H, 'CCAP0HV', 0,
            {
                'en': 'PCA Module0 Reload Value',
                'cn': 'PCA模块0 重载值'
            },
            len=8
        )
        """PCA模块0 重载值"""

        self.CCAP1HV = SFRBitsModel(
            self.CCAP1H, 'CCAP1HV', 0,
            {
                'en': 'PCA Module1 Reload Value',
                'cn': 'PCA模块1 重载值'
            },
            len=8
        )
        """PCA模块1 重载值"""

        self.CCAP2HV = SFRBitsModel(
            self.CCAP2H, 'CCAP2HV', 0,
            {
                'en': 'PCA Module2 Reload Value',
                'cn': 'PCA模块2 重载值'
            },
            len=8
        )
        """PCA模块2 重载值"""

        self.CCAP3HV = SFRBitsModel(
            self.CCAP3H, 'CCAP3HV', 0,
            {
                'en': 'PCA Module3 Reload Value',
                'cn': 'PCA模块3 重载值'
            },
            len=8
        )
        """PCA模块3 重载值"""

        self.XCCAP0L = SFRBitsModel(
            self.PCA_PWM0, 'XCCAP0L', 2,
            {
                'en': 'PCA Module0 10-bit PWM, 9th and 10th bit of Comparison Value',
                'cn': 'PCA模块0 10位PWM的第9第10位的比较值'
            },
            len=2
        )
        """PCA模块0 10位PWM的第9第10位的比较值"""

        self.XCCAP1L = SFRBitsModel(
            self.PCA_PWM1, 'XCCAP1L', 2,
            {
                'en': 'PCA Module1 10-bit PWM, 9th and 10th bit of Comparison Value',
                'cn': 'PCA模块1 10位PWM的第9第10位的比较值'
            },
            len=2
        )
        """PCA模块1 10位PWM的第9第10位的比较值"""

        self.XCCAP2L = SFRBitsModel(
            self.PCA_PWM2, 'XCCAP2L', 2,
            {
                'en': 'PCA Module2 10-bit PWM, 9th and 10th bit of Comparison Value',
                'cn': 'PCA模块2 10位PWM的第9第10位的比较值'
            },
            len=2
        )
        """PCA模块2 10位PWM的第9第10位的比较值"""

        self.XCCAP3L = SFRBitsModel(
            self.PCA_PWM3, 'XCCAP3L', 2,
            {
                'en': 'PCA Module3 10-bit PWM, 9th and 10th bit of Comparison Value',
                'cn': 'PCA模块3 10位PWM的第9第10位的比较值'
            },
            len=2
        )
        """PCA模块3 10位PWM的第9第10位的比较值"""

        self.XCCAP0H = SFRBitsModel(
            self.PCA_PWM0, 'XCCAP0H', 4,
            {
                'en': 'PCA Module0 10-bit PWM, 9th and 10th bit of Reload Value',
                'cn': 'PCA模块0 10位PWM的第9第10位的重载值'
            },
            len=2
        )
        """PCA模块0 10位PWM的第9第10位的重载值"""

        self.XCCAP1H = SFRBitsModel(
            self.PCA_PWM1, 'XCCAP1H', 4,
            {
                'en': 'PCA Module1 10-bit PWM, 9th and 10th bit of Reload Value',
                'cn': 'PCA模块1 10位PWM的第9第10位的重载值'
            },
            len=2
        )
        """PCA模块1 10位PWM的第9第10位的重载值"""

        self.XCCAP2H = SFRBitsModel(
            self.PCA_PWM2, 'XCCAP2H', 4,
            {
                'en': 'PCA Module2 10-bit PWM, 9th and 10th bit of Reload Value',
                'cn': 'PCA模块2 10位PWM的第9第10位的重载值'
            },
            len=2
        )
        """PCA模块2 10位PWM的第9第10位的重载值"""

        self.XCCAP3H = SFRBitsModel(
            self.PCA_PWM3, 'XCCAP3H', 4,
            {
                'en': 'PCA Module3 10-bit PWM, 9th and 10th bit of Reload Value',
                'cn': 'PCA模块3 10位PWM的第9第10位的重载值'
            },
            len=2
        )
        """PCA模块3 10位PWM的第9第10位的重载值"""


        # __init__ end
