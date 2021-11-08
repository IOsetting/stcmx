from stcmx.stc8a_database import Stc8aDatabase
from stcmx.config_control import ConfigControl
from stcmx.util import InputHelper,SelectHelper


class Stc8aConfig(Stc8aDatabase, ConfigControl):

    def __init__(self):
        super().__init__()
        self.FOSC = 24000000

    def define_clock(self):
        self.print({
            'en': "==== SYSTEM CLOCK CONFIG START ====",
            'cn': "==== 系统时钟配置开始 ====",
        })
        self.cpuid_select()
        self.clock_source_select()
        self.set_fosc()
        self.frequency_adjust()
        v = self.CLKDIV_0.select(self.lang)
        # 设置时钟输出
        v = self.MCLKODIV.select(self.lang)
        if v != 0x00:
            # 时钟输出脚选择
            self.MCLKO_S.select(self.lang)
        self.print({
            'en': "==== SYSTEM CLOCK CONFIG END ====",
            'cn': "==== 系统时钟配置结束 ====",
        })

    def define_power(self):
        self.print({
            'en': "==== POWER CONFIG START ====",
            'cn': "==== 电源配置开始 ====",
        })
        self.PCON_PD.select(self.lang)
        self.PCON_IDEL.select(self.lang)
        self.print({
            'en': "==== POWER CONFIG END ====",
            'cn': "==== 电源配置结束 ====",
        })

    def define_uart(self):
        self.print({
            'en': "==== UART CONFIG START ====",
            'cn': "==== 串口配置开始 ====",
        })
        self.uart1_mode_select()
        self.SCON_REN.select(self.lang)
        self.uart1_mode1_mode3_baud_rate_source_select()
        self.uart1_mode0_baud_rate_control()
        self.uart1_mode123_double_baud_rate_control()
        self.uart1_frame_err_detect_control()
        self.print({
            'en': "==== UART CONFIG END ====",
            'cn': "==== 串口配置结束 ====",
        })

    def cpuid_select(self):
        opt = SelectHelper(
            {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6'},
            {
                'en': "Please select MCU type\n:" +
                      "  0: STC8F1K08, STC8F1K08S2\n" +
                      "  1: STC8F1K12, STC8F1K12S2\n" +
                      "  2: STC8F1K17, STC8F1K17S2\n" +
                      "  3: STC8A8K16S4A12 STC8A4K16S4A12 STC8F2K16S4 STC8F2K16S2\n" +
                      "  4: STC8A8K32S4A12 STC8A4K32S4A12 STC8F2K32S4 STC8F2K32S2\n" +
                      "  5: STC8A8K60S4A12 STC8A4K60S4A12 STC8F2K60S4 STC8F2K60S2\n" +
                      "  6: STC8A8K64S4A12 STC8A4K64S4A12 STC8F2K64S4 STC8F2K64S2\n[%s]:",
                'cn': "请选择芯片型号\n:" +
                      "  0: STC8F1K08, STC8F1K08S2\n" +
                      "  1: STC8F1K12, STC8F1K12S2\n" +
                      "  2: STC8F1K17, STC8F1K17S2\n" +
                      "  3: STC8A8K16S4A12 STC8A4K16S4A12 STC8F2K16S4 STC8F2K16S2\n" +
                      "  4: STC8A8K32S4A12 STC8A4K32S4A12 STC8F2K32S4 STC8F2K32S2\n" +
                      "  5: STC8A8K60S4A12 STC8A4K60S4A12 STC8F2K60S4 STC8F2K60S2\n" +
                      "  6: STC8A8K64S4A12 STC8A4K64S4A12 STC8F2K64S4 STC8F2K64S2\n[%s]:",
            },
            '0'
        )
        self.OPTIONS['cpuid'] = opt.select(self.lang)

    def clock_source_select(self):
        """Select the clock source"""
        value = self.MCKSEL.select(self.lang)
        if value == 0B00:
            self.IRC24MCR.set_bits(0B1, 0B1, 7)
            self.XOSCCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B0, 0B1, 6)
            self.IRC32KCR.set_bits(0B0, 0B1, 7)
        elif value == 0B01:
            self.IRC24MCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B1, 0B1, 7)
            self.XOSCCR.set_bits(0B1, 0B1, 6)
            self.IRC32KCR.set_bits(0B0, 0B1, 7)
        elif value == 0B10:
            self.IRC24MCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B1, 0B1, 7)
            self.XOSCCR.set_bits(0B0, 0B1, 6)
            self.IRC32KCR.set_bits(0B0, 0B1, 7)
        elif value == 0B11:
            self.IRC24MCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B0, 0B1, 6)
            self.IRC32KCR.set_bits(0B1, 0B1, 7)

    def set_fosc(self):
        """Set IRTRIM according to input frequency"""

        if self.MCKSEL.get_value() == 0B01 or self.MCKSEL.get_value() == 0B10:
            opt = InputHelper(
                {
                    'en': "Please input the external OSC/CLK frequency, value in range [4500000, 28000000]\n[%d]:",
                    'cn': "请输入外部振荡源或时钟频率, 值必须在[4500000, 28000000]区间内\n[%d]:",
                },
                self.FOSC,
                valid=lambda a: (4500000 <= int(a) <= 28000000)
            )
            self.FOSC = int(opt.input(self.lang))
            self.IRC24MCR.reset()
            self.IRTRIM.reset()
            return
        elif self.MCKSEL.get_value() == 0B11:
            self.FOSC = 32768
            self.IRC24MCR.reset()
            self.IRTRIM.reset()
            return

        """For internal RC oscillator, we need to carefully make it close to the target frequency"""
        # Calculate possible frequency range
        opt = InputHelper(
            {
                'en': "Please input the frequency, value in range [16000000, 28000000]\n[%d]:",
                'cn': "请输入频率, 可调节频率范围区间为[16000000, 28000000]\n[%d]:",
            },
            self.FOSC,
            valid=lambda a: (16000000 <= int(a) <= 28000000)
        )
        val = int(opt.input(self.lang))
        # For built-in fixed 24MHz and 22.1184MHz, use rom value
        if val == 24000000:
            self.IRTRIM.assignment = 'T24M_ADDR'
            self.FOSC = 24000000
            return
        elif val == 22118400:
            self.IRTRIM.assignment = 'T22M1184_ADDR'
            self.FOSC = 22118400
            return
        # For other frequencies, calculate basing on fixed
        irtrim = 0
        if 16000000 <= val < 22118400:
            base_freq = 22118400
            while True:
                if base_freq / 1.0024 < val:
                    break
                irtrim += 1
                base_freq = base_freq / 1.0024
            self.IRTRIM.assignment = "T22M1184_ADDR - %d" % irtrim
            self.FOSC = int(base_freq)
        elif val <= 24000000:
            base_freq = 24000000
            while True:
                if base_freq / 1.0024 < val:
                    break
                irtrim += 1
                base_freq = base_freq / 1.0024
            self.IRTRIM.assignment = "T24M_ADDR - %d" % irtrim
            self.FOSC = int(base_freq)
        else:
            base_freq = 24000000
            while True:
                if base_freq * 1.0024 > val:
                    break
                irtrim += 1
                base_freq = base_freq * 1.0024
            self.IRTRIM.assignment = "T24M_ADDR + %d" % irtrim
            self.FOSC = int(base_freq)
