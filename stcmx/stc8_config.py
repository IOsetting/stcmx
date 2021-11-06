from stcmx.stc8_database import Stc8Database
from stcmx.sfrbits_model import SFRBitsModel


class Stc8Config(Stc8Database):
    """STC8 Base Configurations."""

    def __init__(self):
        super().__init__()
        # __init__ end

    def frequency_adjust(self):
        """Adjust frequency"""
        if self.MCKSEL.get_value() == 0B01 or self.MCKSEL.get_value() == 0B10:
            self.print({
                'en': "External clock source, skip frequency adjust",
                'cn': "外部震荡源/时钟源, 跳过频率调节",
            })
            return
        elif self.MCKSEL.get_value() == 0B11:
            self.print({
                'en': "Internal low frequency OSC, skip frequency adjust",
                'cn': "内部低频晶振, 跳过频率调节",
            })
            return
        value = self.LIRTRIM_0.select(self.lang)
        if value == 0B01:
            self.FOSC = int(self.FOSC * 1.0001)
        elif value == 0B10:
            self.FOSC = int(self.FOSC * 1.0004)
        elif value == 0B11:
            self.FOSC = int(self.FOSC * 1.001)

