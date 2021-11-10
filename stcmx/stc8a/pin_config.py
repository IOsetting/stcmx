from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class PinConfig:

    def __init__(self, base: Stc8aConfig):
        self.base = base

    def info(self):
        mcu = self.base
        print(mcu.CCP_S.get_info(mcu.lang))
        print(mcu.SPI_S.get_info(mcu.lang))
        print(mcu.I2C_S.get_info(mcu.lang))
        print(mcu.CMPO_S.get_info(mcu.lang))
        print(mcu.S1_S.get_info(mcu.lang))
        print(mcu.S2_S.get_info(mcu.lang))
        print(mcu.S3_S.get_info(mcu.lang))
        print(mcu.S4_S.get_info(mcu.lang))

    def generate(self):
        mcu = self.base
        print("void pin_switch_init()\n{")
        mcu.P_SW1.output_code(mcu.verbose, mcu.lang)
        mcu.P_SW2.output_code(mcu.verbose, mcu.lang)
        print("}")

