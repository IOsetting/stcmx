from __future__ import annotations
from typing import TYPE_CHECKING
import stcmx.util as util


if TYPE_CHECKING:
    from stcmx.stc8d_config import Stc8dConfig


class UartConfig:

    def __init__(self, base: Stc8dConfig):
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
                mcu.uart1['baudRate'] = int(mcu.SYSCLK)
            print("UART1 BaudRate: %d" % mcu.uart1['baudRate'])

        # 模式1, 波特率与时钟1/时钟2关联
        elif mode == 0B01:
            # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
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
                tm2ps = mcu.TM2PS_V.get_value()
                thl = (mcu.T2H.val << 8) + mcu.T2L.val
                baudRate = mcu.timer_config.timer2_freq_calculate(mode_1t == 0B1, tm2ps, thl, True)
            print("UART1 Freq: %d" % baudRate)

        # 模式2
        elif mode == 0B10:
            # 串口1模式1/2/3的双倍波特率模式
            print('TODO')

        # 模式3
        else:
            # 串口1模式1/2/3的双倍波特率模式
            print(mcu.SMOD.get_info(mcu.lang))
            # 串口1模式1/3波特率来源
            print(mcu.S1ST2.get_info(mcu.lang))

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
            mcu.SCON.set_bit(0B0, 5)
            uart_m0x6 = mcu.UART_M0x6.select(mcu.lang)
            if uart_m0x6 == 0B0:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK / 12)
            else:
                mcu.uart1['baudRate'] = int(mcu.SYSCLK)
            mcu.uart1['enabled'] = True

        # 模式1, 波特率与时钟1/时钟2关联
        elif mode == 0B01:
            # 模式 1 和模式 0 为非多机通信方式，在这两种方式时，SM2 应设置为 0
            mcu.SCON.set_bit(0B0, 5)
            # 串口1模式1/2/3的双倍波特率模式
            uart_rate_double = mcu.SMOD.select(mcu.lang) == 0B1
            # 串口1模式1/3可以配置波特率来源
            oscSource = mcu.S1ST2.select(mcu.lang)
            if oscSource == 0B0:  # 定时器1
                mcu.timer_config.timer1_config(True, uart_rate_double)
            else:  # 定时器2
                mcu.timer_config.timer2_config(True)

        # 模式2
        elif mode == 0B10:
            # 串口1模式1/2/3的双倍波特率模式
            doubleBaudRateMode = mcu.SMOD.select(mcu.lang)

        # 模式3
        else:
            # 串口1模式1/2/3的双倍波特率模式
            doubleBaudRateMode = mcu.SMOD.select(mcu.lang)
            # 串口1模式1/3波特率来源
            oscSource = mcu.S1ST2.select(mcu.lang)

        # 启用接收
        mcu.SCON_REN.select(mcu.lang)
        # 错误帧检测
        mcu.SMOD0.select(mcu.lang)
        mcu.uart1['enabled'] = True
