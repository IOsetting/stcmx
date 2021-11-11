from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class IntConfig:

    def __init__(self, base: Stc8aConfig):
        self.base = base

    def info(self):
        mcu = self.base
        print(mcu.EA.get_info(mcu.lang))
        print(mcu.ELVD.get_info(mcu.lang))
        print(mcu.EADC.get_info(mcu.lang))
        print(mcu.CMPO_S.get_info(mcu.lang))
        print(mcu.ES.get_info(mcu.lang))
        print(mcu.ES2.get_info(mcu.lang))
        print(mcu.ES3.get_info(mcu.lang))
        print(mcu.ES4.get_info(mcu.lang))
        print(mcu.ET0.get_info(mcu.lang))
        print(mcu.ET1.get_info(mcu.lang))
        print(mcu.ET2.get_info(mcu.lang))
        print(mcu.ET3.get_info(mcu.lang))
        print(mcu.ET4.get_info(mcu.lang))
        print(mcu.EX0.get_info(mcu.lang))
        print(mcu.EX1.get_info(mcu.lang))
        print(mcu.ESPI.get_info(mcu.lang))

    def generate(self):
        mcu = self.base
        print("void int_init()\n{")
        mcu.IE.output_code(mcu.verbose, mcu.lang)
        mcu.IE2.output_code(mcu.verbose, mcu.lang)
        print("}")

