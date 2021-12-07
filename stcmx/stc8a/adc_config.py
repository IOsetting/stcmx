from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class AdcConfig:

    def __init__(self, base: Stc8aConfig):
        self.base = base

    def info(self):
        mcu = self.base
        print(mcu.ADC_POWER.get_info(mcu.lang))
        if mcu.ADC_POWER.get_value() == 0B1:
            print(mcu.ADC_RESFMT.get_info(mcu.lang))
            print(mcu.ADC_SPEED.get_info(mcu.lang))
            print(mcu.ADC_CHS.get_info(mcu.lang))

    def generate(self):
        mcu = self.base
        print("void adc_init()\n{")
        mcu.ADC_CONTR.output_code()
        mcu.ADCCFG.output_code()
        print("}")

    def config(self):
        mcu = self.base
        mcu.ADC_POWER.select(mcu.lang)
        mcu.ADC_RESFMT.select(mcu.lang)
        mcu.ADC_SPEED.select(mcu.lang)
        mcu.ADC_CHS.select(mcu.lang)
