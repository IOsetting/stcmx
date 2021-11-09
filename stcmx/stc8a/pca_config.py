from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class PcaConfig:

    def __init__(self, base: Stc8aConfig):
        self.base = base

    def info(self):
        mcu = self.base
        print(mcu.CR.get_info(mcu.lang))
        print(mcu.CPS.get_info(mcu.lang))
        print(mcu.ECF.get_info(mcu.lang))
        print(mcu.CCP_S.get_info(mcu.lang))
        print('')
        print(mcu.PWM0.get_info(mcu.lang))
        v = mcu.PWM0.get_value()
        if v == 0B1:
            print(mcu.EBS0.get_info(mcu.lang))
        print(mcu.ECOM0.get_info(mcu.lang))
        print(mcu.TOG0.get_info(mcu.lang))
        print(mcu.MAT0.get_info(mcu.lang))
        print(mcu.ECCF0.get_info(mcu.lang))
        print(mcu.CCAPP0.get_info(mcu.lang))
        print(mcu.CCAPN0.get_info(mcu.lang))
        print('')
        print(mcu.PWM1.get_info(mcu.lang))
        v = mcu.PWM1.get_value()
        if v == 0B1:
            print(mcu.EBS1.get_info(mcu.lang))
        print(mcu.ECOM1.get_info(mcu.lang))
        print(mcu.TOG1.get_info(mcu.lang))
        print(mcu.MAT1.get_info(mcu.lang))
        print(mcu.ECCF1.get_info(mcu.lang))
        print(mcu.CCAPP1.get_info(mcu.lang))
        print(mcu.CCAPN1.get_info(mcu.lang))
        print('')
        print(mcu.PWM2.get_info(mcu.lang))
        v = mcu.PWM2.get_value()
        if v == 0B1:
            print(mcu.EBS2.get_info(mcu.lang))
        print(mcu.ECOM2.get_info(mcu.lang))
        print(mcu.TOG2.get_info(mcu.lang))
        print(mcu.MAT2.get_info(mcu.lang))
        print(mcu.ECCF2.get_info(mcu.lang))
        print(mcu.CCAPP2.get_info(mcu.lang))
        print(mcu.CCAPN2.get_info(mcu.lang))
        print('')
        print(mcu.PWM3.get_info(mcu.lang))
        v = mcu.PWM3.get_value()
        if v == 0B1:
            print(mcu.EBS3.get_info(mcu.lang))
        print(mcu.ECOM3.get_info(mcu.lang))
        print(mcu.TOG3.get_info(mcu.lang))
        print(mcu.MAT3.get_info(mcu.lang))
        print(mcu.ECCF3.get_info(mcu.lang))
        print(mcu.CCAPP3.get_info(mcu.lang))
        print(mcu.CCAPN3.get_info(mcu.lang))

    def generate(self):
        mcu = self.base
        print("void pca_init()\n{")
        mcu.CCON.output_code(mcu.verbose, mcu.lang)
        mcu.CMOD.output_code(mcu.verbose, mcu.lang)
        mcu.CCAPM0.output_code(mcu.verbose, mcu.lang)
        mcu.CCAPM1.output_code(mcu.verbose, mcu.lang)
        mcu.CCAPM2.output_code(mcu.verbose, mcu.lang)
        mcu.CCAPM3.output_code(mcu.verbose, mcu.lang)
        if mcu.PWM0.get_value() == 0B1:
            mcu.PCA_PWM0.output_code(mcu.verbose, mcu.lang)
        if mcu.PWM1.get_value() == 0B1:
            mcu.PCA_PWM1.output_code(mcu.verbose, mcu.lang)
        if mcu.PWM2.get_value() == 0B1:
            mcu.PCA_PWM2.output_code(mcu.verbose, mcu.lang)
        if mcu.PWM3.get_value() == 0B1:
            mcu.PCA_PWM3.output_code(mcu.verbose, mcu.lang)
        print("}")

    def config(self):
        mcu = self.base
        mcu.CR.select(mcu.lang)
        mcu.CPS.select(mcu.lang)
        mcu.ECF.select(mcu.lang)
        mcu.CCP_S.select(mcu.lang)

    def pca0_config(self):
        mcu = self.base
        v = mcu.PWM0.select(mcu.lang)
        if v == 0B1:
            mcu.ECCF0.select(mcu.lang)
            mcu.EBS0.select(mcu.lang)
            mcu.ECOM0.set_value(0B1)
        else:
            mcu.ECOM0.select(mcu.lang)
            mcu.TOG0.select(mcu.lang)
            mcu.MAT0.select(mcu.lang)
        mcu.CCAPP0.select(mcu.lang)
        mcu.CCAPN0.select(mcu.lang)

    def pca1_config(self):
        mcu = self.base
        v = mcu.PWM1.select(mcu.lang)
        if v == 0B1:
            mcu.ECCF1.select(mcu.lang)
            mcu.EBS1.select(mcu.lang)
            mcu.ECOM0.set_value(0B1)
        else:
            mcu.ECOM1.select(mcu.lang)
            mcu.TOG1.select(mcu.lang)
            mcu.MAT1.select(mcu.lang)
        mcu.CCAPP1.select(mcu.lang)
        mcu.CCAPN1.select(mcu.lang)

    def pca2_config(self):
        mcu = self.base
        v = mcu.PWM2.select(mcu.lang)
        if v == 0B1:
            mcu.ECCF2.select(mcu.lang)
            mcu.EBS2.select(mcu.lang)
            mcu.ECOM0.set_value(0B1)
        else:
            mcu.ECOM2.select(mcu.lang)
            mcu.TOG2.select(mcu.lang)
            mcu.MAT2.select(mcu.lang)
        mcu.CCAPP2.select(mcu.lang)
        mcu.CCAPN2.select(mcu.lang)

    def pca3_config(self):
        mcu = self.base
        v = mcu.PWM3.select(mcu.lang)
        if v == 0B1:
            mcu.ECCF3.select(mcu.lang)
            mcu.EBS3.select(mcu.lang)
            mcu.ECOM0.set_value(0B1)
        else:
            mcu.ECOM3.select(mcu.lang)
            mcu.TOG3.select(mcu.lang)
            mcu.MAT3.select(mcu.lang)
        mcu.CCAPP3.select(mcu.lang)
        mcu.CCAPN3.select(mcu.lang)


