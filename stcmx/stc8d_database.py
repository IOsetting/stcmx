from stcmx.sfr_model import SFRModel
from stcmx.sfrbits_model import SFRBitsModel
from stcmx.stc8_config import Stc8Config
import stcmx.util as util


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

        # SFR Bits
        self.MCLKOCRDIV = SFRBitsModel(
            self.MCLKOCR, 'MCLKOCRDIV', 0,
            {
                'en': "Please input the out clock division, value in range [0, 127]\n" +
                      "  0:No output,\n" +
                      "  1~127: output = SYSCLK/division",
                'cn': "请输入时钟输出的分频系数, 取值范围[0, 127]\n" +
                      "  0:不输出,\n" +
                      "  1~127: 输出频率 = SYSCLK/分频系数",
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
                'cn': "运行定时器0",
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
                'cn': "运行定时器1",
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
                'cn': "运行定时器2",
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
                'en': '',
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

    def generate(self):
        print("Code for current configuration:\n MCU Type: %s\n"%self.name)
        print('''#include "stc8a8k64d4.h"
''')
        print("void init()\n{")
        # extend ROM
        self.P_SW2.set_bits(0B1, 0B1, 7)
        self.P_SW2.output_code(self.verbose, self.lang, force=True)
        self.CKSEL.output_code(self.verbose, self.lang)
        self.HIRCCR.output_code(self.verbose, self.lang)
        self.XOSCCR.output_code(self.verbose, self.lang)
        self.IRC32KCR.output_code(self.verbose, self.lang)
        self.MCLKOCR.output_code(self.verbose, self.lang)
        self.CLKDIV.output_code(self.verbose, self.lang)
        self.IRCBAND.output_code(self.verbose, self.lang)
        self.VRTRIM.output_code(self.verbose, self.lang)
        self.IRTRIM.output_code(self.verbose, self.lang)
        self.LIRTRIM.output_code(self.verbose, self.lang)
        self.T2H.output_code(self.verbose, self.lang)
        self.T2L.output_code(self.verbose, self.lang)
        self.P_SW2.reset()
        self.P_SW2.output_code(self.verbose, self.lang, force=True)
        print('')
        # internal RAM
        self.SCON.output_code(self.verbose, self.lang)
        self.PCON.output_code(self.verbose, self.lang)
        self.AUXR.output_code(self.verbose, self.lang)
        self.TCON.output_code(self.verbose, self.lang)
        self.TMOD.output_code(self.verbose, self.lang)
        self.TH0.output_code(self.verbose, self.lang)
        self.TL0.output_code(self.verbose, self.lang)
        self.TH1.output_code(self.verbose, self.lang)
        self.TL1.output_code(self.verbose, self.lang)
        print("}")

    def info(self):
        print("/** FOSC: %s, SYSCLK: %s */" % (
             util.format_frequency(self.FOSC), util.format_frequency(self.SYSCLK)))
