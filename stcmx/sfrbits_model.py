from stcmx.sfr_model import SFRModel


class SFRBitsModel:
    sfr:SFRModel
    masks:list = [0B0, 0B1, 0B11, 0B111, 0B1111, 0B11111, 0B111111, 0B1111111, 0B11111111]

    def __init__(
            self,
            sfr:SFRModel,
            name:str,
            offset:int,
            prompt:dict,
            len:int = 1,
            options:dict = None,
            prompt_once:dict = None,
            sbit:bool = False):

        self.sfr = sfr
        self.name = name,
        self.options = options
        self.prompt_once = prompt_once
        self.prompt = prompt
        self.offset = offset
        self.len = len
        self.sbit = sbit

    def get_value(self):
        return self.sfr.get_bits(self.masks[self.len],  self.offset)

    def set_value(self, value):
        self.sfr.set_bits(value, self.masks[self.len], self.offset)

    def get_selection(self):
        value = self.get_value()
        for k, v in self.options.items():
            if v == value:
                return k
        return None

    def set_selection(self, key):
        value = self.options[key]
        self.set_value(value)

    def select(self, lang:str):
        if self.prompt_once is not None and len(self.prompt_once) > 0:
            print(self.prompt_once[lang])
        if self.options is None or len(self.options) == 0:
            # Direct input
            while True:
                arg = input(self.prompt[lang] % self.get_value())
                if len(arg) > 0:
                    value = int(arg)
                    if 0 <= value <= self.masks[self.len]:
                        self.set_value(value)
                        break
                else:
                    # keep current value
                    break
        else:
            # Choose from options
            while True:
                arg = input(self.prompt[lang] % self.get_selection())
                if len(arg) > 0:
                    if arg in self.options.keys():
                        self.set_selection(arg)
                        break
                else:
                    # keep current selection
                    break
        return self.get_value()