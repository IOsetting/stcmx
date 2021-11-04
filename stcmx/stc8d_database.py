from stcmx.sfr_model import SFRModel
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

    # Basic SFR
    IRCBAND = SFRModel('IRCBAND',   0x9D, 0, 0x00, dict(en='Internal OSC Band Select', cn='IRC频段选择'))
    VRTRIM  = SFRModel('VRTRIM',    0xA6, 0, 0x00, dict(en='Internal OSC Band Frequency Adjust', cn='IRC频段频率调节'))

    # Extend RAM SFR
    HIRCCR  = SFRModel('HIRCCR',    0xFE02, 1, 0x80, dict(en='Internal High Speed OSC Control',cn='内部高速振荡器控制寄存器'))

    MCLKOCR = SFRModel('MCLKOCR',   0xFE05, 1, 0x00, dict(en='Clock Output Control',cn='主时钟输出控制寄存器'))
    IRCDB   = SFRModel('IRCDB',     0xFE06, 1, 0x80, dict(en='Internal OSC Calibration Control', cn='内部IRC起振去抖控制'))

    TM2PS   = SFRModel('TM2PS',     0xFEA2, 1, 0x80, dict(en='Timer2 prescale', cn='定时器2时钟预分频寄存器'))
    TM3PS   = SFRModel('TM3PS',     0xFEA3, 1, 0x80, dict(en='Timer3 prescale', cn='定时器3时钟预分频寄存器'))
    TM4PS   = SFRModel('TM4PS',     0xFEA4, 1, 0x80, dict(en='Timer4 prescale', cn='定时器4时钟预分频寄存器'))

    def __init__(self):
        super().__init__()
        self.name = "STC8A8KxxDx Series"

    def generate(self):
        print("Code for current configuration:\n MCU Type: %s\n"%self.name)
        print('''
#define CPUIDBASE 0xFDE0

SFRX(ID_ADDR,        CPUIDBASE + 0x00);
SFR16LEX(VREF_ADDR,  CPUIDBASE + 0x07);
SFR16LEX(F32K_ADDR,  CPUIDBASE + 0x09);
SFRX(T22M_ADDR,      CPUIDBASE + 0x0b); // 22.1184MHz
SFRX(T24M_ADDR,      CPUIDBASE + 0x0c); // 24MHz
SFRX(T20M_ADDR,      CPUIDBASE + 0x0d); // 20MHz
SFRX(T27M_ADDR,      CPUIDBASE + 0x0e); // 27MHz
SFRX(T30M_ADDR,      CPUIDBASE + 0x0f); // 30MHz
SFRX(T33M_ADDR,      CPUIDBASE + 0x10); // 33.1776MHz
SFRX(T35M_ADDR,      CPUIDBASE + 0x11); // 35MHz
SFRX(T36M_ADDR,      CPUIDBASE + 0x12); // 36.864MHz
SFRX(T40M_ADDR,      CPUIDBASE + 0x13); // 40MHz
SFRX(T45M_ADDR,      CPUIDBASE + 0x14); // 45MHz
SFRX(VRT6M_ADDR,     CPUIDBASE + 0x15); // VRTRIM_6M
SFRX(VRT10M_ADDR,    CPUIDBASE + 0x16); // VRTRIM_10M
SFRX(VRT27M_ADDR,    CPUIDBASE + 0x17); // VRTRIM_27M
SFRX(VRT44M_ADDR,    CPUIDBASE + 0x18); // VRTRIM_44M
SFR(VRTRIM,          0xA6);
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
        self.P_SW2.reset()
        self.P_SW2.output_code(self.verbose, self.lang, force=True)
        print('')
        # internal RAM
        self.IRCBAND.output_code(self.verbose, self.lang)
        self.VRTRIM.output_code(self.verbose, self.lang)
        self.IRTRIM.output_code(self.verbose, self.lang)
        self.LIRTRIM.output_code(self.verbose, self.lang)
        self.SCON.output_code(self.verbose, self.lang)
        self.PCON.output_code(self.verbose, self.lang)
        self.AUXR.output_code(self.verbose, self.lang)
        self.TCON.output_code(self.verbose, self.lang)
        self.TMOD.output_code(self.verbose, self.lang)
        self.TH0.output_code(self.verbose, self.lang)
        self.TL0.output_code(self.verbose, self.lang)
        print("}")

    def info(self):
        print("/** FOSC: %s, SYSCLK: %s */" % (
             util.format_frequency(self.FOSC), util.format_frequency(self.SYSCLK)))
