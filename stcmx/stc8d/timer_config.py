from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8d_config import Stc8dConfig


class TimerConfig:

    def __init__(self, base: Stc8dConfig):
        self.base = base

    def info(self):
        mcu = self.base
        # timer0
        print(mcu.TR0.get_info(mcu.lang))
        print(mcu.T0x12.get_info(mcu.lang))
        print(mcu.T0_CT.get_info(mcu.lang))
        print(mcu.T0_GATE.get_info(mcu.lang))
        print(mcu.T0_MODE.get_info(mcu.lang))
        print(mcu.T0CLKO.get_info(mcu.lang))
        if mcu.T0_MODE.get_value() == 0B10:
            thl = mcu.TH0.val
        else:
            thl = mcu.TH0.val << 8 + mcu.TL0.val
        print("TIMER0 Freq: %d" % self.timer0and1_freq_calculate(
            mcu.T0x12.get_value() == 0B1,
            mcu.T0_MODE.get_value() == 0B10,
            thl
        ))

    def generate(self):
        mcu = self.base
        print("void timer_init()\n{")
        # internal RAM
        mcu.PCON.output_code(mcu.verbose, mcu.lang)
        mcu.AUXR.output_code(mcu.verbose, mcu.lang)
        mcu.TCON.output_code(mcu.verbose, mcu.lang)
        mcu.TMOD.output_code(mcu.verbose, mcu.lang)
        mcu.TH0.output_code(mcu.verbose, mcu.lang)
        mcu.TL0.output_code(mcu.verbose, mcu.lang)
        mcu.TH1.output_code(mcu.verbose, mcu.lang)
        mcu.TL1.output_code(mcu.verbose, mcu.lang)
        print("}")

    def timer0_config(self):
        mcu = self.base
        mcu.TR0.select(mcu.lang)
        mcu.T0x12.select(mcu.lang)
        mcu.T0_CT.select(mcu.lang)
        mcu.T0_GATE.select(mcu.lang)
        mcu.T0_MODE.select(mcu.lang)
        mcu.T0CLKO.select(mcu.lang)
        self.timer0_period_config()

    def timer0_period_config(self):
        """
        Set TH0 and TL0 according to input frequency.

        Mode0,1,3: Period = (12T Mode: 12 x)(65536 - [TH0,TL0])/SYSCLK
        Mode 2:    Period = (12T Mode: 12 x)(256 - [TH0])/SYSCLK
        """
        mcu = self.base
        mode_1t = mcu.T0x12.get_value() == 0B1
        mode_2 = mcu.T0_MODE.get_value() == 0B10

        # Calculate possible frequency range in current configuration
        if mode_2: # Mode2
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 255)
        else: # Mode0,1,3
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 65535)
        val = lb

        while True:
            arg = mcu.input({
                'en': "Please input timer0 frequency, value between %d and %d:\n[%d]:" % (lb, hb, val),
                'cn': "请输入定时器0的频率, 取值于 [%d,  %d]区间内:\n[%d]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = int(arg)
            if lb <= val <= hb:
                if mode_2:  # Mode2
                    th = self.timer0and1_thl_calculate(mode_1t, mode_2, val)
                    if 0 < th < 256:
                        mcu.TH0.set_bits(int(th), 0xFF, 0)
                        mcu.TL0.set_bits(int(th), 0xFF, 0)
                        break
                else:  # Mode0,1,3
                    thl = self.timer0and1_thl_calculate(mode_1t, mode_2, val)
                    if 0 < thl < 65536:
                        mcu.TL0.set_bits(int(thl) & 0xFF, 0xFF, 0)
                        mcu.TH0.set_bits(int(thl) >> 8, 0xFF, 0)
                        break

    def timer1_config(self, uart_mode: bool = False, uart_rate_double: bool = False):
        """定时器1的完整配置"""
        mcu = self.base
        if uart_mode:
            mcu.TR1.set_value(0B1)  # 开启定时器1
            mode_1t = mcu.T1x12.select(mcu.lang) == 0B1 # 1T/12T模式
            mcu.T1_CT.set_value(0B0)  # 工作方式timer
            mcu.T1_GATE.set_value(0B0) # 触发方式普通
            mcu.T1CLKO.set_value(0B0)  # 关闭输出
            while True:
                t1mode = mcu.T1_MODE.select(mcu.lang)
                if t1mode == 0B00 or t1mode == 0B10:
                    mode_2 = t1mode == 0B10
                    break
                else:
                    mcu.print({
                        'en': 'Only Mode0 and Mode2 are acceptable',
                        'cn': '用于串口波特率发生器, 只能选择模式0或模式2',
                    })

        else: # 正常模式, 直接配置定时器1
            mcu.TR1.select(mcu.lang)
            mode_1t = mcu.T1x12.select(mcu.lang) == 0B1
            mcu.T1_CT.select(mcu.lang)
            mcu.T1_GATE.select(mcu.lang)
            mcu.T1CLKO.select(mcu.lang)
            t1mode = mcu.T1_MODE.select(mcu.lang)

            if t1mode == 0B11:
                mcu.print({
                    'en': "Timer1 is in mode 3, skip",
                    'cn': "定时器1为模式3(停止状态), 跳过频率设置",
                })
                return

            mode_2 = t1mode == 0B10
        # 收集输入频率, 计算TH/TL
        self.timer1_period_config(mode_1t, mode_2, uart_mode, uart_rate_double)

    def timer0and1_thl_calculate(self, mode_1t:bool, mode_2:bool, freq, uart_mode:bool=False, uart_rate_double:bool=False):
        """根据定时器1的频率, 计算TH/TL"""
        mcu = self.base
        if mode_2:
            if uart_mode:
                if uart_rate_double:
                    return int(256 - (mcu.SYSCLK * 2 / freq / 32)) if mode_1t else int(256 - (mcu.SYSCLK * 2 / freq / 32 / 12))
                else:
                    return int(256 - (mcu.SYSCLK / freq / 32)) if mode_1t else int(256 - (mcu.SYSCLK / freq / 32 / 12))
            else:
                return int(256 - (mcu.SYSCLK / freq)) if mode_1t else int(256 - (mcu.SYSCLK / freq / 12))
        else:
            if uart_mode:
                return int(65536 - (mcu.SYSCLK / freq / 4)) if mode_1t else int(65536 - (mcu.SYSCLK / freq / 4 / 12))
            else:
                return int(65536 - (mcu.SYSCLK / freq)) if mode_1t else int(65536 - (mcu.SYSCLK / freq / 12))

    def timer0and1_freq_calculate(self, mode_1t:bool, mode_2:bool, thl:int, uart_mode:bool=False, uart_rate_double:bool=False):
        """根据定时器1的 TH/TL 计算频率"""
        mcu = self.base
        if mode_2:
            if uart_mode: # 计算波特率
                if uart_rate_double: # 模式2, 波特率翻倍
                    return int(mcu.SYSCLK / (256 - thl) / 32 * 2) if mode_1t else int(mcu.SYSCLK / (256 - thl) / 32 / 12 * 2)
                else:
                    return int(mcu.SYSCLK / (256 - thl) / 32) if mode_1t else int(mcu.SYSCLK / (256 - thl) / 32 / 12)
            else:
                return int(mcu.SYSCLK / (256 - thl)) if mode_1t else int(mcu.SYSCLK / (256 - thl) / 12)
        else:
            if uart_mode: # 计算波特率
                return int(mcu.SYSCLK / (65536 - thl) / 4) if mode_1t else int(mcu.SYSCLK / (65536 - thl) / 4 / 12)
            else:
                return int(mcu.SYSCLK / (65536 - thl)) if mode_1t else int(mcu.SYSCLK / (65536 - thl) / 12)

    def timer1_period_config(self, mode_1t:bool, mode_2:bool, uart_mode:bool=False, uart_rate_double:bool=False):
        """配置时钟1"""
        mcu = self.base
        if mode_2: # Mode2
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0, uart_mode, uart_rate_double)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 255, uart_mode, uart_rate_double)

        else: # Mode0, Mode1
            lb = self.timer0and1_freq_calculate(mode_1t, mode_2, 0, uart_mode, uart_rate_double)
            hb = self.timer0and1_freq_calculate(mode_1t, mode_2, 65535, uart_mode, uart_rate_double)
        val = lb

        while True:
            arg = mcu.input({
                'en': "Please input timer1 frequency, value between %d and %d:\n[%d]:" % (lb, hb, val),
                'cn': "请输入频率, 取值于 [%d,  %d]区间内:\n[%d]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = int(arg)
            if lb <= val <= hb:
                if mode_2:
                    th = self.timer0and1_thl_calculate(mode_1t, mode_2, val, uart_mode, uart_rate_double)
                    if 0 < th < 256:
                        mcu.TH1.set_bits(th, 0xFF, 0)
                        mcu.TL1.set_bits(th, 0xFF, 0)
                        break
                else:
                    thl = self.timer0and1_thl_calculate(mode_1t, mode_2, val, uart_mode, uart_rate_double)
                    if 0 < thl < 65536:
                        mcu.TL1.set_bits(thl & 0xFF, 0xFF, 0)
                        mcu.TH1.set_bits(thl >> 8, 0xFF, 0)
                        break

    def timer2_config(self, uart_mode:bool=False):
        """定时器2的完整配置"""
        mcu = self.base
        if uart_mode:
            mcu.T2R.set_value(0B1)  # 开启定时器2
            mode_1t = mcu.T2x12.select(mcu.lang) == 0B1 # 1T/12T模式
            mcu.T2_CT.set_value(0B0)  # 工作方式timer
            mcu.T2CLKO.set_value(0B0)  # 关闭输出
            tm2ps = 0 # 串口使用定时器2时, 不使用预分频

        else: # 普通模式, 直接配置定时器1
            mcu.T2R.select(mcu.lang)
            mode_1t = mcu.T2x12.select(mcu.lang) == 0B1
            mcu.T2_CT.select(mcu.lang)
            mcu.T2CLKO.select(mcu.lang)
            tm2ps = mcu.TM2PS_V.select(mcu.lang)

        # 收集输入频率, 计算TH/TL
        self.timer2_period_config(tm2ps, mode_1t, uart_mode)

    def timer2_period_config(self, tm2ps, mode_1t: bool, uart_mode: bool = False):
        mcu = self.base
        tm2ps = tm2ps + 1 # SYSCLK / (TM2PS + 1)
        lb = self.timer2_freq_calculate(mode_1t, tm2ps, 0, uart_mode)
        hb = self.timer2_freq_calculate(mode_1t, tm2ps, 65535, uart_mode)
        val = lb

        while True:
            arg = mcu.input({
                'en': "Please input timer1 frequency, value between %.2f and %.2f:\n[%.2f]:" % (lb, hb, val),
                'cn': "请输入频率, 取值于 [%.2f,  %.2f]区间内:\n[%.2f]:" % (lb, hb, val),
            })
            if len(arg) > 0:
                val = float(arg)
            if lb <= val <= hb:
                thl = self.timer2_thl_calculate(mode_1t, tm2ps, val, uart_mode)
                if 0 < thl < 65536:
                    mcu.T2L.set_bits(int(thl) & 0xFF, 0xFF, 0)
                    mcu.T2H.set_bits(int(thl) >> 8, 0xFF, 0)
                    break

    def timer2_freq_calculate(self, mode_1t: bool, tm2ps: int, thl: int, uart_mode: bool = False):
        """根据定时器2的TH/TL, 计算频率"""
        mcu = self.base
        if uart_mode: # uart不使用TM2PS预分频
            return (mcu.SYSCLK / (65536 - thl) / 4) if mode_1t else (mcu.SYSCLK / (65536 - thl) / 4 / 12)
        else:
            return (mcu.SYSCLK / (65536 - thl) / tm2ps) if mode_1t else (mcu.SYSCLK / (65536 - thl) / tm2ps / 12)

    def timer2_thl_calculate(self, mode_1t: bool, tm2ps: int, freq, uart_mode: bool = False):
        """根据定时器2的频率, 计算TH/TL"""
        mcu = self.base
        if uart_mode: # uart不使用TM2PS预分频
            return int(65536 - (mcu.SYSCLK / freq / 4)) if mode_1t else int(65536 - (mcu.SYSCLK / freq / 4 / 12))
        else:
            return int(65536 - (mcu.SYSCLK / freq / tm2ps)) if mode_1t else int(65536 - (mcu.SYSCLK / freq / tm2ps / 12))
