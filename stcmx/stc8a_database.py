from stcmx.sfr_model import SFRModel
from stcmx.stc8_config import Stc8Config
import stcmx.util as util


class Stc8aDatabase(Stc8Config):
    """Database that holds STC8 SFR information."""

    OPTIONS:dict = {
        'cpuid': '0',
    }

    # Special Address in ROM, store chip related info, including UUID, 32KHz wakeup clock, 1.344V ref and Internal RC OSC value
    CPUIDBASE:dict = {
        '0':  0x1FF3, # STC8F1K08, STC8F1K08S2
        '1':  0x2FF3, # STC8F1K12, STC8F1K12S2
        '2':  0x43F3, # STC8F1K17, STC8F1K17S2
        '3':  0x3FF3, # STC8A8K16S4A12 STC8A4K16S4A12 STC8F2K16S4 STC8F2K16S2
        '4':  0x7FF3, # STC8A8K32S4A12 STC8A4K32S4A12 STC8F2K32S4 STC8F2K32S2
        '5':  0xEFF3, # STC8A8K60S4A12 STC8A4K60S4A12 STC8F2K60S4 STC8F2K60S2
        '6' : 0xFDF3, # STC8A8K64S4A12 STC8A4K64S4A12 STC8F2K64S4 STC8F2K64S2
    }

    # Basic SFR

    # Extend RAM SFR
    IRC24MCR = SFRModel('IRC24MCR', 0xFE02, 1, 0x80, dict(en='Internal High Speed OSC Control', cn='内部24M振荡器控制寄存器'))
    ADCTIM   = SFRModel('ADCTIM', 0xFEA8, 1, 0x80, dict(en='ADC Time Sequence Control', cn='ADC时序控制寄存器'))

    def __init__(self):
        super().__init__()
        self.name = "STC8A,STC8C,STC8F Series"

    def generate(self):
        print("Code for current configuration:\n")
        # CPUID define
        print("#define CPUIDBASE 0x%04X" % self.CPUIDBASE[self.OPTIONS['cpuid']])
        print('''
#define T24M_ADDR     (*(unsigned char volatile xdata *)(CPUIDBASE + 0x00))
#define T22M1184_ADDR (*(unsigned char volatile xdata *)(CPUIDBASE + 0x01))
#define F32K_ADDR     (*(unsigned char volatile xdata *)(CPUIDBASE + 0x02))
#define BANDGAP_ADDR  (*(unsigned char volatile xdata *)(CPUIDBASE + 0x04))
#define UUID_ADDR     (*(unsigned char volatile xdata *)(CPUIDBASE + 0x06))
        ''')
        print("void init()\n{")
        # extend ROM
        self.P_SW2.set_bits(0B1, 0B1, 7)
        self.P_SW2.output_code(self.verbose, self.lang, force=True)
        self.CKSEL.output_code(self.verbose, self.lang)
        self.IRC24MCR.output_code(self.verbose, self.lang)
        self.XOSCCR.output_code(self.verbose, self.lang)
        self.IRC32KCR.output_code(self.verbose, self.lang)
        self.CLKDIV.output_code(self.verbose, self.lang)
        self.P_SW2.reset()
        self.P_SW2.output_code(self.verbose, self.lang, force=True)
        print('')
        # internal RAM
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
