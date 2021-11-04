
class BitFieldModel:

    def __init__(self, options:dict, prompt:dict, selection, offset:int, mask:int = 0B1, valid = lambda a: a, name:str = 'DUMMY', prompt_once:dict = None):
        self.name = name
        self.options = options
        self.prompt_once = prompt_once
        self.prompt = prompt
        self.selection = selection
        self.offset = offset
        self.mask = mask
        self.valid = valid
        self.value = None

    def set_selection(self, select_value):
        for k, v in self.options.items():
            if v == select_value:
                self.selection = k
                return

    def select(self, lang:str):
        if self.prompt_once is not None and len(self.prompt_once) > 0:
            print(self.prompt_once[lang])
        while True:
            arg = input(self.prompt[lang] % self.selection)
            arg = arg if len(arg) > 0 else self.selection
            if arg in self.options.keys():
                self.selection = arg
                self.value = self.options[arg]
                return arg

    def input(self, lang:str)->str:
        if self.prompt_once is not None and len(self.prompt_once) > 0:
            print(self.prompt_once[lang])
        while True:
            arg = input(self.prompt[lang] % self.selection)
            arg = arg if len(arg) > 0 else self.selection
            if self.valid(arg):
                self.selection = arg
                return arg
