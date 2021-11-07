# make all type hints be strings and skip evaluating them
from __future__ import annotations
# The TYPE_CHECKING constant is always False at runtime, so the import won't be evaluated, but type-checking tools will
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8d_config import Stc8dConfig


class ClockConfig:

    def __init__(self, base:Stc8dConfig):
        self.base = base

    def config(self):
        mcu = self.base
        value = mcu.MCKSEL.select(mcu.lang)
        if value == 0B00:  # 使用内部RC
            mcu.XOSCCR.reset()
            mcu.IRC32KCR.reset()
            mcu.MX_CLOCK.select(mcu.lang)
            mcu.IRTRIM.assignment = mcu.MX_CLOCK.get_value()[0]
            mcu.MX_FOSC.set_value(mcu.MX_CLOCK.get_value()[1])
            # set internal OSC band
            if mcu.MX_CLOCK.get_selection() in ['0', '1', '2', '3', '4', '5']:
                # use 27MHz band
                mcu.IRCBAND.set_bits(0B10, 0B11, 0)
                mcu.VRTRIM.assignment = 'VRT27M_ADDR'
            else:
                # use 44MHz band
                mcu.IRCBAND.set_bits(0B11, 0B11, 0)
                mcu.VRTRIM.assignment = 'VRT44M_ADDR'

            value = mcu.LIRTRIM_0.select(mcu.lang)
            if value == 0B01:
                mcu.FOSC = int(mcu.MX_FOSC.get_value() * 1.0001)
            elif value == 0B10:
                mcu.FOSC = int(mcu.MX_FOSC.get_value() * 1.0004)
            elif value == 0B11:
                mcu.FOSC = int(mcu.MX_FOSC.get_value() * 1.001)

        elif value == 0B01:
            mcu.HIRCCR.set_bits(0B0, 0B1, 7)
            mcu.XOSCCR.set_bits(0B1, 0B1, 7)
            mcu.XOSCCR.set_bits(0B1, 0B1, 6)
            mcu.IRC32KCR.reset()
            v = mcu.MX_FOSC.input(mcu.lang)
            mcu.FOSC = v
            mcu.IRCBAND.reset()
            mcu.IRTRIM.reset()

        elif value == 0B10:
            mcu.HIRCCR.set_bits(0B0, 0B1, 7)
            mcu.XOSCCR.set_bits(0B1, 0B1, 7)
            mcu.IRC32KCR.reset()
            v = mcu.MX_FOSC.input(mcu.lang)
            mcu.FOSC = v
            mcu.IRCBAND.reset()
            mcu.IRTRIM.reset()

        elif value == 0B11:  # 使用内部32K RC
            mcu.HIRCCR.set_bits(0B0, 0B1, 7)
            mcu.XOSCCR.reset()
            mcu.IRC32KCR.set_bits(0B1, 0B1, 7)
            mcu.MX_FOSC.set_value(32768)
            mcu.IRCBAND.reset()
            mcu.IRTRIM.reset()

        # 设置分频系数
        v = mcu.CLKDIV_0.select(mcu.lang)
        mcu.SYSCLK = mcu.MX_FOSC.get_value() if v == 0 else int(mcu.MX_FOSC.get_value() / v)
        # 设置时钟输出
        v = mcu.MCLKOCRDIV.select(mcu.lang)
        if v != 0x00:
            # 时钟输出脚选择
            mcu.MCLKO_S.select(mcu.lang)

    def info(self):
        mcu = self.base
        print(mcu.MCKSEL.get_info(mcu.lang))
        if mcu.MCKSEL.get_value() == 0B00:
            print(mcu.MX_CLOCK.get_info(mcu.lang))
            print(mcu.MX_FOSC.get_info(mcu.lang))
            print(mcu.LIRTRIM_0.get_info(mcu.lang))
            # calculate fosc and sysclk
            base_fosc = mcu.MX_CLOCK.get_value()[1]
            if mcu.LIRTRIM_0.get_value() == 0B00:
                fosc = base_fosc
            elif mcu.LIRTRIM_0.get_value() == 0B01:
                fosc = base_fosc * (1 + 0.0001)
            elif mcu.LIRTRIM_0.get_value() == 0B10:
                fosc = base_fosc * (1 + 0.0004)
            else:
                fosc = base_fosc * (1 + 0.001)

        elif mcu.MCKSEL.get_value() == 0B01:
            print(mcu.MX_FOSC.get_info(mcu.lang))
            fosc = mcu.MX_FOSC.get_value()
        elif mcu.MCKSEL.get_value() == 0B10:
            print(mcu.MX_FOSC.get_info(mcu.lang))
            fosc = mcu.MX_FOSC.get_value()
        else:
            print(mcu.MX_FOSC.get_info(mcu.lang))
            fosc = mcu.MX_FOSC.get_value()

        print("FOSC: %s" % util.format_frequency(fosc))
        print(mcu.CLKDIV_0.get_info(mcu.lang))
        print("SYSCLK: %s" % util.format_frequency(mcu.SYSCLK))

        print(mcu.MCLKOCRDIV.get_info(mcu.lang))
        if mcu.MCLKOCRDIV.get_value() != 0x00:
            print(mcu.MCLKO_S.get_info(mcu.lang))
            sysclk_output = int(mcu.SYSCLK/mcu.MCLKOCRDIV.get_value())
            print("Output clock: %s" % util.format_frequency(sysclk_output))

    def generate(self):
        mcu = self.base
        print("void clock_init()\n{")
        # extend ROM
        mcu.P_SW2.set_bits(0B1, 0B1, 7)
        mcu.P_SW2.output_code(mcu.verbose, mcu.lang, force=True)
        mcu.CKSEL.output_code(mcu.verbose, mcu.lang)
        mcu.HIRCCR.output_code(mcu.verbose, mcu.lang)
        mcu.XOSCCR.output_code(mcu.verbose, mcu.lang)
        mcu.IRC32KCR.output_code(mcu.verbose, mcu.lang)
        mcu.MCLKOCR.output_code(mcu.verbose, mcu.lang)
        mcu.CLKDIV.output_code(mcu.verbose, mcu.lang)
        mcu.IRCBAND.output_code(mcu.verbose, mcu.lang)
        mcu.VRTRIM.output_code(mcu.verbose, mcu.lang)
        mcu.IRTRIM.output_code(mcu.verbose, mcu.lang)
        mcu.LIRTRIM.output_code(mcu.verbose, mcu.lang)
        mcu.P_SW2.reset()
        mcu.P_SW2.output_code(mcu.verbose, mcu.lang, force=True)
        print('')
        # internal RAM
        print("}")