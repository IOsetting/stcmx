from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class SpiConfig:

    def __init__(self, base: Stc8aConfig):
        self.base = base

    def info(self):
        mcu = self.base
        print(mcu.SPEN.get_info(mcu.lang))
        if mcu.SPEN.get_value() == 0B1:
            print(mcu.SSIG.get_info(mcu.lang))
            print(mcu.DORD.get_info(mcu.lang))
            print(mcu.MSTR.get_info(mcu.lang))
            print(mcu.CPOL.get_info(mcu.lang))
            print(mcu.CPHA.get_info(mcu.lang))
            print(mcu.SPR.get_info(mcu.lang))

    def generate(self):
        mcu = self.base
        if mcu.SPEN.get_value() == 0B1:
            print("void spi_init()\n{")
            mcu.SPCTL.output_code(mcu.verbose, mcu.lang)
            print("}")

    def config(self):
        mcu = self.base
        mcu.SPEN.select(mcu.lang)
        if mcu.SPEN.get_value() == 0B1:
            mcu.SSIG.select(mcu.lang)
            mcu.DORD.select(mcu.lang)
            mcu.MSTR.select(mcu.lang)
            mcu.CPOL.select(mcu.lang)
            mcu.CPHA.select(mcu.lang)
            mcu.SPR.select(mcu.lang)

    def get_spi_clock(self):
        fosc = self.base.clock_config.get_sysclk()
        return fosc / (2 << (self.base.SPR.get_value() + 2))