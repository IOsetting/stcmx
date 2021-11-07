
class ValueModel:
    """Value Input Model"""

    prompt_word: dict = {'en': '. Currently [%s]\n:', 'cn': '. 当前设置[%s]\n:'}

    def __init__(
            self,
            name: str,
            value,
            title: dict,
            type:str = 'int',
            valid = lambda a: a,
            prompt_word: dict = None):
        self.name = name
        self.value = value
        self.title = title
        self.type = type
        """值的类型, 默认为int, 可以使用str, float"""
        self.valid = valid
        if prompt_word is not None:
            self.prompt_word = prompt_word

    def get_value(self):
        return self.value

    def get_info(self, lang:str):
        if self.type == 'int':
            value = '%d'%self.value
        elif self.type == 'float':
            value = '%f'%self.value
        else:
            value = self.value
        return self.title[lang] + ': ' + value

    def set_value(self, value):
        self.value = value

    def input(self, lang:str):
        # Direct input
        while True:
            arg = input(self.title[lang] + self.prompt_word[lang] % self.value)
            if len(arg) > 0:
                if self.type == 'int':
                    value = int(arg)
                elif self.type == 'float':
                    value = float(arg)
                else:
                    value = arg
                if self.valid(value):
                    self.value = value
                    return value
            else:
                # keep current value
                break
        return self.value
