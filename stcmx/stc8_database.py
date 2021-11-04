from stcmx.sfr_model import SFRModel

class Stc8Database(object):
    """Database that holds SFR information."""

    def __init__(self):
        self.name:str = 'STC8 Generic'
        self.lang:str = 'en'
        self.verbose:bool = True
        # The frequency of internal or external oscillator, or external clock source
        self.FOSC:int = 11059200
        # System clock
        self.SYSCLK:int = 11059200

        # Basic SFR
        self.LIRTRIM = SFRModel('LIRTRIM', 0x9E, 0, 0x00, dict(en='Internal OSC Frequency Adjust', cn='IRC频率微调寄存器'))
        self.CLKDIV  = SFRModel('CLKDIV',    0xFE01, 1, 0x00, dict(en='System Clock Division Select', cn='时钟分频寄存器'))
        self.S4CON   = SFRModel('S4CON', 0x84, 0, 0x00, dict(en='UART4 Control', cn='串口4控制寄存器'))
        self.S4BUF   = SFRModel('S4BUF', 0x85, 0, 0x00, dict(en='UART4 Data', cn='串口4数据寄存器'))
        self.PCON    = SFRModel('PCON',  0x87, 0, 0x30, dict(en='Power Control', cn='电源控制寄存器'))
        self.TCON    = SFRModel('TCON',  0x88, 0, 0x00, dict(en='Timer Control', cn='定时器控制寄存器'))
        self.TMOD    = SFRModel('TMOD',  0x89, 0, 0x00, dict(en='Timer Mode', cn='定时器模式寄存器'))
        self.TL0     = SFRModel('TL0',   0x8A, 0, 0x00, dict(en='Timer0 Low 8bit', cn='定时器0低8位寄存器'))
        self.TL1     = SFRModel('TL1',   0x8B, 0, 0x00, dict(en='Timer1 Low 8bit', cn='定时器1低8位寄存器'))
        self.TH0     = SFRModel('TH0',   0x8C, 0, 0x00, dict(en='Timer0 High 8bit', cn='定时器0高8位寄存器'))
        self.TH1     = SFRModel('TH1',   0x8D, 0, 0x00, dict(en='Timer1 High 8bit', cn='定时器1高8位寄存器'))
        self.AUXR    = SFRModel('AUXR',  0x8E, 0, 0x01, dict(en='Auxr Control', cn='辅助寄存器'))
        self.INTCLKO = SFRModel('INTCLKO', 0x8F, 0, 0x00, dict(en='Timer output and Interrupt Control', cn='中断与时钟输出控制寄存器'))
        self.SCON    = SFRModel('SCON',  0x98, 0, 0x00, dict(en='UART1 Control', cn='串口1控制寄存器'))
        self.SBUF    = SFRModel('SBUF',  0x99, 0, 0x00, dict(en='UART1 Data', cn='串口1数据寄存器'))
        self.S2CON   = SFRModel('S2CON', 0x9A, 0, 0x40, dict(en='UART2 Control', cn='串口2控制寄存器'))
        self.S2BUF   = SFRModel('S2BUF', 0x9B, 0, 0x00, dict(en='UART2 Data', cn='串口2数据寄存器'))
        self.IRTRIM  = SFRModel('IRTRIM', 0x9F, 0, 0x00, dict(en='Internal OSC Frequency Control', cn='IRC频率调整寄存器'))
        self.S3CON   = SFRModel('S3CON', 0xAC, 0, 0x00, dict(en='UART3 Control', cn='串口3控制寄存器'))
        self.S3BUF   = SFRModel('S3BUF', 0xAD, 0, 0x00, dict(en='UART3 Data', cn='串口3数据寄存器'))
        self.SADDR   = SFRModel('SADDR', 0xA9, 0, 0x00, dict(en='UART1 Slave Address', cn='串口1从机地址寄存器'))
        self.WKTCL   = SFRModel('WKTCL', 0xAA, 0, 0x00, dict(en='Wakup Timer Low Byte', cn='掉电唤醒定时器低字节'))
        self.WKTCH   = SFRModel('WKTCL', 0xAB, 0, 0x00, dict(en='Wakeup Timer High Byte', cn='掉电唤醒定时器高字节'))
        self.SADEN   = SFRModel('SADEN', 0xB9, 0, 0x00, dict(en='UART1 Slave Deny Address', cn='串口1从机地址屏蔽寄存'))
        self.P_SW2   = SFRModel('P_SW2', 0xBA, 0, 0x00, dict(en='Peripheral Port Switch', cn='外设端口切换寄存器2'))
        self.PSW     = SFRModel('PSW',   0xD0, 0, 0x00, dict(en='Program Status', cn='程序状态字寄存器'))
        self.T4T3M   = SFRModel('T4T3M', 0xD1, 0, 0x00, dict(en='Timer4/3 Control', cn='定时器4/3控制寄存器'))
        self.T4H     = SFRModel('T4H',   0xD2, 0, 0x00, dict(en='Timer4 High Byte', cn='定时器4高字节'))
        self.T4L     = SFRModel('T4L',   0xD3, 0, 0x00, dict(en='Timer4 Low Byte', cn='定时器4低字节'))
        self.T3H     = SFRModel('T3H',   0xD4, 0, 0x00, dict(en='Timer3 High Byte', cn='定时器3高字节'))
        self.T3L     = SFRModel('T3L',   0xD5, 0, 0x00, dict(en='Timer4 Low Byte', cn='定时器3低字节'))
        self.T2H     = SFRModel('T2H',   0xD6, 0, 0x00, dict(en='Timer3 High Byte', cn='定时器2高字节'))
        self.T2L     = SFRModel('T2L',   0xD7, 0, 0x00, dict(en='Timer4 Low Byte', cn='定时器2低字节'))

        # Extend RAM SFR
        self.CKSEL   = SFRModel('CKSEL',     0xFE00, 1, 0x00, dict(en='Clock Source Select', cn='时钟选择寄存器'))
        self.XOSCCR  = SFRModel('XOSCCR',    0xFE03, 1, 0x00, dict(en='External OSC Control', cn='外部晶振控制寄存器'))
        self.IRC32KCR = SFRModel('IRC32KCR', 0xFE04, 1, 0x00, dict(en='Internal Low Frequency OSC Control', cn='内部32K振荡器控制寄存器'))


    def define_lang(self):
        languages = {'0': 'en', '1': 'cn'}
        while True:
            arg = self.input({
                'en': "Please select lanuage, Currently [%r]\n0: English, 1: 中文\n:"%self.lang,
                'cn': "请选择语言, 当前设置[%r]:\n0: English, 1: 中文\n:"%self.lang,
            })
            if len(arg) > 0:
                if arg in languages.keys():
                    self.lang = languages[arg]
                    break

    def define_verbose(self):
        while True:
            arg = self.input({
                'en': "Enable debug output? Currently [%r]\n0: No, 1: Yes\n:"%self.verbose,
                'cn': "开启Debug输出? 当前设置[%r]\n0: 否, 1: 是\n:"%self.verbose,
            })
            if len(arg) > 0:
                self.verbose = False if arg == '0' else True
                break

    def print(self, content:dict):
        print(content[self.lang])

    def input(self, content:dict):
        return input(content[self.lang])
