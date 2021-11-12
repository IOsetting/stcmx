from stcmx.stc8a_database import Stc8aDatabase
from stcmx.config_control import ConfigControl
from stcmx.stc8a.clock_config import ClockConfig
from stcmx.stc8a.timer_config import TimerConfig
from stcmx.stc8a.uart_config import UartConfig
from stcmx.stc8a.adc_config import AdcConfig
from stcmx.stc8a.pca_config import PcaConfig
from stcmx.stc8a.pin_config import PinConfig
from stcmx.stc8a.int_config import IntConfig
from stcmx.stc8a.spi_config import SpiConfig


class Stc8aConfig(Stc8aDatabase, ConfigControl):

    def __init__(self):
        super().__init__()
        self.FOSC = 24000000
        self.clock_config = ClockConfig(self)
        self.timer_config = TimerConfig(self)
        self.uart_config = UartConfig(self)
        self.adc_config = AdcConfig(self)
        self.pca_config = PcaConfig(self)
        self.pin_config = PinConfig(self)
        self.int_config = IntConfig(self)
        self.spi_config = SpiConfig(self)

        self.uart1: dict = {}
        # __init__ end

    def define_clock(self):
        self.print({'en': "==== SYSTEM CLOCK CONFIG START ====", 'cn': "==== 系统时钟配置开始 ===="})
        self.clock_config.config()
        self.print({'en': "==== SYSTEM CLOCK CONFIG END ====", 'cn': "==== 系统时钟配置结束 ===="})

    def define_power(self):
        self.print({'en': "==== POWER CONFIG START ====", 'cn': "==== 电源配置开始 ===="})
        self.PCON_PD.select(self.lang)
        self.PCON_IDEL.select(self.lang)
        self.print({'en': "==== POWER CONFIG END ====", 'cn': "==== 电源配置结束 ===="})

    def define_timer0(self):
        self.print({
            'en': "==== TIMER0 CONFIG START ====",
            'cn': "==== 定时器0 配置开始 ====",
        })
        self.timer_config.timer0_config()
        self.print({
            'en': "==== TIMER0 CONFIG END ====",
            'cn': "==== 定时器0 配置结束 ====",
        })

    def define_timer1(self):
        self.print({
            'en': "==== TIMER1 CONFIG START ====",
            'cn': "==== 定时器1 配置开始 ====",
        })
        self.timer_config.timer1_config()
        self.print({
            'en': "==== TIMER1 CONFIG END ====",
            'cn': "==== 定时器1 配置结束 ====",
        })

    def define_timer2(self):
        self.print({
            'en': "==== TIMER2 CONFIG START ====",
            'cn': "==== 定时器2 配置开始 ====",
        })
        self.timer_config.timer2_config()
        self.print({
            'en': "==== TIMER2 CONFIG END ====",
            'cn': "==== 定时器2 配置结束 ====",
        })

    def define_uart1(self):
        self.print({
            'en': "==== UART1 CONFIG START ====",
            'cn': "==== 串口1配置开始 ====",
        })
        self.uart_config.uart1_config()
        self.print({
            'en': "==== UART1 CONFIG END ====",
            'cn': "==== 串口1配置结束 ====",
        })

    def define_adc(self):
        self.print({
            'en': "==== ADC CONFIG START ====",
            'cn': "==== ADC配置开始 ====",
        })
        self.adc_config.config()
        self.print({
            'en': "==== ADC CONFIG END ====",
            'cn': "==== ADC配置结束 ====",
        })

    def define_pca(self):
        self.print({
            'en': "==== PCA/PWM CONFIG START ====",
            'cn': "==== PCA/PWM配置开始 ====",
        })
        self.pca_config.config()
        self.print({
            'en': "==== PCA/PWM CONFIG END ====",
            'cn': "==== PCA/PWM配置结束 ====",
        })

    def define_pca0(self):
        self.print({
            'en': "==== PCA0/PWM0 CONFIG START ====",
            'cn': "==== PCA0/PWM0配置开始 ====",
        })
        self.pca_config.pca0_config()
        self.print({
            'en': "==== PCA0/PWM0 CONFIG END ====",
            'cn': "==== PCA0/PWM0配置结束 ====",
        })

    def define_pca1(self):
        self.print({
            'en': "==== PCA1/PWM1 CONFIG START ====",
            'cn': "==== PCA1/PWM1配置开始 ====",
        })
        self.pca_config.pca1_config()
        self.print({
            'en': "==== PCA1/PWM1 CONFIG END ====",
            'cn': "==== PCA1/PWM1配置结束 ====",
        })

    def define_pca2(self):
        self.print({
            'en': "==== PCA2/PWM2 CONFIG START ====",
            'cn': "==== PCA2/PWM2配置开始 ====",
        })
        self.pca_config.pca2_config()
        self.print({
            'en': "==== PCA2/PWM2 CONFIG END ====",
            'cn': "==== PCA2/PWM2配置结束 ====",
        })

    def define_pca3(self):
        self.print({
            'en': "==== PCA3/PWM3 CONFIG START ====",
            'cn': "==== PCA3/PWM3配置开始 ====",
        })
        self.pca_config.pca3_config()
        self.print({
            'en': "==== PCA3/PWM3 CONFIG END ====",
            'cn': "==== PCA3/PWM3配置结束 ====",
        })

    def define_spi(self):
        self.print({
            'en': "==== SPI CONFIG START ====",
            'cn': "==== SPI配置开始 ====",
        })
        self.spi_config.config()
        self.print({
            'en': "==== SPI CONFIG END ====",
            'cn': "==== SPI配置结束 ====",
        })

    def info(self):
        self.clock_config.info()
        print('')
        self.timer_config.info()
        print('')
        self.uart_config.info()
        print('')
        self.adc_config.info()
        print('')
        self.pca_config.info()
        print('')
        self.spi_config.info()
        print('')
        self.pin_config.info()
        print('')
        self.int_config.info()

    def generate(self):
        print("Code for current configuration:\n MCU Type: %s\n" % self.name)
        print('''#include "stc8a.h"''')
        print('')
        self.clock_config.generate()
        print('')
        self.timer_config.generate()
        print('')
        self.uart_config.generate()
        print('')
        self.adc_config.generate()
        print('')
        self.pca_config.generate()
        print('')
        self.spi_config.generate()
        print('')
        self.pin_config.generate()
        print('')
        self.int_config.generate()
