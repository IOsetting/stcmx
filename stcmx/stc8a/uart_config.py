from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8a_config import Stc8aConfig


class UartConfig:

    def __init__(self, base: Stc8aConfig):
        self.base = base

    def info(self):
        mcu = self.base
        # uart1
        print(mcu.SCON_MODE.get_info(mcu.lang))
        mode = mcu.SCON_MODE.get_value()
        if mode == 0B00:
            print(mcu.UART_M0x6.get_info(mcu.lang))
            uart_m0x6 = mcu.UART_M0x6.get_value()
            if uart_m0x6 == 0B0:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 12)
            else:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 2)
            print("UART1 BaudRate: %d" % mcu.uart1['baudRate'])

        # 模式1, 波特率与时钟1/时钟2关联
        elif mode == 0B01:
            print(mcu.SMOD.get_info(mcu.lang))
            uart_rate_double = mcu.SMOD.get_value() == 0B1
            print(mcu.S1ST2.get_info(mcu.lang))
            oscSource = mcu.S1ST2.get_value()
            if oscSource == 0B0:  # 定时器1
                mode_1t = mcu.T1x12.get_value()
                t1mode = mcu.T1_MODE.get_value()
                if t1mode == 0B10:  # mode_2
                    thl = mcu.TH1.val
                else:
                    thl = (mcu.TH1.val << 8) + mcu.TL1.val
                baudRate = mcu.timer_config.timer0and1_freq_calculate(mode_1t == 0B1, t1mode == 0B10, thl, True, uart_rate_double)
            else:  # 定时器2
                mode_1t = mcu.T2x12.get_value()
                thl = (mcu.T2H.val << 8) + mcu.T2L.val
                baudRate = mcu.timer_config.timer2_freq_calculate(mode_1t == 0B1, thl, True)
            print("UART1 Baud Rate: %d" % baudRate)

        # 模式2
        elif mode == 0B10:
            print(mcu.SM2.get_info(mcu.lang))
            print(mcu.SMOD.get_info(mcu.lang))
            if mcu.SMOD.select(mcu.lang) == 0B0:
                baudRate = int(mcu.SYSCLK / 64)
            else:
                baudRate = int(mcu.SYSCLK / 32)
            print("UART1 Baud Rate: %d" % baudRate)

        # 模式3
        else:
            print(mcu.SM2.get_info(mcu.lang))
            print(mcu.SMOD.get_info(mcu.lang))
            uart_rate_double = mcu.SMOD.get_value() == 0B1
            print(mcu.S1ST2.get_info(mcu.lang))
            oscSource = mcu.S1ST2.get_value()
            if oscSource == 0B0:  # 定时器1
                mode_1t = mcu.T1x12.get_value()
                t1mode = mcu.T1_MODE.get_value()
                if t1mode == 0B10:  # mode_2
                    thl = mcu.TH1.val
                else:
                    thl = (mcu.TH1.val << 8) + mcu.TL1.val
                baudRate = mcu.timer_config.timer0and1_freq_calculate(mode_1t == 0B1, t1mode == 0B10, thl, True, uart_rate_double)
            else:  # 定时器2
                mode_1t = mcu.T2x12.get_value()
                thl = (mcu.T2H.val << 8) + mcu.T2L.val
                baudRate = mcu.timer_config.timer2_freq_calculate(mode_1t == 0B1, thl, True)
            print("UART1 Baud Rate: %d" % baudRate)

        # 启用接收
        print(mcu.SCON_REN.get_info(mcu.lang))
        # 错误帧检测
        print(mcu.SMOD0.get_info(mcu.lang))

    def generate(self):
        mcu = self.base
        print("void uart_init()\n{")
        # internal RAM
        mcu.SCON.output_code(mcu.verbose, mcu.lang)
        mcu.PCON.output_code(mcu.verbose, mcu.lang)
        mcu.AUXR.output_code(mcu.verbose, mcu.lang)
        print("}")

    def uart1_config(self):
        mcu = self.base
        # 选择串口1模式, 波特率与系统时钟关联, 固定
        mode = mcu.SCON_MODE.select(mcu.lang)
        # 模式0, 同步移位寄存器模式, 当UART_M0x6=0,波特率=SYSCLK/12, 当UART_M0x6=1时,波特率为SYSCLK/2
        if mode == 0B00:
            # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
            mcu.SM2.set_value(0B0)
            uart_m0x6 = mcu.UART_M0x6.select(mcu.lang)
            if uart_m0x6 == 0B0:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 12)
            else:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 2)

        # 模式1, 可变波特率8bit, 波特率与时钟1/时钟2关联
        elif mode == 0B01:
            # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
            mcu.SM2.set_value(0B0)
            # 串口1模式1/2/3的双倍波特率模式
            double_baud_rate = mcu.SMOD.select(mcu.lang) == 0B1
            # 串口1模式1/3可以配置波特率来源
            oscSource = mcu.S1ST2.select(mcu.lang)
            if oscSource == 0B0:  # 定时器1
                mcu.timer_config.timer1_config(True, double_baud_rate)
            else:  # 定时器2
                mcu.timer_config.timer2_config(True)

        # 模式2, 固定波特率9bit
        elif mode == 0B10:
            mcu.SM2.select(mcu.lang)
            # 串口1模式1/2/3的双倍波特率模式
            if mcu.SMOD.select(mcu.lang) == 0B0:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 64)
            else:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 32)

        # 模式3, 可变波特率9bit, 波特率与时钟1/时钟2关联
        else:
            mcu.SM2.select(mcu.lang)
            # 串口1模式1/2/3的双倍波特率模式
            double_baud_rate = mcu.SMOD.select(mcu.lang) == 0B1
            # 串口1模式1/3波特率来源
            oscSource = mcu.S1ST2.select(mcu.lang)
            if oscSource == 0B0:  # 定时器1
                mcu.timer_config.timer1_config(True, double_baud_rate)
            else:  # 定时器2
                mcu.timer_config.timer2_config(True)

        # 启用接收
        mcu.SCON_REN.select(mcu.lang)
        # 错误帧检测
        mcu.SMOD0.select(mcu.lang)
        # 管脚选择
        mcu.S1_S.select(mcu.lang)
