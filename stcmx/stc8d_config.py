from stcmx.stc8d_database import Stc8dDatabase
from stcmx.config_control import ConfigControl
from stcmx.util import InputHelper,SelectHelper


class Stc8dConfig(Stc8dDatabase, ConfigControl):

    def __init__(self):
        super().__init__()

        self.uart1: dict = {
            'enabled': False,
        }
        # __init__ end

    def define_clock(self):
        self.print({
            'en': "==== SYSTEM CLOCK CONFIG START ====",
            'cn': "==== 系统时钟配置开始 ====",
        })
        self.clock_source_select()
        self.set_fosc()
        self.frequency_adjust()
        # 设置分频系数
        v = self.CLKDIV_0.select(self.lang)
        self.SYSCLK = self.FOSC if v == 0 else int(self.FOSC / v)
        # 设置时钟输出
        v = self.MCLKOCRDIV.select(self.lang)
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

    def define_uart1(self):
        self.print({
            'en': "==== UART1 CONFIG START ====",
            'cn': "==== 串口1配置开始 ====",
        })
        self.uart1_config()
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
        self.T0CLKO.select(self.lang)
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
        self.timer1_config()
        self.print({
            'en': "==== TIMER1 CONFIG END ====",
            'cn': "==== 定时器1 配置结束 ====",
        })

    def define_timer2(self):
        self.print({
            'en': "==== TIMER2 CONFIG START ====",
            'cn': "==== 定时器2 配置开始 ====",
        })
        self.timer2_config()
        self.print({
            'en': "==== TIMER2 CONFIG END ====",
            'cn': "==== 定时器2 配置结束 ====",
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

    def timer1_config(self, uart_mode:bool=False, uart_rate_double:bool=False):
        """定时器1的完整配置"""
        if uart_mode:
            self.TR1.set_value(0B1)  # 开启定时器1
            mode_1t = self.T1x12.select(self.lang) == 0B1 # 1T/12T模式
            self.T1_CT.set_value(0B0)  # 工作方式timer
            self.T1_GATE.set_value(0B0) # 触发方式普通
            self.T1CLKO.set_value(0B0)  # 关闭输出
            while True:
                t1mode = self.T1_MODE.select(self.lang)
                if t1mode == 0B00 or t1mode == 0B10:
                    mode_2 = t1mode == 0B10
                    break
                else:
                    self.print({
                        'en': 'Only Mode0 and Mode2 are acceptable',
                        'cn': '用于串口波特率发生器, 只能选择模式0或模式2',
                    })

        else: # 正常模式, 直接配置定时器1
            self.TR1.select(self.lang)
            mode_1t = self.T1x12.select(self.lang) == 0B1
            self.T1_CT.select(self.lang)
            self.T1_GATE.select(self.lang)
            self.T1CLKO.select(self.lang)
            t1mode = self.T1_MODE.select(self.lang)

            if t1mode == 0B11:
                self.print({
                    'en': "Timer1 is in mode 3, skip",
                    'cn': "定时器1为模式3(停止状态), 跳过频率设置",
                })
                return

            mode_2 = t1mode == 0B10
        # 收集输入频率, 计算TH/TL
        self.timer1_period_config(mode_1t, mode_2, uart_mode, uart_rate_double)

    def timer0_period_config(self):
        """
        Set TH0 and TL0 according to input frequency.

        Mode0,1,3: Period = (12T Mode: 12 x)(65536 - [TH0,TL0])/SYSCLK
        Mode 2:    Period = (12T Mode: 12 x)(256 - [TH0])/SYSCLK
        """
        mode_1t = self.T0x12.get_value() == 0B1
        mode_2 = self.T0_MODE.get_value() == 0B10

        # Calculate possible frequency range in current configuration
        if mode_2: # Mode2
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 255)
        else: # Mode0,1,3
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 65535)
        val = lb

        while True:
            arg = self.input({
                'en': "Please input timer0 frequency, value between %d and %d:\n[%d]:" % (lb, hb, val),
                'cn': "请输入定时器0的频率, 取值于 [%d,  %d]区间内:\n[%d]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = int(arg)
            if lb <= val <= hb:
                if mode_2:  # Mode2
                    th = self.timer0and1_thl_calculate(mode_1t, mode_2, val)
                    if 0 < th < 256:
                        self.TH0.set_bits(int(th), 0xFF, 0)
                        self.TL0.set_bits(int(th), 0xFF, 0)
                        break
                else:  # Mode0,1,3
                    thl = self.timer0and1_thl_calculate(mode_1t, mode_2, val)
                    if 0 < thl < 65536:
                        self.TL0.set_bits(int(thl) & 0xFF, 0xFF, 0)
                        self.TH0.set_bits(int(thl) >> 8, 0xFF, 0)
                        break

    def timer0and1_thl_calculate(self, mode_1t:bool, mode_2:bool, freq, uart_mode:bool=False, uart_rate_double:bool=False):
        """根据定时器1的频率, 计算TH/TL"""
        if mode_2:
            if uart_mode:
                if uart_rate_double:
                    return int(256 - (self.SYSCLK * 2 / freq / 32)) if mode_1t else int(256 - (self.SYSCLK * 2 / freq / 32 / 12))
                else:
                    return int(256 - (self.SYSCLK / freq / 32)) if mode_1t else int(256 - (self.SYSCLK / freq / 32 / 12))
            else:
                return int(256 - (self.SYSCLK / freq)) if mode_1t else int(256 - (self.SYSCLK / freq / 12))
        else:
            if uart_mode:
                return int(65536 - (self.SYSCLK / freq / 4)) if mode_1t else int(65536 - (self.SYSCLK / freq / 4 / 12))
            else:
                return int(65536 - (self.SYSCLK / freq)) if mode_1t else int(65536 - (self.SYSCLK / freq / 12))

    def timer0and1_freq_calculate(self, mode_1t:bool, mode_2:bool, thl:int, uart_mode:bool=False, uart_rate_double:bool=False):
        """根据定时器1的 TH/TL 计算频率"""
        if mode_2:
            if uart_mode: # 计算波特率
                if uart_rate_double: # 模式2, 波特率翻倍
                    return int(self.SYSCLK / (256 - thl) / 32 * 2) if mode_1t else int(self.SYSCLK / (256 - thl) / 32 / 12 * 2)
                else:
                    return int(self.SYSCLK / (256 - thl) / 32) if mode_1t else int(self.SYSCLK / (256 - thl) / 32 / 12)
            else:
                return int(self.SYSCLK / (256 - thl)) if mode_1t else int(self.SYSCLK / (256 - thl) / 12)
        else:
            if uart_mode: # 计算波特率
                return int(self.SYSCLK / (65536 - thl) / 4) if mode_1t else int(self.SYSCLK / (65536 - thl) / 4 / 12)
            else:
                return int(self.SYSCLK / (65536 - thl)) if mode_1t else int(self.SYSCLK / (65536 - thl) / 12)

    def timer1_period_config(self, mode_1t:bool, mode_2:bool, uart_mode:bool=False, uart_rate_double:bool=False):
        """配置时钟1"""
        if mode_2: # Mode2
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0, uart_mode, uart_rate_double)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 255, uart_mode, uart_rate_double)

        else: # Mode0, Mode1
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0, uart_mode, uart_rate_double)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 65535, uart_mode, uart_rate_double)
        val = lb

        while True:
            arg = self.input({
                'en': "Please input timer1 frequency, value between %d and %d:\n[%d]:" % (lb, hb, val),
                'cn': "请输入频率, 取值于 [%d,  %d]区间内:\n[%d]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = int(arg)
            if lb <= val <= hb:
                if mode_2:
                    th = self.timer0and1_thl_calculate(mode_1t, mode_2, val, uart_mode, uart_rate_double)
                    if 0 < th < 256:
                        self.TH1.set_bits(th, 0xFF, 0)
                        self.TL1.set_bits(th, 0xFF, 0)
                        break
                else:
                    thl = self.timer0and1_thl_calculate(mode_1t, mode_2, val, uart_mode, uart_rate_double)
                    if 0 < thl < 65536:
                        self.TL1.set_bits(thl & 0xFF, 0xFF, 0)
                        self.TH1.set_bits(thl >> 8, 0xFF, 0)
                        break

    def timer2_config(self, uart_mode:bool=False):
        """定时器2的完整配置"""
        if uart_mode:
            self.T2R.set_value(0B1)  # 开启定时器2
            mode_1t = self.T2x12.select(self.lang) == 0B1 # 1T/12T模式
            self.T2_CT.set_value(0B0)  # 工作方式timer
            self.T2CLKO.set_value(0B0)  # 关闭输出
            tm2ps = 0 # 串口使用定时器2时, 不使用预分频

        else: # 普通模式, 直接配置定时器1
            self.T2R.select(self.lang)
            mode_1t = self.T2x12.select(self.lang) == 0B1
            self.T2_CT.select(self.lang)
            self.T2CLKO.select(self.lang)
            tm2ps = self.TM2PS_V.select(self.lang)

        # 收集输入频率, 计算TH/TL
        self.timer2_period_config(tm2ps, mode_1t, uart_mode)

    def timer2_period_config(self, tm2ps, mode_1t:bool, uart_mode:bool=False):
        tm2ps = tm2ps + 1 # SYSCLK / (TM2PS + 1)
        lb = self.timer2_freq_calculate(mode_1t, tm2ps, 0, uart_mode)
        hb = self.timer2_freq_calculate(mode_1t, tm2ps, 65535, uart_mode)
        val = lb

        while True:
            arg = self.input({
                'en': "Please input timer1 frequency, value between %.2f and %.2f:\n[%.2f]:" % (lb, hb, val),
                'cn': "请输入频率, 取值于 [%.2f,  %.2f]区间内:\n[%.2f]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = float(arg)
            if lb <= val <= hb:
                thl = self.timer2_thl_calculate(mode_1t, tm2ps, val, uart_mode)
                if 0 < thl < 65536:
                    self.T2L.set_bits(int(thl) & 0xFF, 0xFF, 0)
                    self.T2H.set_bits(int(thl) >> 8, 0xFF, 0)
                    break

    def timer2_freq_calculate(self, mode_1t:bool, tm2ps:int, thl:int, uart_mode:bool=False):
        """根据定时器2的TH/TL, 计算频率"""
        if uart_mode: # uart不使用TM2PS预分频
            return (self.SYSCLK / (65536 - thl) / 4) if mode_1t else (self.SYSCLK / (65536 - thl) / 4 / 12)
        else:
            return (self.SYSCLK / (65536 - thl) / tm2ps) if mode_1t else (self.SYSCLK / (65536 - thl) / tm2ps / 12)

    def timer2_thl_calculate(self, mode_1t:bool, tm2ps:int, freq, uart_mode:bool=False):
        """根据定时器2的频率, 计算TH/TL"""
        if uart_mode: # uart不使用TM2PS预分频
            return int(65536 - (self.SYSCLK / freq / 4)) if mode_1t else int(65536 - (self.SYSCLK / freq / 4 / 12))
        else:
            return int(65536 - (self.SYSCLK / freq / tm2ps)) if mode_1t else int(65536 - (self.SYSCLK / freq / tm2ps / 12))

    def uart1_config(self):
        # 选择串口1模式, 波特率与系统时钟关联, 固定
        mode = self.SCON_MODE.select(self.lang)
        # 模式0, 同步移位寄存器模式, 当UART_M0x6=0,波特率=SYSCLK/12, 当UART_M0x6=1时,波特率为SYSCLK/2
        if mode == 0B00:
            # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
            self.SCON.set_bit(0B0, 5)
            uart_m0x6 = self.UART_M0x6.select(self.lang)
            if uart_m0x6 == 0B0:
                self.uart1['baudRate'] = int(self.SYSCLK / 12)
            else:
                self.uart1['baudRate'] = int(self.SYSCLK)
            self.uart1['enabled'] = True

        # 模式1, 波特率与时钟1/时钟2关联
        elif mode == 0B01:
            # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
            self.SCON.set_bit(0B0, 5)
            # 串口1模式1/2/3的双倍波特率模式
            uart_rate_double = self.SMOD.select(self.lang) == 0B1
            # 串口1模式1/3可以配置波特率来源
            oscSource = self.S1ST2.select(self.lang)
            if oscSource == 0B0:  # 定时器1
                self.timer1_config(True, uart_rate_double)
            else:  # 定时器2
                self.timer2_config(True)

        # 模式2
        elif mode == 0B10:
            # 串口1模式1/2/3的双倍波特率模式
            doubleBaudRateMode = self.SMOD.select(self.lang)

        # 模式3
        else:
            # 串口1模式1/2/3的双倍波特率模式
            doubleBaudRateMode = self.SMOD.select(self.lang)
            # 串口1模式1/3波特率来源
            oscSource = self.S1ST2.select(self.lang)

        # 启用接收
        self.SCON_REN.select(self.lang)
        # 错误帧检测
        self.SMOD0.select(self.lang)
        self.uart1['enabled'] = True