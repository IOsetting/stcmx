
class SelectionModel:
    """Selection Model"""

    prompt_word: dict = {'en': '. Currently [%s]:\n', 'cn': '. 当前选择[%s]:\n'}

    def __init__(
            self,
            name: str,
            selection,
            title: dict,
            options: dict = None,
            values: dict = None,
            prompt_word: dict = None):
        self.name = name
        self.selection = selection
        self.title = title
        self.values = values
        self.options = options
        if prompt_word is not None:
            self.prompt_word = prompt_word

    def get_selection(self):
        return self.selection

    def get_value(self):
        return self.values[self.selection]

    def get_info(self, lang:str):
        return self.title[lang] + ': ' + self.get_selected_option(lang)

    def get_selected_option(self, lang:str):
        return self.options[self.selection][lang]

    def set_value(self, value):
        for k, v in self.values.items():
            if v == value:
                self.selection = k
                return k
        return None

    def set_selection(self, selection):
        self.selection = selection

    def select(self, lang:str):
        while True:
            arg = input(self.get_prompt(lang))
            if len(arg) > 0:
                if arg in self.values.keys():
                    self.selection = arg
                    break
            else:
                # keep current selection
                break
        return self.values[self.selection]

    def get_prompt(self, lang:str):
        output = self.title[lang] + self.prompt_word[lang] % self.get_selection()
        for k, v in self.options.items():
            output += "  %s: %s\n" % (k, v[lang])
        return output + ":"
