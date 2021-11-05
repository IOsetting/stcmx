import cmd
from stcmx.stc8a_config import Stc8aConfig
from stcmx.stc8d_config import Stc8dConfig
from stcmx.config_control import ConfigControl


class Cli(cmd.Cmd):
    """Interactive Cli mode"""

    codegen:ConfigControl

    def __init__(self):
        super().__init__()

        lvds = {'stc8a': 0, 'stc8d': 1}
        while True:
            arg = input("Please choose a MCU type(请选择MCU类型) %s\n:" % list(lvds.keys()))
            if len(arg) > 0:
                if arg in lvds.keys():
                    if arg == 'stc8a':
                        self.codegen = Stc8aConfig()
                    elif arg == 'stc8d':
                        self.codegen = Stc8dConfig()
                    break
            print("Must be one of %s" % list(lvds.keys()))
        self.codegen.define_lang()

    def do_exit(self, line):
        exit(0)

    def do_quit(self, line):
        exit(0)

    def do_EOF(self, line):
        return True

    def do_lang(self, line):
        self.codegen.define_lang()

    def do_verbose(self, line):
        self.codegen.define_verbose()

    def do_clock(self, line):
        self.codegen.define_clock()

    def do_power(self, line):
        self.codegen.define_power()

    def do_timer0(self, line):
        self.codegen.define_timer0()

    def do_timer1(self, line):
        self.codegen.define_timer1()

    def do_timer2(self, line):
        self.codegen.define_timer2()

    def do_uart1(self, line):
        self.codegen.define_uart1()

    def do_info(self, line):
        self.codegen.info()

    def do_gen(self, line):
        self.codegen.generate()




