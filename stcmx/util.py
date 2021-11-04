
def format_frequency(val):
    if val > 1000000:
        return "%.6fMHz"%(val / 1000000)
    elif val > 1000:
        return "%.3fKHz"%(val / 1000)
    else:
        return "%dHz"%(val)


class SelectHelper:

    def __init__(self, options:dict, prompt:dict, selection, prompt_once:dict = None):
        self.options = options
        self.prompt_once = prompt_once
        self.prompt = prompt
        self.selection = selection

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
            if len(arg) > 0:
                if arg in self.options.keys():
                    self.selection = arg
                    return self.options[arg]
                else:
                    return self.options[self.selection]


class InputHelper:

    def __init__(self, prompt:dict, value, valid = lambda a: a, prompt_once:dict = None):
        self.value = value
        self.prompt_once = prompt_once
        self.prompt = prompt
        self.valid = valid

    def input(self, lang: str) -> str:
        if self.prompt_once is not None and len(self.prompt_once) > 0:
            print(self.prompt_once[lang])
        while True:
            arg = input(self.prompt[lang] % self.value)
            if len(arg) > 0:
                if self.valid(arg):
                    self.value = arg
                    return arg
            else:
                return self.value
