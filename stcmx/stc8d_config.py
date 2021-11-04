from stcmx.stc8d_database import Stc8dDatabase
from stcmx.config_control import ConfigControl
from stcmx.sfrbits_model import SFRBitsModel
from stcmx.util import InputHelper,SelectHelper


class Stc8dConfig(Stc8dDatabase, ConfigControl):

    def __init__(self):
        super().__init__()
        # SFR Bits
        self.MCLKOCRDIV = SFRBitsModel(
            self.MCLKOCR, 'MCLKOCRDIV', 0,
            {
                'en': "Please input the out clock division, value in range [0, 127]\n" +
                      "  0:No output,\n" +
                      "  1~127: output = SYSCLK/division\n[%s]:",
                'cn': "请输入时钟输出的分频系数, 取值范围[0, 127]\n" +
                      "  0:无输出,\n" +
                      "  1~127: 输出频率 = SYSCLK/分频系数\n[%s]:",
            },
            len=7,
        )

        self.MCLKO_S = SFRBitsModel(
            self.MCLKOCR, 'MCLKO_S', 7,
            {
                'en': "Please select the clock output pin:\n  0:P5.4, 1:P1.6\n[%s]:",
                'cn': "请选择时钟输出PIN脚:\n  0:P5.4, 1:P1.6\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.TR0 = SFRBitsModel(
            self.TCON, 'TR0', 4,
            {
                'en': "Please select Timer0 running mode: 0:Stop, 1:Run\n[%s]:",
                'cn': "是否运行Timer0? 0:停止, 1:运行\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
            sbit=True
        )

        self.TR1 = SFRBitsModel(
            self.TCON, 'TR1', 6,
            {
                'en': "Please select Timer1 running mode: 0:Stop, 1:Run\n[%s]:",
                'cn': "是否运行Timer1? 0:停止, 1:运行\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
            sbit=True
        )

        self.T0x12 = SFRBitsModel(
            self.AUXR, 'T0x12', 7,
            {
                'en': "Please select Timer0 clock speed: 0:12T Mode, 1:1T Mode\n[%s]:",
                'cn': "请设置定时器0速度(周期模式): 0:12T模式, 1:1T模式\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.T1x12 = SFRBitsModel(
            self.AUXR, 'T1x12', 6,
            {
                'en': "Please select Timer1 clock speed: 0:12T Mode, 1:1T Mode\n[%s]:",
                'cn': "请设置定时器1速度(周期模式): 0:12T模式, 1:1T模式\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.T0_CT = SFRBitsModel(
            self.TMOD, 'T0_CT', 2,
            {
                'en': "Please select Timer0 function: 0:Timer, 1:Counter\n[%s]:",
                'cn': "请选择定时器0功能: 0:定时器, 1:计数器\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.T1_CT = SFRBitsModel(
            self.TMOD, 'T1_CT', 6,
            {
                'en': "Please select Timer1 function: 0:Timer, 1:Counter\n[%s]:",
                'cn': "请选择定时器1功能: 0:定时器, 1:计数器\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.T0_GATE = SFRBitsModel(
            self.TMOD, 'T0_GATE', 3,
            {
                'en': "Please select Timer0 work mode: 0:Normal, 1:Work only when INT0 and RT0 are high\n[%s]:",
                'cn': "设置定时器0打开条件: 0:正常, 1:只有在INT0脚为高及TR0控制位置1时才可打开定时器/计数器0\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.T1_GATE = SFRBitsModel(
            self.TMOD, 'T1_GATE', 7,
            {
                'en': "Please select Timer1 work mode: 0:Normal, 1:Work only when INT1 and RT1 are high\n[%s]:",
                'cn': "设置定时器1打开条件: 0:正常, 1:只有在INT1脚为高及TR1控制位置1时才可打开定时器/计数器1\n[%s]:",
            },
            options={'0': 0B0, '1': 0B1},
        )

        self.T0_MODE = SFRBitsModel(
            self.TMOD, 'T0_MODE', 0,
            {
                'en': "Please select Timer0 timer mode:\n" +
                      "  0:16bit auto-reload, [TH0,TL0] will auto-reload when overflow\n" +
                      "  1:16bit no-auto-reload, [TH0,TL0] will start from 0 when overflow\n" +
                      "  2:8bit auto-reload, TL0 will auto-reload from TH0 when overflow\n" +
                      "  3:Non-interruptable 16bit auto-reload, highest priority\n[%s]:",
                'cn': "请选择定时器0的定时器模式\n" +
                      "  0:16位自动重载模式, 当[TH0,TL0]中的16位计数值溢出时，系统会自动将内部16位重载寄存器中的重载值装入[TH0,TL0]中\n" +
                      "  1:16位不自动重载模式, 当[TH0,TL0]中的16位计数值溢出时，定时器1将从0开始计数\n" +
                      "  2:8位自动重载模式, 当TL0中的8位计数值溢出时，系统会自动将TH0中的重载值装入TL0中\n" +
                      "  3:不可屏蔽中断的16位自动重载模式, 与模式0相同，不可屏蔽, 中断优先级最高且不可关闭, 可用作操作系统的系统节拍定时器或系统监控定时器\n[%s]:",
            },
            len=2,
            options={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
        )

        self.T1_MODE = SFRBitsModel(
            self.TMOD, 'T1_MODE', 4,
            {
                'en': "Please select Timer1 timer mode:\n" +
                      "  0:16bit auto-reload, [TH1,TL1] will auto-reload when overflow\n" +
                      "  1:16bit no-auto-reload, [TH1,TL1] will start from 0 when overflow\n" +
                      "  2:8bit auto-reload, TL1 will auto-reload from TH1 when overflow\n" +
                      "  3:Timer1 stop\n[%s]:",
                'cn': "请选择定时器1的定时器模式\n" +
                      "  0:16位自动重载模式, 当[TH1,TL1]中的16位计数值溢出时，系统会自动将内部16位重载寄存器中的重载值装入[TH1,TL1]中\n" +
                      "  1:16位不自动重载模式, 当[TH1,TL1]中的16位计数值溢出时，定时器1将从0开始计数\n" +
                      "  2:8位自动重载模式, 当TL1中的8位计数值溢出时，系统会自动将TH1中的重载值装入TL1中\n" +
                      "  3:T1停止工作\n[%s]:",
            },
            len=2,
            options={'0': 0B00, '1': 0B01, '2': 0B10, '3': 0B11},
        )

        # __init__ end

    def define_clock(self):
        self.print({
            'en': "==== SYSTEM CLOCK CONFIG START ====",
            'cn': "==== 系统时钟配置开始 ====",
        })
        self.clock_source_select()
        self.set_fosc()
        self.frequency_adjust()
        self.set_sysclock_division()
        self.MCLKOCRDIV.select(self.lang)
        self.clock_output_pin_select()
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

    def define_timer0(self):
        self.print({
            'en': "==== TIMER0 CONFIG START ====",
            'cn': "==== 定时器0 配置开始 ====",
        })
        self.TR0.select(self.lang)
        self.T0x12.select(self.lang)
        self.T0_CT.select(self.lang)
        self.T0_GATE.select(self.lang)
        self.T0_MODE.select(self.lang)
        self.timer0_period_config()
        self.print({
            'en': "==== TIMER0 CONFIG END ====",
            'cn': "==== 定时器0 配置结束 ====",
        })

    def define_timer1(self):
        self.print({
            'en': "==== TIMER1 CONFIG START ====",
            'cn': "==== 定时器1 配置开始 ====",
        })
        self.TR1.select(self.lang)
        self.T1x12.select(self.lang)
        self.T1_CT.select(self.lang)
        self.T1_GATE.select(self.lang)
        self.T1_MODE.select(self.lang)
        self.timer1_period_config()
        self.print({
            'en': "==== TIMER1 CONFIG START ====",
            'cn': "==== 定时器1 配置结束 ====",
        })

    """
    ============================================================
    """

    def clock_source_select(self):
        """Select the clock source"""
        value = self.MCKSEL.select(self.lang)
        if value == 0B00:
            self.XOSCCR.reset()
            self.IRC32KCR.reset()
        elif value == 0B01:
            self.HIRCCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B1, 0B1, 7)
            self.XOSCCR.set_bits(0B1, 0B1, 6)
            self.IRC32KCR.reset()
        elif value == 0B10:
            self.HIRCCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.set_bits(0B1, 0B1, 7)
            self.IRC32KCR.reset()
        elif value == 0B11:
            self.HIRCCR.set_bits(0B0, 0B1, 7)
            self.XOSCCR.reset()
            self.IRC32KCR.set_bits(0B1, 0B1, 7)

    def set_fosc(self):
        """Set IRCBAND and IRTRIM according to specified frequency"""
        if self.CKSEL.val == 0B01 or self.CKSEL.val == 0B10:
            opt = InputHelper(
                {
                    'en': "Please input the external OSC/CLK frequency, value in range [4500000, 53400000]\n[%d]:",
                    'cn': "请输入外部振荡源或时钟频率, 值必须在[4500000, 53400000]区间内\n[%d]:",
                },
                valid=lambda a: (int(a) >= 4000000 and int(a) <= 53000000),
            )
            val = int(opt.input(self.lang))
            self.FOSC = val
            self.IRCBAND.reset()
            self.IRTRIM.reset()
            return
        elif self.CKSEL.val == 0B11:
            self.FOSC = 32768
            self.IRCBAND.reset()
            self.IRTRIM.reset()
            return

        frequencies:dict = {
            '0': 20000000,
            '1': 22118400,
            '2': 24000000,
            '3': 27000000,
            '4': 30000000,
            '5': 33177600,
            '6': 25000000,
            '7': 36864000,
            '8': 40000000,
            '9': 45000000,
        }
        opt = SelectHelper(
            {
                '0': 'T20M_ADDR',
                '1': 'T22M_ADDR',
                '2': 'T24M_ADDR',
                '3': 'T27M_ADDR',
                '4': 'T30M_ADDR',
                '5': 'T33M_ADDR',
                '6': 'T35M_ADDR',
                '7': 'T36M_ADDR',
                '8': 'T40M_ADDR',
                '9': 'T45M_ADDR'
            },
            {
                'en': "Please select frequency\n" +
                      "  0: 20MHz\n" +
                      "  1: 22.1184MHz\n" +
                      "  2: 24MHz\n" +
                      "  3: 27MHz\n" +
                      "  4: 30MHz\n" +
                      "  5: 33.1776MHz\n" +
                      "  6: 35MHz\n" +
                      "  7: 36.864MHz\n" +
                      "  8: 40MHz\n" +
                      "  9: 45MHz\n[%s]:",
                'cn': "请选择频率\n" +
                      "  0: 20MHz\n" +
                      "  1: 22.1184MHz\n" +
                      "  2: 24MHz\n" +
                      "  3: 27MHz\n" +
                      "  4: 30MHz\n" +
                      "  5: 33.1776MHz\n" +
                      "  6: 35MHz\n" +
                      "  7: 36.864MHz\n" +
                      "  8: 40MHz\n" +
                      "  9: 45MHz\n[%s]:",
            },
            '0',
            prompt_once={
                'en': 'Internal OSC frequency options: 6M Band[4.5MHz～8MHz], 10M Band[7.5MHz～13.5MHz], 27M Band[20.5MHz, 36MHz]，44M Band[29MHz～55MHz]',
                'cn': '内部振荡源频段: 6M频段[4.5MHz～8MHz], 10M频段[7.5MHz～13.5MHz], 27M频段[20.5MHz, 36MHz]，44M频段[29MHz～55MHz]'
            },
        )
        self.IRTRIM.assignment = opt.select(self.lang)
        self.FOSC = frequencies[opt.selection]
        # set internal OSC band
        if opt.selection in ['0','1','2','3','4','5']:
            # use 27MHz band
            self.IRCBAND.set_bits(0B10, 0B11, 0)
            self.VRTRIM.assignment = 'VRT27M_ADDR'
        elif opt.selection in ['6','7','8','9']:
            # use 44MHz band
            self.IRCBAND.set_bits(0B11, 0B11, 0)
            self.VRTRIM.assignment = 'VRT44M_ADDR'

    def clock_output_pin_select(self):
        if self.MCLKOCRDIV.get_value() == 0x00:
            self.print({
                'en': "No clock output, skip output pin selection",
                'cn': "未设置时钟输出, 跳过输出PIN脚选择",
            })
            return
        self.MCLKO_S.select(self.lang)

    def timer0_period_config(self):
        """
        Set TH0 and TL0 according to input frequency.

        Mode0,1,3: Period = (12T Mode: 12 x)(65536 - [TH0,TL0])/SYSCLK
        Mode 2:    Period = (12T Mode: 12 x)(256 - [TH0])/SYSCLK
        """
        # Calculate possible frequency range in current configuration
        if self.T0_MODE.get_value() == 0B10: # Mode2
            if self.T0x12.get_value() == 0B0: # 12T
                lb = int(self.SYSCLK/256/12)
                hb = int(self.SYSCLK/12)
            else: # 1T
                lb = int(self.SYSCLK / 256)
                hb = int(self.SYSCLK)
        else: # Mode0,1,3
            if self.T0x12.get_value() == 0B0:  # 12T
                lb = int(self.SYSCLK / 65536 / 12)
                hb = int(self.SYSCLK / 12)
            else:  # 1T
                lb = int(self.SYSCLK / 65536)
                hb = int(self.SYSCLK)
        val = lb

        while True:
            arg = self.input({
                'en': "Please input timer0 frequency, value between %d and %d:\n[%d]:" % (lb, hb, val),
                'cn': "请输入定时器0的频率, 取值于 [%d,  %d]区间内:\n[%d]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = int(arg)
            if lb <= val <= hb:
                if self.T0_MODE.get_value() == 0B10:  # Mode2
                    if self.T0x12.get_value() == 0B0:  # 12T
                        th = 256 - (self.SYSCLK / (val * 12))
                        if 0 < th < 256:
                            self.TH0.set_bits(int(th), 0xFF, 0)
                            self.TL0.set_bits(int(th), 0xFF, 0)
                            break
                    else:  # 1T
                        th = 256 - (self.SYSCLK / val)
                        if 0 < th < 256:
                            self.TH0.set_bits(int(th), 0xFF, 0)
                            self.TL0.set_bits(int(th), 0xFF, 0)
                            break
                else:  # Mode0,1,3
                    if self.T0x12.get_value() == 0B0:  # 12T
                        thl = 65536 - (self.SYSCLK / (val * 12))
                        if 0 < thl < 65536:
                            self.TL0.set_bits(int(thl) & 0xFF, 0xFF, 0)
                            self.TH0.set_bits(int(thl) >> 8, 0xFF, 0)
                            break
                    else:  # 1T
                        thl = 65536 - (self.SYSCLK / val)
                        if 0 < thl < 65536:
                            self.TL0.set_bits(int(thl) & 0xFF, 0xFF, 0)
                            self.TH0.set_bits(int(thl) >> 8, 0xFF, 0)
                            break

    def timer1_period_config(self):
        if self.T1_MODE.get_value() == 0B11:
            self.print({
                'en': "Timer1 is stopped, skip",
                'cn': "定时器1为停止状态, 跳过频率设置",
            })
            return
        elif self.T1_MODE.get_value() == 0B10: # Mode2
            if self.T1x12.get_value() == 0B0: # 12T
                lb = int(self.SYSCLK/256/12)
                hb = int(self.SYSCLK/12)
            else: # 1T
                lb = int(self.SYSCLK / 256)
                hb = int(self.SYSCLK)
        else: # Mode0, Mode1
            if self.T1x12.get_value() == 0B0:  # 12T
                lb = int(self.SYSCLK / 65536 / 12)
                hb = int(self.SYSCLK / 12)
            else:  # 1T
                lb = int(self.SYSCLK / 65536)
                hb = int(self.SYSCLK)
        val = lb

        while True:
            arg = self.input({
                'en': "Please input timer1 frequency, value between %d and %d:\n[%d]:" % (lb, hb, val),
                'cn': "请输入定时器1的频率, 取值于 [%d,  %d]区间内:\n[%d]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = int(arg)
            if lb <= val <= hb:
                if self.T1_MODE.get_value() == 0B10:  # Mode2
                    if self.T1x12.get_value() == 0B0:  # 12T
                        th = 256 - (self.SYSCLK / (val * 12))
                        if 0 < th < 256:
                            self.TH1.set_bits(int(th), 0xFF, 0)
                            self.TL1.set_bits(int(th), 0xFF, 0)
                            break
                    else:  # 1T
                        th = 256 - (self.SYSCLK / val)
                        if 0 < th < 256:
                            self.TH1.set_bits(int(th), 0xFF, 0)
                            self.TL1.set_bits(int(th), 0xFF, 0)
                            break
                else:  # Mode0, Mode1
                    if self.T1x12.get_value() == 0B0:  # 12T
                        thl = 65536 - (self.SYSCLK / (val * 12))
                        if 0 < thl < 65536:
                            self.TL1.set_bits(int(thl) & 0xFF, 0xFF, 0)
                            self.TH1.set_bits(int(thl) >> 8, 0xFF, 0)
                            break
                    else:  # 1T
                        thl = 65536 - (self.SYSCLK / val)
                        if 0 < thl < 65536:
                            self.TL1.set_bits(int(thl) & 0xFF, 0xFF, 0)
                            self.TH1.set_bits(int(thl) >> 8, 0xFF, 0)
                            break
