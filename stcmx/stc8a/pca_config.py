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
        print(mcu.CIDL.get_info(mcu.lang))
        print(mcu.CPS.get_info(mcu.lang))
        print(mcu.ECF.get_info(mcu.lang))
        pcaclk = self.get_pca_clock()
        print("PCA Clock: %s" % util.format_frequency(pcaclk))
        print('')

        print(mcu.PWM0.get_info(mcu.lang))
        v = mcu.PWM0.get_value()
        if v == 0B1:  # PWM Mode
            print(mcu.EBS0.get_info(mcu.lang))
            print(mcu.CCAP0HV.get_info(mcu.lang))
            print(mcu.XCCAP0H.get_info(mcu.lang))
            print(mcu.CCAP0LV.get_info(mcu.lang))
            print(mcu.XCCAP0L.get_info(mcu.lang))
            print("PWM0 Freq: %.3f, Duty Cycle: %.3f" %(self.get_pwm0_frequency(pcaclk), self.get_pwm0_duty_cycle()))

        print(mcu.ECOM0.get_info(mcu.lang))
        print(mcu.TOG0.get_info(mcu.lang))
        print(mcu.MAT0.get_info(mcu.lang))
        print(mcu.ECCF0.get_info(mcu.lang))
        print(mcu.CCAPP0.get_info(mcu.lang))
        print(mcu.CCAPN0.get_info(mcu.lang))
        print('')

        print(mcu.PWM1.get_info(mcu.lang))
        v = mcu.PWM1.get_value()
        if v == 0B1:  # PWM Mode
            print(mcu.EBS1.get_info(mcu.lang))
            print(mcu.CCAP1HV.get_info(mcu.lang))
            print(mcu.XCCAP1H.get_info(mcu.lang))
            print(mcu.CCAP1LV.get_info(mcu.lang))
            print(mcu.XCCAP1L.get_info(mcu.lang))
            print("PWM1 Freq: %.3f, Duty Cycle: %.3f" % (self.get_pwm1_frequency(pcaclk), self.get_pwm1_duty_cycle()))
        print(mcu.ECOM1.get_info(mcu.lang))
        print(mcu.TOG1.get_info(mcu.lang))
        print(mcu.MAT1.get_info(mcu.lang))
        print(mcu.ECCF1.get_info(mcu.lang))
        print(mcu.CCAPP1.get_info(mcu.lang))
        print(mcu.CCAPN1.get_info(mcu.lang))
        print('')

        print(mcu.PWM2.get_info(mcu.lang))
        v = mcu.PWM2.get_value()
        if v == 0B1:  # PWM Mode
            print(mcu.EBS2.get_info(mcu.lang))
            print(mcu.CCAP2HV.get_info(mcu.lang))
            print(mcu.XCCAP2H.get_info(mcu.lang))
            print(mcu.CCAP2LV.get_info(mcu.lang))
            print(mcu.XCCAP2L.get_info(mcu.lang))
            print("PWM2 Freq: %.3f, Duty Cycle: %.3f" % (self.get_pwm2_frequency(pcaclk), self.get_pwm2_duty_cycle()))
        print(mcu.ECOM2.get_info(mcu.lang))
        print(mcu.TOG2.get_info(mcu.lang))
        print(mcu.MAT2.get_info(mcu.lang))
        print(mcu.ECCF2.get_info(mcu.lang))
        print(mcu.CCAPP2.get_info(mcu.lang))
        print(mcu.CCAPN2.get_info(mcu.lang))
        print('')

        print(mcu.PWM3.get_info(mcu.lang))
        v = mcu.PWM3.get_value()
        if v == 0B1:  # PWM Mode
            print(mcu.EBS3.get_info(mcu.lang))
            print(mcu.CCAP3HV.get_info(mcu.lang))
            print(mcu.XCCAP3H.get_info(mcu.lang))
            print(mcu.CCAP3LV.get_info(mcu.lang))
            print(mcu.XCCAP3L.get_info(mcu.lang))
            print("PWM3 Freq: %.3f, Duty Cycle: %.3f" % (self.get_pwm3_frequency(pcaclk), self.get_pwm3_duty_cycle()))
        print(mcu.ECOM3.get_info(mcu.lang))
        print(mcu.TOG3.get_info(mcu.lang))
        print(mcu.MAT3.get_info(mcu.lang))
        print(mcu.ECCF3.get_info(mcu.lang))
        print(mcu.CCAPP3.get_info(mcu.lang))
        print(mcu.CCAPN3.get_info(mcu.lang))

    def get_pca_clock(self):
        mcu = self.base
        pca_clock = 0
        v = mcu.CPS.get_value()  # clock source
        sysclk = mcu.clock_config.get_sysclk()
        if v == 0B000:
            pca_clock = int(sysclk / 12)
        elif v == 0B001:
            pca_clock = int(sysclk / 2)
        elif v == 0B010:
            pca_clock = mcu.timer_config.get_timer0_freq()
        elif v == 0B011:
            pca_clock = 0
        elif v == 0B100:
            pca_clock = sysclk
        elif v == 0B101:
            pca_clock = int(sysclk / 4)
        elif v == 0B110:
            pca_clock = int(sysclk / 6)
        elif v == 0B111:
            pca_clock = int(sysclk / 8)
        return pca_clock

    def get_pwm0_duty_cycle(self):
        mcu = self.base
        v = mcu.EBS0.get_value()
        lv = mcu.CCAP0HV.get_value()
        hv = mcu.XCCAP0H.get_value()
        if v == 0B00:  # 8bit
            return lv / 256 * 100
        elif v == 0B01:  # 7bit
            return lv / 128 * 100
        elif v == 0B10:  # 6bit
            return lv / 64 * 100
        else:  # 10bit
            lv = lv + (hv << 8)
            return lv / 1024 * 100

    def get_pwm1_duty_cycle(self):
        mcu = self.base
        v = mcu.EBS1.get_value()
        lv = mcu.CCAP1HV.get_value()
        hv = mcu.XCCAP1H.get_value()
        if v == 0B00:  # 8bit
            return lv / 256 * 100
        elif v == 0B01:  # 7bit
            return lv / 128 * 100
        elif v == 0B10:  # 6bit
            return lv / 64 * 100
        else:  # 10bit
            lv = lv + (hv << 8)
            return lv / 1024 * 100

    def get_pwm2_duty_cycle(self):
        mcu = self.base
        v = mcu.EBS2.get_value()
        lv = mcu.CCAP2HV.get_value()
        hv = mcu.XCCAP2H.get_value()
        if v == 0B00:  # 8bit
            return lv / 256 * 100
        elif v == 0B01:  # 7bit
            return lv / 128 * 100
        elif v == 0B10:  # 6bit
            return lv / 64 * 100
        else:  # 10bit
            lv = lv + (hv << 8)
            return lv / 1024 * 100

    def get_pwm3_duty_cycle(self):
        mcu = self.base
        v = mcu.EBS3.get_value()
        lv = mcu.CCAP3HV.get_value()
        hv = mcu.XCCAP3H.get_value()
        if v == 0B00:  # 8bit
            return lv / 256 * 100
        elif v == 0B01:  # 7bit
            return lv / 128 * 100
        elif v == 0B10:  # 6bit
            return lv / 64 * 100
        else:  # 10bit
            lv = lv + (hv << 8)
            return lv / 1024 * 100

    def get_pwm0_frequency(self, pca_freq):
        mcu = self.base
        v = mcu.EBS0.get_value()
        if v == 0B00:  # 8bit
            return pca_freq / 256
        elif v == 0B01:  # 7bit
            return pca_freq / 128
        elif v == 0B10:  # 6bit
            return pca_freq / 64
        else:  # 10bit
            return pca_freq / 1024

    def get_pwm1_frequency(self, pca_freq):
        mcu = self.base
        v = mcu.EBS1.get_value()
        if v == 0B00:  # 8bit
            return pca_freq / 256
        elif v == 0B01:  # 7bit
            return pca_freq / 128
        elif v == 0B10:  # 6bit
            return pca_freq / 64
        else:  # 10bit
            return pca_freq / 1024

    def get_pwm2_frequency(self, pca_freq):
        mcu = self.base
        v = mcu.EBS2.get_value()
        if v == 0B00:  # 8bit
            return pca_freq / 256
        elif v == 0B01:  # 7bit
            return pca_freq / 128
        elif v == 0B10:  # 6bit
            return pca_freq / 64
        else:  # 10bit
            return pca_freq / 1024

    def get_pwm3_frequency(self, pca_freq):
        mcu = self.base
        v = mcu.EBS3.get_value()
        if v == 0B00:  # 8bit
            return pca_freq / 256
        elif v == 0B01:  # 7bit
            return pca_freq / 128
        elif v == 0B10:  # 6bit
            return pca_freq / 64
        else:  # 10bit
            return pca_freq / 1024

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
            mcu.PCA_PWM0.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP0H.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP0L.output_code(mcu.verbose, mcu.lang, force=True)
        if mcu.PWM1.get_value() == 0B1:
            mcu.PCA_PWM1.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP1H.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP1L.output_code(mcu.verbose, mcu.lang, force=True)
        if mcu.PWM2.get_value() == 0B1:
            mcu.PCA_PWM2.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP2H.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP2L.output_code(mcu.verbose, mcu.lang, force=True)
        if mcu.PWM3.get_value() == 0B1:
            mcu.PCA_PWM3.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP3H.output_code(mcu.verbose, mcu.lang, force=True)
            mcu.CCAP3L.output_code(mcu.verbose, mcu.lang, force=True)
        print("}")

    def config(self):
        mcu = self.base
        mcu.CR.select(mcu.lang)
        mcu.CIDL.select(mcu.lang)
        mcu.CPS.select(mcu.lang)
        mcu.ECF.select(mcu.lang)
        mcu.CCP_S.select(mcu.lang)

    def pca0_config(self):
        mcu = self.base
        v = mcu.PWM0.select(mcu.lang)
        if v == 0B1:  # PWM Mode
            mcu.ECCF0.select(mcu.lang)
            v2 = mcu.EBS0.select(mcu.lang)
            # Calculate duty cycles
            dc = mcu.MX_PWM0_DUTY_CYCLE.input(mcu.lang)
            if v2 == 0B00:  # 8bit
                dc = int(256 * dc / 100)
                mcu.CCAP0LV.set_value(dc)
                mcu.CCAP0HV.set_value(dc)
            elif v2 == 0B01:  # 7bit
                dc = int(128 * dc / 100)
                mcu.CCAP0LV.set_value(dc)
                mcu.CCAP0HV.set_value(dc)
            elif v2 == 0B10:  # 6bit
                dc = int(64 * dc / 100)
                mcu.CCAP0LV.set_value(dc)
                mcu.CCAP0HV.set_value(dc)
            else: # 10bit
                dc = int(1024 * dc / 100)
                mcu.CCAP0LV.set_value(dc & 0xFF)
                mcu.CCAP0HV.set_value(dc & 0xFF)
                mcu.XCCAP0L.set_value(dc >> 8)
                mcu.XCCAP0H.set_value(dc >> 8)

            mcu.ECOM0.set_value(0B1)
            mcu.TOG0.set_value(0B0)
            mcu.MAT0.set_value(0B0)
        else:
            mcu.ECCF0.set_value(0B0)
            mcu.EBS0.set_value(0B00)
            mcu.ECOM0.select(mcu.lang)
            mcu.TOG0.select(mcu.lang)
            mcu.MAT0.select(mcu.lang)
        mcu.CCAPP0.select(mcu.lang)
        mcu.CCAPN0.select(mcu.lang)

    def pca1_config(self):
        mcu = self.base
        v = mcu.PWM1.select(mcu.lang)
        if v == 0B1:  # PWM Mode
            mcu.ECCF1.select(mcu.lang)
            v2 = mcu.EBS1.select(mcu.lang)
            # Calculate duty cycles
            dc = mcu.MX_PWM1_DUTY_CYCLE.input(mcu.lang)
            if v2 == 0B00:  # 8bit
                dc = int(256 * dc / 100)
                mcu.CCAP1LV.set_value(dc)
                mcu.CCAP1HV.set_value(dc)
            elif v2 == 0B01:  # 7bit
                dc = int(128 * dc / 100)
                mcu.CCAP1LV.set_value(dc)
                mcu.CCAP1HV.set_value(dc)
            elif v2 == 0B10:  # 6bit
                dc = int(64 * dc / 100)
                mcu.CCAP1LV.set_value(dc)
                mcu.CCAP1HV.set_value(dc)
            else:  # 10bit
                dc = int(1024 * dc / 100)
                mcu.CCAP1LV.set_value(dc & 0xFF)
                mcu.CCAP1HV.set_value(dc & 0xFF)
                mcu.XCCAP1L.set_value(dc >> 8)
                mcu.XCCAP1H.set_value(dc >> 8)

            mcu.ECOM1.set_value(0B1)
            mcu.TOG1.set_value(0B0)
            mcu.MAT1.set_value(0B0)
        else:
            mcu.ECCF1.set_value(0B0)
            mcu.EBS1.set_value(0B00)
            mcu.ECOM1.select(mcu.lang)
            mcu.TOG1.select(mcu.lang)
            mcu.MAT1.select(mcu.lang)
        mcu.CCAPP1.select(mcu.lang)
        mcu.CCAPN1.select(mcu.lang)

    def pca2_config(self):
        mcu = self.base
        v = mcu.PWM2.select(mcu.lang)
        if v == 0B1:  # PWM Mode
            mcu.ECCF2.select(mcu.lang)
            v2 = mcu.EBS2.select(mcu.lang)
            # Calculate duty cycles
            dc = mcu.MX_PWM2_DUTY_CYCLE.input(mcu.lang)
            if v2 == 0B00:  # 8bit
                dc = int(256 * dc / 100)
                mcu.CCAP2LV.set_value(dc)
                mcu.CCAP2HV.set_value(dc)
            elif v2 == 0B01:  # 7bit
                dc = int(128 * dc / 100)
                mcu.CCAP2LV.set_value(dc)
                mcu.CCAP2HV.set_value(dc)
            elif v2 == 0B10:  # 6bit
                dc = int(64 * dc / 100)
                mcu.CCAP2LV.set_value(dc)
                mcu.CCAP2HV.set_value(dc)
            else:  # 10bit
                dc = int(1024 * dc / 100)
                mcu.CCAP2LV.set_value(dc & 0xFF)
                mcu.CCAP2HV.set_value(dc & 0xFF)
                mcu.XCCAP2L.set_value(dc >> 8)
                mcu.XCCAP2H.set_value(dc >> 8)
            mcu.ECOM2.set_value(0B1)
            mcu.TOG2.set_value(0B0)
            mcu.MAT2.set_value(0B0)
        else:
            mcu.ECCF2.set_value(0B0)
            mcu.EBS2.set_value(0B00)
            mcu.ECOM2.select(mcu.lang)
            mcu.TOG2.select(mcu.lang)
            mcu.MAT2.select(mcu.lang)
        mcu.CCAPP2.select(mcu.lang)
        mcu.CCAPN2.select(mcu.lang)

    def pca3_config(self):
        mcu = self.base
        v = mcu.PWM3.select(mcu.lang)
        if v == 0B1:  # PWM Mode
            mcu.ECCF3.select(mcu.lang)
            v2 = mcu.EBS3.select(mcu.lang)
            # Calculate duty cycles
            dc = mcu.MX_PWM3_DUTY_CYCLE.input(mcu.lang)
            if v2 == 0B00:  # 8bit
                dc = int(256 * dc / 100)
                mcu.CCAP3LV.set_value(dc)
                mcu.CCAP3HV.set_value(dc)
            elif v2 == 0B01:  # 7bit
                dc = int(128 * dc / 100)
                mcu.CCAP3LV.set_value(dc)
                mcu.CCAP3HV.set_value(dc)
            elif v2 == 0B10:  # 6bit
                dc = int(64 * dc / 100)
                mcu.CCAP3LV.set_value(dc)
                mcu.CCAP3HV.set_value(dc)
            else:  # 10bit
                dc = int(1024 * dc / 100)
                mcu.CCAP3LV.set_value(dc & 0xFF)
                mcu.CCAP3HV.set_value(dc & 0xFF)
                mcu.XCCAP3L.set_value(dc >> 8)
                mcu.XCCAP3H.set_value(dc >> 8)
            mcu.ECOM3.set_value(0B1)
            mcu.TOG3.set_value(0B0)
            mcu.MAT3.set_value(0B0)
        else:
            mcu.ECCF3.set_value(0B0)
            mcu.EBS3.set_value(0B00)
            mcu.ECOM3.select(mcu.lang)
            mcu.TOG3.select(mcu.lang)
            mcu.MAT3.select(mcu.lang)
        mcu.CCAPP3.select(mcu.lang)
        mcu.CCAPN3.select(mcu.lang)


