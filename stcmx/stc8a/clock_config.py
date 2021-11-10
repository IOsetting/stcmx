# make all type hints be strings and skip evaluating them
from __future__ import annotations
# The TYPE_CHECKING constant is always False at runtime, so the import won't be evaluated, but type-checking tools will
from typing import TYPE_CHECKING
import stcmx.util as util
from stcmx.util import InputHelper


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class ClockConfig:

    def __init__(self, base:Stc8aConfig):
        self.base = base

    def config(self):
        mcu = self.base
        value = mcu.MCKSEL.select(mcu.lang)
        if value == 0B00:  # 使用内部24MHz RC
            mcu.ENIRC24M.set_value(0B1)
            mcu.ENXOSC.set_value(0B0)
            mcu.ENIRC32K.set_value(0B0)
            mcu.MX_CLOCK.select(mcu.lang)
            mcu.IRTRIM.assignment = mcu.MX_CLOCK.get_value()[0]
            mcu.MX_FOSC.set_value(mcu.MX_CLOCK.get_value()[1])

        elif value == 0B01: # 使用外部时钟输入
            mcu.ENIRC24M.set_value(0B0)
            mcu.ENXOSC.set_value(0B1)
            mcu.ENIRC32K.set_value(0B0)
            mcu.XITYPE.select(mcu.lang)
            mcu.IRTRIM.reset()

        elif value == 0B11: # 使用内部32K IRC
            # 使用内部32K RC
            mcu.ENIRC24M.set_value(0B0)
            mcu.ENXOSC.set_value(0B0)
            mcu.ENIRC32K.set_value(0B1)
            mcu.MX_FOSC.set_value(32768)
            mcu.IRTRIM.reset()

        # 设置分频系数
        v = mcu.CLKDIV_0.select(mcu.lang)
        mcu.FOSC = self.get_fosc()
        mcu.SYSCLK = mcu.FOSC if v == 0 else int(mcu.FOSC / v)
        # 设置时钟输出
        v = mcu.MCLKODIV.select(mcu.lang)
        if v != 0x00:
            # 时钟输出脚选择
            mcu.MCLKO_S.select(mcu.lang)

    def info(self):
        mcu = self.base
        print(mcu.MCKSEL.get_info(mcu.lang))
        print(mcu.ENIRC24M.get_info(mcu.lang))
        print(mcu.ENXOSC.get_info(mcu.lang))
        print(mcu.ENIRC32K.get_info(mcu.lang))
        if mcu.MCKSEL.get_value() == 0B00:
            print(mcu.MX_CLOCK.get_info(mcu.lang))
            print(mcu.MX_FOSC.get_info(mcu.lang))
            print(mcu.IRTRIM_S.get_info(mcu.lang))
            print(mcu.LIRTRIM_0.get_info(mcu.lang))
        elif mcu.MCKSEL.get_value() == 0B01:
            print(mcu.XITYPE.get_info(mcu.lang))
            print(mcu.MX_FOSC.get_info(mcu.lang))
        elif mcu.MCKSEL.get_value() == 0B11:
            print(mcu.MX_FOSC.get_info(mcu.lang))

        print(mcu.CLKDIV_0.get_info(mcu.lang))
        mcu.FOSC = self.get_fosc()
        v = mcu.CLKDIV_0.get_value()
        mcu.SYSCLK = mcu.FOSC if v == 0 else int(mcu.FOSC / v)
        print("FOSC: %s" % util.format_frequency(mcu.FOSC))
        print("SYSCLK: %s" % util.format_frequency(mcu.SYSCLK))

        print(mcu.MCLKODIV.get_info(mcu.lang))
        if mcu.MCLKODIV.get_value() != 0x00:
            print(mcu.MCLKO_S.get_info(mcu.lang))
            sysclk_output = int(mcu.SYSCLK / mcu.MCLKODIV.get_value())
            print("Output clock: %s" % util.format_frequency(sysclk_output))

    def get_fosc(self):
        mcu = self.base
        if mcu.MCKSEL.get_value() == 0B00:
            base_fosc = mcu.MX_CLOCK.get_value()[1]
            if mcu.LIRTRIM_0.get_value() == 0B00:
                fosc = base_fosc
            elif mcu.LIRTRIM_0.get_value() == 0B01:
                fosc = base_fosc * (1 + 0.0001)
            elif mcu.LIRTRIM_0.get_value() == 0B10:
                fosc = base_fosc * (1 + 0.0004)
            else:
                fosc = base_fosc * (1 + 0.001)

        elif mcu.MCKSEL.get_value() == 0B01 or mcu.MCKSEL.get_value() == 0B11:
            fosc = mcu.MX_FOSC.get_value()
        else:
            fosc = 0 # This should not happen
        return fosc

    def get_sysclk(self):
        mcu = self.base
        v = mcu.CLKDIV_0.get_value()
        fosc = self.get_fosc()
        return fosc if v == 0 else int(fosc / v)

    def generate(self):
        mcu = self.base
        print("void clock_init()\n{")
        # extend ROM
        mcu.P_SW2.set_bits(0B1, 0B1, 7)
        mcu.P_SW2.output_code(mcu.verbose, mcu.lang, force=True)
        mcu.CKSEL.output_code(mcu.verbose, mcu.lang)
        mcu.IRC24MCR.output_code(mcu.verbose, mcu.lang)
        mcu.XOSCCR.output_code(mcu.verbose, mcu.lang)
        mcu.IRC32KCR.output_code(mcu.verbose, mcu.lang)
        mcu.CLKDIV.output_code(mcu.verbose, mcu.lang, force=True)
        mcu.IRTRIM.output_code(mcu.verbose, mcu.lang)
        mcu.LIRTRIM.output_code(mcu.verbose, mcu.lang, force=True)
        mcu.P_SW2.reset()
        mcu.P_SW2.output_code(mcu.verbose, mcu.lang, force=True)
        print('')
        # internal RAM
        print("}")
