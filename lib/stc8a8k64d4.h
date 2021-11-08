#ifndef __STC8A8K64D4_H__
#define __STC8A8K64D4_H__

#include <compiler.h>

#define  _P0            0x80
SFR(P0,                 _P0);
SBIT(P00,               _P0, 0);
SBIT(P01,               _P0, 1);
SBIT(P02,               _P0, 2);
SBIT(P03,               _P0, 3);
SBIT(P04,               _P0, 4);
SBIT(P05,               _P0, 5);
SBIT(P06,               _P0, 6);
SBIT(P07,               _P0, 7);
SFR(SP,                 0x81);
SFR(DPL,                0x82);
SFR(DPH,                0x83);
SFR(S4CON,              0x84);
#define  S4SM0              0x80
#define  S4ST4              0x40
#define  S4SM2              0x20
#define  S4REN              0x10
#define  S4TB8              0x08
#define  S4RB8              0x04
#define  S4TI               0x02
#define  S4RI               0x01
SFR(S4BUF,              0x85);
SFR(PCON,               0x87);
#define  SMOD               0x80
#define  SMOD0              0x40
#define  LVDF               0x20
#define  POF                0x10
#define  GF1                0x08
#define  GF0                0x04
#define  PD                 0x02
#define  IDL                0x01
#define  _TCON          0x88
SFR(TCON,               _TCON);
SBIT(TF1,               _TCON, 7);
SBIT(TR1,               _TCON, 6);
SBIT(TF0,               _TCON, 5);
SBIT(TR0,               _TCON, 4);
SBIT(IE1,               _TCON, 3);
SBIT(IT1,               _TCON, 2);
SBIT(IE0,               _TCON, 1);
SBIT(IT0,               _TCON, 0);
SFR(TMOD,               0x89);

#define  T1_GATE            0x80
#define  T1_CT              0x40
#define  T1_M1              0x20
#define  T1_M0              0x10
#define  T0_GATE            0x08
#define  T0_CT              0x04
#define  T0_M1              0x02
#define  T0_M0              0x01
SFR(TL0,                0x8A);
SFR(TL1,                0x8B);
SFR(TH0,                0x8C);
SFR(TH1,                0x8D);
SFR(AUXR,               0x8E);
#define  T0x12              0x80
#define  T1x12              0x40
#define  UART_M0x6          0x20
#define  T2R                0x10
#define  T2_CT              0x08
#define  T2x12              0x04
#define  EXTRAM             0x02
#define  S1ST2              0x01
SFR(INTCLKO,            0x8F);
#define  EX4                0x40
#define  EX3                0x20
#define  EX2                0x10
#define  T2CLKO             0x04
#define  T1CLKO             0x02
#define  T0CLKO             0x01
#define  _P1            0x90
SFR(P1,                 _P1);
SBIT(P10,               _P1, 0);
SBIT(P11,               _P1, 1);
SBIT(P12,               _P1, 2);
SBIT(P13,               _P1, 3);
SBIT(P14,               _P1, 4);
SBIT(P15,               _P1, 5);
SBIT(P16,               _P1, 6);
SBIT(P17,               _P1, 7);

SFR(P1M1,               0x91);
SFR(P1M0,               0x92);
SFR(P0M1,               0x93);
SFR(P0M0,               0x94);
SFR(P2M1,               0x95);
SFR(P2M0,               0x96);

#define  _SCON          0x98
SFR(SCON,               _SCON);
SBIT(SM0,               _SCON, 7);
SBIT(SM1,               _SCON, 6);
SBIT(SM2,               _SCON, 5);
SBIT(REN,               _SCON, 4);
SBIT(TB8,               _SCON, 3);
SBIT(RB8,               _SCON, 2);
SBIT(TI,                _SCON, 1);
SBIT(RI,                _SCON, 0);

SFR(SBUF,               0x99);
SFR(S2CON,              0x9A);
#define  S2SM0              0x80
#define  S2SM2              0x20
#define  S2REN              0x10
#define  S2TB8              0x08
#define  S2RB8              0x04
#define  S2TI               0x02
#define  S2RI               0x01
SFR(S2BUF,              0x9B);
SFR(IRCBAND,            0x9D);
SFR(LIRTRIM,            0x9E);
SFR(IRTRIM,             0x9F);
#define  _P2            0xA0
SFR(P2,                 _P2);
SBIT(P20,               _P2, 0);
SBIT(P21,               _P2, 1);
SBIT(P22,               _P2, 2);
SBIT(P23,               _P2, 3);
SBIT(P24,               _P2, 4);
SBIT(P25,               _P2, 5);
SBIT(P26,               _P2, 6);
SBIT(P27,               _P2, 7);

SFR(BUS_SPEED,          0xA1);
SFR(P_SW1,              0xA2);
#define  UART1_S1           0x00
#define  UART1_S2           0x40
#define  UART1_S3           0x80
#define  UART1_S4           0xC0
#define  CCP_S1             0x00
#define  CCP_S2             0x10
#define  CCP_S3             0x20
#define  CCP_S4             0x30
#define  SPI_S1             0x00
#define  SPI_S2             0x04
#define  SPI_S3             0x08
#define  SPI_S4             0x0C
SFR(VRTRIM,             0xA6);
#define  _IE            0xA8
SFR(IE,                 _IE);
SBIT(EA,                _IE, 7);
SBIT(ELVD,              _IE, 6);
SBIT(EADC,              _IE, 5);
SBIT(ES,                _IE, 4);
SBIT(ET1,               _IE, 3);
SBIT(EX1,               _IE, 2);
SBIT(ET0,               _IE, 1);
SBIT(EX0,               _IE, 0);
SFR(SADDR,              0xA9);
SFR(WKTCL,              0xAA);
SFR(WKTCH,              0xAB);
#define WKTEN               0x80

SFR(S3CON,              0xAC);
#define  S3SM0              0x80
#define  S3ST3              0x40
#define  S3SM2              0x20
#define  S3REN              0x10
#define  S3TB8              0x08
#define  S3RB8              0x04
#define  S3TI               0x02
#define  S3RI               0x01
SFR(S3BUF,              0xAD);
SFR(TA,                 0xAE);
SFR(IE2,                0xAF);
#define  ET4                0x40
#define  ET3                0x20
#define  ES4                0x10
#define  ES3                0x08
#define  ET2                0x04
#define  ESPI               0x02
#define  ES2                0x01

#define  _P3            0xB0
SFR(P3,                 _P3);
SBIT(P30,               _P3, 0);
SBIT(P31,               _P3, 1);
SBIT(P32,               _P3, 2);
SBIT(P33,               _P3, 3);
SBIT(P34,               _P3, 4);
SBIT(P35,               _P3, 5);
SBIT(P36,               _P3, 6);
SBIT(P37,               _P3, 7);
SFR(P3M1,               0xB1);
SFR(P3M0,               0xB2);
SFR(P4M1,               0xB3);
SFR(P4M0,               0xB4);
SFR(IP2,                0xB5);

#define  PI2C               0x40
#define  PCMP               0x20
#define  PX4                0x10
#define  PPWMFD             0x08
#define  PPWM               0x04
#define  PSPI               0x02
#define  PS2                0x01
SFR(IP2H,               0xB6);
#define  PI2CH              0x40
#define  PCMPH              0x20
#define  PX4H               0x10
#define  PPWMFDH            0x08
#define  PPWMH              0x04
#define  PSPIH              0x02
#define  PS2H               0x01
SFR(IPH,                0xB7);
#define  PPCAH              0x80
#define  PLVDH              0x40
#define  PADCH              0x20
#define  PSH                0x10
#define  PT1H               0x08
#define  PX1H               0x04
#define  PT0H               0x02
#define  PX0H               0x01

#define  _IP            0xB8
SFR(IP,                 _IP);
SBIT(PPCA,              _IP, 7);
SBIT(PLVD,              _IP, 6);
SBIT(PADC,              _IP, 5);
SBIT(PS,                _IP, 4);
SBIT(PT1,               _IP, 3);
SBIT(PX1,               _IP, 2);
SBIT(PT0,               _IP, 1);
SBIT(PX0,               _IP, 0);
SFR(SADEN,              0xB9);
SFR(P_SW2,              0xBA);
#define  EAXFR              0x80
#define  I2C_S1             0x00
#define  I2C_S2             0x10
#define  I2C_S3             0x20
#define  I2C_S4             0x30
#define  CMPO_S1            0x00
#define  CMPO_S2            0x08
#define  UART4_S1           0x00
#define  UART4_S2           0x04
#define  UART3_S1           0x00
#define  UART3_S2           0x02
#define  UART2_S1           0x00
#define  UART2_S2           0x01
SFR(VOCTRL,             0xBB);
SFR(ADC_CONTR,          0xBC);
#define  ADC_POWER          0x80
#define  ADC_START          0x40
#define  ADC_FLAG           0x20
#define  ADC_EPWMT          0x10
SFR(ADC_RES,            0xBD);
SFR(ADC_RESL,           0xBE);

#define  _P4            0xC0
SFR(P4,                 _P4);
SBIT(P40,               _P4, 0);
SBIT(P41,               _P4, 1);
SBIT(P42,               _P4, 2);
SBIT(P43,               _P4, 3);
SBIT(P44,               _P4, 4);
SBIT(P45,               _P4, 5);
SBIT(P46,               _P4, 6);
SBIT(P47,               _P4, 7);
SFR(WDT_CONTR,          0xC1);
#define  WDT_FLAG           0x80
#define  EN_WDT             0x20
#define  CLR_WDT            0x10
#define  IDL_WDT            0x08

SFR(IAP_DATA,           0xC2);
SFR(IAP_ADDRH,          0xC3);
SFR(IAP_ADDRL,          0xC4);
SFR(IAP_CMD,            0xC5);
#define  IAP_IDL            0x00
#define  IAP_READ           0x01
#define  IAP_WRITE          0x02
#define  IAP_ERASE          0x03
SFR(IAP_TRIG,           0xC6);
SFR(IAP_CONTR,          0xC7);
#define  IAPEN              0x80
#define  SWBS               0x40
#define  SWRST              0x20
#define  CMD_FAIL           0x10
#define  _P5            0xC8
SFR(P5,                 _P5);
SBIT(P50,               _P5, 0);
SBIT(P51,               _P5, 1);
SBIT(P52,               _P5, 2);
SBIT(P53,               _P5, 3);
SBIT(P54,               _P5, 4);
SBIT(P55,               _P5, 5);
SBIT(P56,               _P5, 6);
SBIT(P57,               _P5, 7);
SFR(P5M1,               0xC9);
SFR(P5M0,               0xCA);
SFR(P6M1,               0xCB);
SFR(P6M0,               0xCC);
SFR(SPSTAT,             0xCD);
#define  SPIF               0x80
#define  WCOL               0x40

SFR(SPCTL,              0xCE);
#define  SSIG               0x80
#define  SPEN               0x40
#define  DORD               0x20
#define  MSTR               0x10
#define  CPOL               0x08
#define  CPHA               0x04
SFR(SPDAT,              0xCF);
#define  _PSW           0xD0
SFR(PSW,                _PSW);
SBIT(CY,                _PSW, 7);
SBIT(AC,                _PSW, 6);
SBIT(F0,                _PSW, 5);
SBIT(RS1,               _PSW, 4);
SBIT(RS0,               _PSW, 3);
SBIT(OV,                _PSW, 2);

SBIT(P,                 _PSW, 0);
SFR(T4T3M,              0xD1);
#define  T4R                0x80
#define  T4_CT              0x40
#define  T4x12              0x20
#define  T4CLKO             0x10
#define  T3R                0x08
#define  T3_CT              0x04
#define  T3x12              0x02
#define  T3CLKO             0x01

SFR(T4H,                0xD2);
SFR(T4L,                0xD3);
SFR(T3H,                0xD4);
SFR(T3L,                0xD5);
SFR(T2H,                0xD6);
SFR(T2L,                0xD7);

#define  _CCON          0xD8
SFR(CCON,               _CCON);
SBIT(CF,                _CCON, 7);
SBIT(CR,                _CCON, 6);
SBIT(CCF3,              _CCON, 3);
SBIT(CCF2,              _CCON, 2);
SBIT(CCF1,              _CCON, 1);
SBIT(CCF0,              _CCON, 0);
SFR(CMOD,               0xD9);
#define  CIDL               0x80
#define  ECF                0x01
SFR(CCAPM0,             0xDA);
#define  ECOM0              0x40
#define  CCAPP0             0x20
#define  CCAPN0             0x10
#define  MAT0               0x08
#define  TOG0               0x04
#define  PWM0               0x02
#define  ECCF0              0x01

SFR(CCAPM1,             0xDB);
#define  ECOM1              0x40
#define  CCAPP1             0x20
#define  CCAPN1             0x10
#define  MAT1               0x08
#define  TOG1               0x04
#define  PWM1               0x02
#define  ECCF1              0x01
SFR(CCAPM2,             0xDC);
#define  ECOM2              0x40
#define  CCAPP2             0x20
#define  CCAPN2             0x10
#define  MAT2               0x08
#define  TOG2               0x04
#define  PWM2               0x02
#define  ECCF2              0x01

SFR(ADCCFG,             0xDE);
#define  ADC_RESFMT         0x20
SFR(IP3,                0xDF);
#define  PS4                0x02
#define  PS3                0x01
SFR(ACC,                0xE0);
SFR(P7M1,               0xE1);
SFR(P7M0,               0xE2);
SFR(DPS,                0xE3);
SFR(DPL1,               0xE4);
SFR(DPH1,               0xE5);
SFR(CMPCR1,             0xE6);
#define  CMPEN              0x80
#define  CMPIF              0x40
#define  PIE                0x20
#define  NIE                0x10
#define  CMPOE              0x02
#define  CMPRES             0x01
SFR(CMPCR2,             0xE7);
#define  INVCMPO            0x80
#define  DISFLT             0x40
#define  _P6            0xE8
SFR(P6,                 _P6);
SBIT(P60,               _P6, 0);
SBIT(P61,               _P6, 1);
SBIT(P62,               _P6, 2);
SBIT(P63,               _P6, 3);
SBIT(P64,               _P6, 4);
SBIT(P65,               _P6, 5);
SBIT(P66,               _P6, 6);
SBIT(P67,               _P6, 7);
SFR(CL,                 0xE9);
SFR(CCAP0L,             0xEA);
SFR(CCAP1L,             0xEB);
SFR(CCAP2L,             0xEC);
SFR(IP3H,               0xEE);
#define  PS4H               0x02
#define  PS3H               0x01
SFR(AUXINTIF,           0xEF);

#define  INT4IF             0x40
#define  INT3IF             0x20
#define  INT2IF             0x10
#define  T4IF               0x04
#define  T3IF               0x02
#define  T2IF               0x01
SFR(B,                  0xF0);
SFR(PWMSET,             0xF1);
#define  PWMRST             0x40
#define  ENPWM              0x01
SFR(PCA_PWM0,           0xF2);
SFR(PCA_PWM1,           0xF3);
SFR(PCA_PWM2,           0xF4);
SFR(IAP_TPS,            0xF5);
SFR(PWMCFG,             0xF6);
#define  PWMCBIF            0x08
#define  PWMCBIE            0x04
#define  PWMETA             0x02
#define  PWMCEN             0x01

#define  _P7            0xF8
SFR(P7,                 _P7);
SBIT(P70,               _P7, 0);
SBIT(P71,               _P7, 1);
SBIT(P72,               _P7, 2);
SBIT(P73,               _P7, 3);
SBIT(P74,               _P7, 4);
SBIT(P75,               _P7, 5);
SBIT(P76,               _P7, 6);
SBIT(P77,               _P7, 7);
SFR(CH,                 0xF9);
SFR(CCAP0H,             0xFA);
SFR(CCAP1H,             0xFB);
SFR(CCAP2H,             0xFC);
SFR(RSTCFG,             0xFF);
#define  ENLVR          0x40
#define  P54RST         0x10
#define  LVD_S1         0x00
#define  LVD_S2         0x01
#define  LVD_S3         0x02
#define  LVD_S4         0x03

//如下特殊功能寄存器位于扩展RAM区域
//访问这些寄存器,需先将P_SW2的BIT7设置为1,才可正常读写

/////////////////////////////////////////////////
//FF00H-FFFFH
/////////////////////////////////////////////////

#define     PWMC                    (*(unsigned int  volatile xdata *)0xff00)
#define     PWMCH                   (*(unsigned char volatile xdata *)0xff00)
#define     PWMCL                   (*(unsigned char volatile xdata *)0xff01)
#define     PWMCKS                  (*(unsigned char volatile xdata *)0xff02)
#define     PWM_SELT2               0x10
#define     PWMTADC                 (*(unsigned int  volatile xdata *)0xff03)
#define     PWMTADCH                (*(unsigned char volatile xdata *)0xff03)
#define     PWMTADCL                (*(unsigned char volatile xdata *)0xff04)
#define     PWMIF                   (*(unsigned char volatile xdata *)0xff05)
#define     PWM_C7IF                0x80
#define     PWM_C6IF                0x40
#define     PWM_C5IF                0x20
#define     PWM_C4IF                0x10
#define     PWM_C3IF                0x08
#define     PWM_C2IF                0x04
#define     PWM_C1IF                0x02
#define     PWM_C0IF                0x01
#define     PWMFDCR                 (*(unsigned char volatile xdata *)0xff06)
#define     PWMFD_INVCMP            0x80
#define     PWMFD_INVIO             0x40
#define     PWMFD_ENFD              0x20
#define     PWMFD_FLTFLIO           0x10
#define     PWMFD_EFDI              0x08
#define     PWMFD_FDCMP             0x04
#define     PWMFD_FDIO              0x02
#define     PWMFD_FDIF              0x01
#define     PWMDELSEL               (*(unsigned char volatile xdata *)0xff07)
#define     PWM_CH03FULL            0x00
#define     PWM_CH03HALF            0x01
#define     PWM_CH03NONE            0x02
#define     PWM_CH47FULL            0x00
#define     PWM_CH47HALF            0x04
#define     PWM_CH47NONE            0x08
#define     PWM0T1                  (*(unsigned int  volatile xdata *)0xff10)
#define     PWM0T1H                 (*(unsigned char volatile xdata *)0xff10)
#define     PWM0T1L                 (*(unsigned char volatile xdata *)0xff11)
#define     PWM0T2                  (*(unsigned int  volatile xdata *)0xff12)
#define     PWM0T2H                 (*(unsigned char volatile xdata *)0xff12)
#define     PWM0T2L                 (*(unsigned char volatile xdata *)0xff13)
#define     PWM0CR                  (*(unsigned char volatile xdata *)0xff14)
#define     PWM_ENO                 0x80
#define     PWM_INI0                0x00
#define     PWM_INI1                0x40
#define     PWM_ENI                 0x04
#define     PWM_ENT2I               0x02
#define     PWM_ENT1I               0x01
#define     PWM0HLD                 (*(unsigned char volatile xdata *)0xff15)
#define     PWM_HLDH                0x02
#define     PWM_HLDL                0x01
#define     PWM1T1                  (*(unsigned int  volatile xdata *)0xff18)
#define     PWM1T1H                 (*(unsigned char volatile xdata *)0xff18)
#define     PWM1T1L                 (*(unsigned char volatile xdata *)0xff19)
#define     PWM1T2                  (*(unsigned int  volatile xdata *)0xff1a)
#define     PWM1T2H                 (*(unsigned char volatile xdata *)0xff1a)
#define     PWM1T2L                 (*(unsigned char volatile xdata *)0xff1b)
#define     PWM1CR                  (*(unsigned char volatile xdata *)0xff1c)
#define     PWM1HLD                 (*(unsigned char volatile xdata *)0xff1d)
#define     PWM2T1                  (*(unsigned int  volatile xdata *)0xff20)
#define     PWM2T1H                 (*(unsigned char volatile xdata *)0xff20)
#define     PWM2T1L                 (*(unsigned char volatile xdata *)0xff21)
#define     PWM2T2                  (*(unsigned int  volatile xdata *)0xff22)
#define     PWM2T2H                 (*(unsigned char volatile xdata *)0xff22)
#define     PWM2T2L                 (*(unsigned char volatile xdata *)0xff23)
#define     PWM2CR                  (*(unsigned char volatile xdata *)0xff24)
#define     PWM2HLD                 (*(unsigned char volatile xdata *)0xff25)
#define     PWM3T1                  (*(unsigned int  volatile xdata *)0xff28)
#define     PWM3T1H                 (*(unsigned char volatile xdata *)0xff28)
#define     PWM3T1L                 (*(unsigned char volatile xdata *)0xff29)
#define     PWM3T2                  (*(unsigned int  volatile xdata *)0xff2a)
#define     PWM3T2H                 (*(unsigned char volatile xdata *)0xff2a)
#define     PWM3T2L                 (*(unsigned char volatile xdata *)0xff2b)
#define     PWM3CR                  (*(unsigned char volatile xdata *)0xff2c)
#define     PWM3HLD                 (*(unsigned char volatile xdata *)0xff2d)
#define     PWM4T1                  (*(unsigned int  volatile xdata *)0xff30)
#define     PWM4T1H                 (*(unsigned char volatile xdata *)0xff30)
#define     PWM4T1L                 (*(unsigned char volatile xdata *)0xff31)
#define     PWM4T2                  (*(unsigned int  volatile xdata *)0xff32)
#define     PWM4T2H                 (*(unsigned char volatile xdata *)0xff32)
#define     PWM4T2L                 (*(unsigned char volatile xdata *)0xff33)
#define     PWM4CR                  (*(unsigned char volatile xdata *)0xff34)
#define     PWM4HLD                 (*(unsigned char volatile xdata *)0xff35)
#define     PWM5T1                  (*(unsigned int  volatile xdata *)0xff38)
#define     PWM5T1H                 (*(unsigned char volatile xdata *)0xff38)
#define     PWM5T1L                 (*(unsigned char volatile xdata *)0xff39)
#define     PWM5T2                  (*(unsigned int  volatile xdata *)0xff3a)
#define     PWM5T2H                 (*(unsigned char volatile xdata *)0xff3a)
#define     PWM5T2L                 (*(unsigned char volatile xdata *)0xff3b)
#define     PWM5CR                  (*(unsigned char volatile xdata *)0xff3c)
#define     PWM5HLD                 (*(unsigned char volatile xdata *)0xff3d)
#define     PWM6T1                  (*(unsigned int  volatile xdata *)0xff40)
#define     PWM6T1H                 (*(unsigned char volatile xdata *)0xff40)
#define     PWM6T1L                 (*(unsigned char volatile xdata *)0xff41)
#define     PWM6T2                  (*(unsigned int  volatile xdata *)0xff42)
#define     PWM6T2H                 (*(unsigned char volatile xdata *)0xff42)
#define     PWM6T2L                 (*(unsigned char volatile xdata *)0xff43)
#define     PWM6CR                  (*(unsigned char volatile xdata *)0xff44)
#define     PWM6HLD                 (*(unsigned char volatile xdata *)0xff45)
#define     PWM7T1                  (*(unsigned int  volatile xdata *)0xff48)
#define     PWM7T1H                 (*(unsigned char volatile xdata *)0xff48)
#define     PWM7T1L                 (*(unsigned char volatile xdata *)0xff49)
#define     PWM7T2                  (*(unsigned int  volatile xdata *)0xff4a)
#define     PWM7T2H                 (*(unsigned char volatile xdata *)0xff4a)
#define     PWM7T2L                 (*(unsigned char volatile xdata *)0xff4b)
#define     PWM7CR                  (*(unsigned char volatile xdata *)0xff4c)
#define     PWM7HLD                 (*(unsigned char volatile xdata *)0xff4d)

/////////////////////////////////////////////////
//FE00H-FEFFH
/////////////////////////////////////////////////

#define     CKSEL                   (*(unsigned char volatile xdata *)0xfe00)
#define     MCK_IRC24M              0x00
#define     MCK_XOSC                0x01
#define     MCK_IRC32K              0x03
#define     CLKDIV                  (*(unsigned char volatile xdata *)0xfe01)
#define     HIRCCR                  (*(unsigned char volatile xdata *)0xfe02)
#define     ENHIRC                  0x80
#define     HIRCST                  0x01
#define     XOSCCR                  (*(unsigned char volatile xdata *)0xfe03)
#define     ENXOSC                  0x80
#define     XITYPE                  0x40
#define     XOSCST                  0x01
#define     IRC32KCR                (*(unsigned char volatile xdata *)0xfe04)
#define     ENIRC32K                0x80
#define     IRC32KST                0x01
#define     MCLKOCR                 (*(unsigned char volatile xdata *)0xfe05)
#define     MCLKO_S                 0x80
#define     IRCDB                   (*(unsigned char volatile xdata *)0xfe06)

#define     P0PU                    (*(unsigned char volatile xdata *)0xfe10)
#define     P1PU                    (*(unsigned char volatile xdata *)0xfe11)
#define     P2PU                    (*(unsigned char volatile xdata *)0xfe12)
#define     P3PU                    (*(unsigned char volatile xdata *)0xfe13)
#define     P4PU                    (*(unsigned char volatile xdata *)0xfe14)
#define     P5PU                    (*(unsigned char volatile xdata *)0xfe15)
#define     P6PU                    (*(unsigned char volatile xdata *)0xfe16)
#define     P7PU                    (*(unsigned char volatile xdata *)0xfe17)
#define     P0NCS                   (*(unsigned char volatile xdata *)0xfe18)
#define     P1NCS                   (*(unsigned char volatile xdata *)0xfe19)
#define     P2NCS                   (*(unsigned char volatile xdata *)0xfe1a)
#define     P3NCS                   (*(unsigned char volatile xdata *)0xfe1b)
#define     P4NCS                   (*(unsigned char volatile xdata *)0xfe1c)
#define     P5NCS                   (*(unsigned char volatile xdata *)0xfe1d)
#define     P6NCS                   (*(unsigned char volatile xdata *)0xfe1e)
#define     P7NCS                   (*(unsigned char volatile xdata *)0xfe1f)
#define     P0SR                    (*(unsigned char volatile xdata *)0xfe20)
#define     P1SR                    (*(unsigned char volatile xdata *)0xfe21)
#define     P2SR                    (*(unsigned char volatile xdata *)0xfe22)
#define     P3SR                    (*(unsigned char volatile xdata *)0xfe23)
#define     P4SR                    (*(unsigned char volatile xdata *)0xfe24)
#define     P5SR                    (*(unsigned char volatile xdata *)0xfe25)
#define     P6SR                    (*(unsigned char volatile xdata *)0xfe26)
#define     P7SR                    (*(unsigned char volatile xdata *)0xfe27)
#define     P0DR                    (*(unsigned char volatile xdata *)0xfe28)
#define     P1DR                    (*(unsigned char volatile xdata *)0xfe29)
#define     P2DR                    (*(unsigned char volatile xdata *)0xfe2a)
#define     P3DR                    (*(unsigned char volatile xdata *)0xfe2b)
#define     P4DR                    (*(unsigned char volatile xdata *)0xfe2c)
#define     P5DR                    (*(unsigned char volatile xdata *)0xfe2d)
#define     P6DR                    (*(unsigned char volatile xdata *)0xfe2e)
#define     P7DR                    (*(unsigned char volatile xdata *)0xfe2f)
#define     P0IE                    (*(unsigned char volatile xdata *)0xfe30)
#define     P1IE                    (*(unsigned char volatile xdata *)0xfe31)
#define     P2IE                    (*(unsigned char volatile xdata *)0xfe32)
#define     P3IE                    (*(unsigned char volatile xdata *)0xfe33)
#define     P4IE                    (*(unsigned char volatile xdata *)0xfe34)
#define     P5IE                    (*(unsigned char volatile xdata *)0xfe35)
#define     P6IE                    (*(unsigned char volatile xdata *)0xfe36)
#define     P7IE                    (*(unsigned char volatile xdata *)0xfe37)
                                    
#define     LCMIFCFG                (*(unsigned char volatile xdata *)0xfe50)
#define     LCMIFCFG2               (*(unsigned char volatile xdata *)0xfe51)
#define     LCMIFCR                 (*(unsigned char volatile xdata *)0xfe52)
#define     LCMIFSTA                (*(unsigned char volatile xdata *)0xfe53)
#define     LCMIFDATL               (*(unsigned char volatile xdata *)0xfe54)
#define     LCMIFDATH               (*(unsigned char volatile xdata *)0xfe55)
                                    
#define     I2CCFG                  (*(unsigned char volatile xdata *)0xfe80)
#define     ENI2C                   0x80
#define     I2CMASTER               0x40
#define     I2CSLAVE                0x00
#define     I2CMSCR                 (*(unsigned char volatile xdata *)0xfe81)
#define     EMSI                    0x80
#define     MS_IDLE                     0x00
#define     MS_START                    0x01
#define     MS_SENDDAT                  0x02
#define     MS_RECVACK                  0x03
#define     MS_RECVDAT                  0x04
#define     MS_SENDACK                  0x05
#define     MS_STOP                     0x06
#define     MS_START_SENDDAT_RECVACK    0x09
#define     MS_SENDDAT_RECVACK          0x0a
#define     MS_RECVDAT_SENDACK          0x0b
#define     MS_RECVDAT_SENDNAK          0x0c
#define     I2CMSST                 (*(unsigned char volatile xdata *)0xfe82)
#define     MSBUSY                  0x80
#define     MSIF                    0x40
#define     MSACKI                  0x02
#define     MSACKO                  0x01
#define     I2CSLCR                 (*(unsigned char volatile xdata *)0xfe83)
#define     ESTAI                   0x40
#define     ERXI                    0x20
#define     ETXI                    0x10
#define     ESTOI                   0x08
#define     SLRST                   0x01
#define     I2CSLST                 (*(unsigned char volatile xdata *)0xfe84)
#define     SLBUSY                  0x80
#define     STAIF                   0x40
#define     RXIF                    0x20
#define     TXIF                    0x10
#define     STOIF                   0x08
#define     TXING                   0x04
#define     SLACKI                  0x02
#define     SLACKO                  0x01
#define     I2CSLADR                (*(unsigned char volatile xdata *)0xfe85)
#define     I2CTXD                  (*(unsigned char volatile xdata *)0xfe86)
#define     I2CRXD                  (*(unsigned char volatile xdata *)0xfe87)
#define     I2CMSAUX                (*(unsigned char volatile xdata *)0xfe88)
#define     WDTA                    0x01
                                    
#define     TM2PS                   (*(unsigned char volatile xdata *)0xfea2)
#define     TM3PS                   (*(unsigned char volatile xdata *)0xfea3)
#define     TM4PS                   (*(unsigned char volatile xdata *)0xfea4)
#define     ADCTIM                  (*(unsigned char volatile xdata *)0xfea8)
#define     ADCEXCFG                (*(unsigned char volatile xdata *)0xfead)
#define     CMPEXCFG                (*(unsigned char volatile xdata *)0xfeae)

/////////////////////////////////////////////////
//FD00H-FDFFH
/////////////////////////////////////////////////

#define     P0INTE                  (*(unsigned char volatile xdata *)0xfd00)
#define     P1INTE                  (*(unsigned char volatile xdata *)0xfd01)
#define     P2INTE                  (*(unsigned char volatile xdata *)0xfd02)
#define     P3INTE                  (*(unsigned char volatile xdata *)0xfd03)
#define     P4INTE                  (*(unsigned char volatile xdata *)0xfd04)
#define     P5INTE                  (*(unsigned char volatile xdata *)0xfd05)
#define     P6INTE                  (*(unsigned char volatile xdata *)0xfd06)
#define     P7INTE                  (*(unsigned char volatile xdata *)0xfd07)
#define     P0INTF                  (*(unsigned char volatile xdata *)0xfd10)
#define     P1INTF                  (*(unsigned char volatile xdata *)0xfd11)
#define     P2INTF                  (*(unsigned char volatile xdata *)0xfd12)
#define     P3INTF                  (*(unsigned char volatile xdata *)0xfd13)
#define     P4INTF                  (*(unsigned char volatile xdata *)0xfd14)
#define     P5INTF                  (*(unsigned char volatile xdata *)0xfd15)
#define     P6INTF                  (*(unsigned char volatile xdata *)0xfd16)
#define     P7INTF                  (*(unsigned char volatile xdata *)0xfd17)
#define     P0IM0                   (*(unsigned char volatile xdata *)0xfd20)
#define     P1IM0                   (*(unsigned char volatile xdata *)0xfd21)
#define     P2IM0                   (*(unsigned char volatile xdata *)0xfd22)
#define     P3IM0                   (*(unsigned char volatile xdata *)0xfd23)
#define     P4IM0                   (*(unsigned char volatile xdata *)0xfd24)
#define     P5IM0                   (*(unsigned char volatile xdata *)0xfd25)
#define     P6IM0                   (*(unsigned char volatile xdata *)0xfd26)
#define     P7IM0                   (*(unsigned char volatile xdata *)0xfd27)
#define     P0IM1                   (*(unsigned char volatile xdata *)0xfd30)
#define     P1IM1                   (*(unsigned char volatile xdata *)0xfd31)
#define     P2IM1                   (*(unsigned char volatile xdata *)0xfd32)
#define     P3IM1                   (*(unsigned char volatile xdata *)0xfd33)
#define     P4IM1                   (*(unsigned char volatile xdata *)0xfd34)
#define     P5IM1                   (*(unsigned char volatile xdata *)0xfd35)
#define     P6IM1                   (*(unsigned char volatile xdata *)0xfd36)
#define     P7IM1                   (*(unsigned char volatile xdata *)0xfd37)
#define     P0WKUE                  (*(unsigned char volatile xdata *)0xfd40)
#define     P1WKUE                  (*(unsigned char volatile xdata *)0xfd41)
#define     P2WKUE                  (*(unsigned char volatile xdata *)0xfd42)
#define     P3WKUE                  (*(unsigned char volatile xdata *)0xfd43)
#define     P4WKUE                  (*(unsigned char volatile xdata *)0xfd44)
#define     P5WKUE                  (*(unsigned char volatile xdata *)0xfd45)
#define     P6WKUE                  (*(unsigned char volatile xdata *)0xfd46)
#define     P7WKUE                  (*(unsigned char volatile xdata *)0xfd47)
                                    
#define     CCAPM3                  (*(unsigned char volatile xdata *)0xfd54)
#define     CCAP3L                  (*(unsigned char volatile xdata *)0xfd55)
#define     CCAP3H                  (*(unsigned char volatile xdata *)0xfd56)
#define     PCA_PWM3                (*(unsigned char volatile xdata *)0xfd57)
                                    
#define     PIN_IP                  (*(unsigned char volatile xdata *)0xfd60)
#define     PIN_IPH                 (*(unsigned char volatile xdata *)0xfd61)

#define     CHIPID0                 (*(unsigned char volatile xdata *)0xfde0) // ID_ADDR
#define     CHIPID1                 (*(unsigned char volatile xdata *)0xfde1)
#define     CHIPID2                 (*(unsigned char volatile xdata *)0xfde2)
#define     CHIPID3                 (*(unsigned char volatile xdata *)0xfde3)
#define     CHIPID4                 (*(unsigned char volatile xdata *)0xfde4)
#define     CHIPID5                 (*(unsigned char volatile xdata *)0xfde5)
#define     CHIPID6                 (*(unsigned char volatile xdata *)0xfde6)
#define     CHIPID7                 (*(unsigned char volatile xdata *)0xfde7) // VREF_ADDR
#define     CHIPID8                 (*(unsigned char volatile xdata *)0xfde8)
#define     CHIPID9                 (*(unsigned char volatile xdata *)0xfde9) // F32K_ADDR
#define     CHIPID10                (*(unsigned char volatile xdata *)0xfdea)
#define     CHIPID11                (*(unsigned char volatile xdata *)0xfdeb) // T22M_ADDR
#define     CHIPID12                (*(unsigned char volatile xdata *)0xfdec) // T24M_ADDR
#define     CHIPID13                (*(unsigned char volatile xdata *)0xfded) // T20M_ADDR
#define     CHIPID14                (*(unsigned char volatile xdata *)0xfdee) // T27M_ADDR
#define     CHIPID15                (*(unsigned char volatile xdata *)0xfdef) // T30M_ADDR
#define     CHIPID16                (*(unsigned char volatile xdata *)0xfdf0) // T33M_ADDR
#define     CHIPID17                (*(unsigned char volatile xdata *)0xfdf1) // T35M_ADDR
#define     CHIPID18                (*(unsigned char volatile xdata *)0xfdf2) // T36M_ADDR
#define     CHIPID19                (*(unsigned char volatile xdata *)0xfdf3) // T40M_ADDR
#define     CHIPID20                (*(unsigned char volatile xdata *)0xfdf4) // T45M_ADDR
#define     CHIPID21                (*(unsigned char volatile xdata *)0xfdf5) // VRT6M_ADDR
#define     CHIPID22                (*(unsigned char volatile xdata *)0xfdf6) // VRT10M_ADDR
#define     CHIPID23                (*(unsigned char volatile xdata *)0xfdf7) // VRT27M_ADDR
#define     CHIPID24                (*(unsigned char volatile xdata *)0xfdf8) // VRT44M_ADDR
#define     CHIPID25                (*(unsigned char volatile xdata *)0xfdf9)
#define     CHIPID26                (*(unsigned char volatile xdata *)0xfdfa)
#define     CHIPID27                (*(unsigned char volatile xdata *)0xfdfb)
#define     CHIPID28                (*(unsigned char volatile xdata *)0xfdfc)
#define     CHIPID29                (*(unsigned char volatile xdata *)0xfdfd)
#define     CHIPID30                (*(unsigned char volatile xdata *)0xfdfe)
#define     CHIPID31                (*(unsigned char volatile xdata *)0xfdff)

SFRX(ID_ADDR,           0xfde0);
SFRX(VREF_ADDR,         0xfde7);
SFRX(F32K_ADDR,         0xfde9);
SFRX(T22M_ADDR,         0xfdeb); // 22.1184MHz
SFRX(T24M_ADDR,         0xfdec); // 24MHz
SFRX(T20M_ADDR,         0xfded); // 20MHz
SFRX(T27M_ADDR,         0xfdee); // 27MHz
SFRX(T30M_ADDR,         0xfdef); // 30MHz
SFRX(T33M_ADDR,         0xfdf0); // 33.1776MHz
SFRX(T35M_ADDR,         0xfdf1); // 35MHz
SFRX(T36M_ADDR,         0xfdf2); // 36.864MHz
SFRX(T40M_ADDR,         0xfdf3); // 40MHz
SFRX(T45M_ADDR,         0xfdf4); // 45MHz
SFRX(VRT6M_ADDR,        0xfdf5); // VRTRIM_6M
SFRX(VRT10M_ADDR,       0xfdf6); // VRTRIM_10M
SFRX(VRT27M_ADDR,       0xfdf7); // VRTRIM_27M
SFRX(VRT44M_ADDR,       0xfdf8); // VRTRIM_44M


/////////////////////////////////////////////////
//FC00H-FCFFH
/////////////////////////////////////////////////

#define     MD3                     (*(unsigned char volatile xdata *)0xfcf0)
#define     MD2                     (*(unsigned char volatile xdata *)0xfcf1)
#define     MD1                     (*(unsigned char volatile xdata *)0xfcf2)
#define     MD0                     (*(unsigned char volatile xdata *)0xfcf3)
#define     MD5                     (*(unsigned char volatile xdata *)0xfcf4)
#define     MD4                     (*(unsigned char volatile xdata *)0xfcf5)
#define     dwOP1                   (*(unsigned long volatile xdata *)0xfcf0)
#define     wOP1                    (*(unsigned int  volatile xdata *)0xfcf2)
#define     wOP2                    (*(unsigned int  volatile xdata *)0xfcf4)
#define     ARCON                   (*(unsigned char volatile xdata *)0xfcf6)
#define     MDU16_OP_RSHIFT         (1 << 5)
#define     MDU16_OP_LSHIFT         (2 << 5)
#define     MDU16_OP_NORMALIZE      (3 << 5)
#define     MDU16_OP_16MUL16        (4 << 5)
#define     MDU16_OP_16DIV16        (5 << 5)
#define     MDU16_OP_32DIV16        (6 << 5)
#define     OPCON                   (*(unsigned char volatile xdata *)0xfcf7)
#define     MDU16_START             0x01
#define     MDU16_BUSY              0x01
#define     MDU16_RESET             0x02

/////////////////////////////////////////////////
//FB00H-FBFFH
/////////////////////////////////////////////////


/////////////////////////////////////////////////
//FA00H-FAFFH
/////////////////////////////////////////////////

#define     BMM_M2M_CFG             (*(unsigned char volatile xdata *)0xfa00)
#define     BMM_M2M_CR              (*(unsigned char volatile xdata *)0xfa01)
#define     BMM_M2M_STA             (*(unsigned char volatile xdata *)0xfa02)
#define     BMM_M2M_AMT             (*(unsigned char volatile xdata *)0xfa03)
#define     BMM_M2M_DONE            (*(unsigned char volatile xdata *)0xfa04)
#define     BMM_M2M_TXA             (*(unsigned  int volatile xdata *)0xfa05)
#define     BMM_M2M_TXAH            (*(unsigned char volatile xdata *)0xfa05)
#define     BMM_M2M_TXAL            (*(unsigned char volatile xdata *)0xfa06)
#define     BMM_M2M_RXA             (*(unsigned  int volatile xdata *)0xfa07)
#define     BMM_M2M_RXAH            (*(unsigned char volatile xdata *)0xfa07)
#define     BMM_M2M_RXAL            (*(unsigned char volatile xdata *)0xfa08)
                                    
#define     BMM_ADC_CFG             (*(unsigned char volatile xdata *)0xfa10)
#define     BMM_ADC_CR              (*(unsigned char volatile xdata *)0xfa11)
#define     BMM_ADC_STA             (*(unsigned char volatile xdata *)0xfa12)
#define     BMM_ADC_RXA             (*(unsigned  int volatile xdata *)0xfa17)
#define     BMM_ADC_RXAH            (*(unsigned char volatile xdata *)0xfa17)
#define     BMM_ADC_RXAL            (*(unsigned char volatile xdata *)0xfa18)
#define     BMM_ADC_CFG2            (*(unsigned char volatile xdata *)0xfa19)
#define     BMM_ADC_CHSW0           (*(unsigned char volatile xdata *)0xfa1a)
#define     BMM_ADC_CHSW1           (*(unsigned char volatile xdata *)0xfa1b)
                                    
#define     BMM_SPI_CFG             (*(unsigned char volatile xdata *)0xfa20)
#define     BMM_SPI_CR              (*(unsigned char volatile xdata *)0xfa21)
#define     BMM_SPI_STA             (*(unsigned char volatile xdata *)0xfa22)
#define     BMM_SPI_AMT             (*(unsigned char volatile xdata *)0xfa23)
#define     BMM_SPI_DONE            (*(unsigned char volatile xdata *)0xfa24)
#define     BMM_SPI_TXA             (*(unsigned  int volatile xdata *)0xfa25)
#define     BMM_SPI_TXAH            (*(unsigned char volatile xdata *)0xfa25)
#define     BMM_SPI_TXAL            (*(unsigned char volatile xdata *)0xfa26)
#define     BMM_SPI_RXA             (*(unsigned  int volatile xdata *)0xfa27)
#define     BMM_SPI_RXAH            (*(unsigned char volatile xdata *)0xfa27)
#define     BMM_SPI_RXAL            (*(unsigned char volatile xdata *)0xfa28)
#define     BMM_SPI_CFG2            (*(unsigned char volatile xdata *)0xfa29)
                                    
#define     BMM_UR1T_CFG            (*(unsigned char volatile xdata *)0xfa30)
#define     BMM_UR1T_CR             (*(unsigned char volatile xdata *)0xfa31)
#define     BMM_UR1T_STA            (*(unsigned char volatile xdata *)0xfa32)
#define     BMM_UR1T_AMT            (*(unsigned char volatile xdata *)0xfa33)
#define     BMM_UR1T_DONE           (*(unsigned char volatile xdata *)0xfa34)
#define     BMM_UR1T_TXA            (*(unsigned  int volatile xdata *)0xfa35)
#define     BMM_UR1T_TXAH           (*(unsigned char volatile xdata *)0xfa35)
#define     BMM_UR1T_TXAL           (*(unsigned char volatile xdata *)0xfa36)
#define     BMM_UR1R_CFG            (*(unsigned char volatile xdata *)0xfa38)
#define     BMM_UR1R_CR             (*(unsigned char volatile xdata *)0xfa39)
#define     BMM_UR1R_STA            (*(unsigned char volatile xdata *)0xfa3a)
#define     BMM_UR1R_AMT            (*(unsigned char volatile xdata *)0xfa3b)
#define     BMM_UR1R_DONE           (*(unsigned char volatile xdata *)0xfa3c)
#define     BMM_UR1R_RXA            (*(unsigned  int volatile xdata *)0xfa3d)
#define     BMM_UR1R_RXAH           (*(unsigned char volatile xdata *)0xfa3d)
#define     BMM_UR1R_RXAL           (*(unsigned char volatile xdata *)0xfa3e)
                                    
#define     BMM_UR2T_CFG            (*(unsigned char volatile xdata *)0xfa40)
#define     BMM_UR2T_CR             (*(unsigned char volatile xdata *)0xfa41)
#define     BMM_UR2T_STA            (*(unsigned char volatile xdata *)0xfa42)
#define     BMM_UR2T_AMT            (*(unsigned char volatile xdata *)0xfa43)
#define     BMM_UR2T_DONE           (*(unsigned char volatile xdata *)0xfa44)
#define     BMM_UR2T_TXA            (*(unsigned  int volatile xdata *)0xfa45)
#define     BMM_UR2T_TXAH           (*(unsigned char volatile xdata *)0xfa45)
#define     BMM_UR2T_TXAL           (*(unsigned char volatile xdata *)0xfa46)
#define     BMM_UR2R_CFG            (*(unsigned char volatile xdata *)0xfa48)
#define     BMM_UR2R_CR             (*(unsigned char volatile xdata *)0xfa49)
#define     BMM_UR2R_STA            (*(unsigned char volatile xdata *)0xfa4a)
#define     BMM_UR2R_AMT            (*(unsigned char volatile xdata *)0xfa4b)
#define     BMM_UR2R_DONE           (*(unsigned char volatile xdata *)0xfa4c)
#define     BMM_UR2R_RXA            (*(unsigned  int volatile xdata *)0xfa4d)
#define     BMM_UR2R_RXAH           (*(unsigned char volatile xdata *)0xfa4d)
#define     BMM_UR2R_RXAL           (*(unsigned char volatile xdata *)0xfa4e)
                                    
#define     BMM_UR3T_CFG            (*(unsigned char volatile xdata *)0xfa50)
#define     BMM_UR3T_CR             (*(unsigned char volatile xdata *)0xfa51)
#define     BMM_UR3T_STA            (*(unsigned char volatile xdata *)0xfa52)
#define     BMM_UR3T_AMT            (*(unsigned char volatile xdata *)0xfa53)
#define     BMM_UR3T_DONE           (*(unsigned char volatile xdata *)0xfa54)
#define     BMM_UR3T_TXA            (*(unsigned  int volatile xdata *)0xfa55)
#define     BMM_UR3T_TXAH           (*(unsigned char volatile xdata *)0xfa55)
#define     BMM_UR3T_TXAL           (*(unsigned char volatile xdata *)0xfa56)
#define     BMM_UR3R_CFG            (*(unsigned char volatile xdata *)0xfa58)
#define     BMM_UR3R_CR             (*(unsigned char volatile xdata *)0xfa59)
#define     BMM_UR3R_STA            (*(unsigned char volatile xdata *)0xfa5a)
#define     BMM_UR3R_AMT            (*(unsigned char volatile xdata *)0xfa5b)
#define     BMM_UR3R_DONE           (*(unsigned char volatile xdata *)0xfa5c)
#define     BMM_UR3R_RXA            (*(unsigned  int volatile xdata *)0xfa5d)
#define     BMM_UR3R_RXAH           (*(unsigned char volatile xdata *)0xfa5d)
#define     BMM_UR3R_RXAL           (*(unsigned char volatile xdata *)0xfa5e)
                                    
#define     BMM_UR4T_CFG            (*(unsigned char volatile xdata *)0xfa60)
#define     BMM_UR4T_CR             (*(unsigned char volatile xdata *)0xfa61)
#define     BMM_UR4T_STA            (*(unsigned char volatile xdata *)0xfa62)
#define     BMM_UR4T_AMT            (*(unsigned char volatile xdata *)0xfa63)
#define     BMM_UR4T_DONE           (*(unsigned char volatile xdata *)0xfa64)
#define     BMM_UR4T_TXA            (*(unsigned  int volatile xdata *)0xfa65)
#define     BMM_UR4T_TXAH           (*(unsigned char volatile xdata *)0xfa65)
#define     BMM_UR4T_TXAL           (*(unsigned char volatile xdata *)0xfa66)
#define     BMM_UR4R_CFG            (*(unsigned char volatile xdata *)0xfa68)
#define     BMM_UR4R_CR             (*(unsigned char volatile xdata *)0xfa69)
#define     BMM_UR4R_STA            (*(unsigned char volatile xdata *)0xfa6a)
#define     BMM_UR4R_AMT            (*(unsigned char volatile xdata *)0xfa6b)
#define     BMM_UR4R_DONE           (*(unsigned char volatile xdata *)0xfa6c)
#define     BMM_UR4R_RXA            (*(unsigned  int volatile xdata *)0xfa6d)
#define     BMM_UR4R_RXAH           (*(unsigned char volatile xdata *)0xfa6d)
#define     BMM_UR4R_RXAL           (*(unsigned char volatile xdata *)0xfa6e)
                                    
#define     BMM_LCM_CFG             (*(unsigned char volatile xdata *)0xfa70)
#define     BMM_LCM_CR              (*(unsigned char volatile xdata *)0xfa71)
#define     BMM_LCM_STA             (*(unsigned char volatile xdata *)0xfa72)
#define     BMM_LCM_AMT             (*(unsigned char volatile xdata *)0xfa73)
#define     BMM_LCM_DONE            (*(unsigned char volatile xdata *)0xfa74)
#define     BMM_LCM_TXA             (*(unsigned  int volatile xdata *)0xfa75)
#define     BMM_LCM_TXAH            (*(unsigned char volatile xdata *)0xfa75)
#define     BMM_LCM_TXAL            (*(unsigned char volatile xdata *)0xfa76)
#define     BMM_LCM_RXA             (*(unsigned  int volatile xdata *)0xfa77)
#define     BMM_LCM_RXAH            (*(unsigned char volatile xdata *)0xfa77)
#define     BMM_LCM_RXAL            (*(unsigned char volatile xdata *)0xfa78)


/////////////////////////////////////////////////

#define     INT0_VECTOR             0       //0003H
#define     TMR0_VECTOR             1       //000BH
#define     INT1_VECTOR             2       //0013H
#define     TMR1_VECTOR             3       //001BH
#define     UART1_VECTOR            4       //0023H
#define     ADC_VECTOR              5       //002BH
#define     LVD_VECTOR              6       //0033H
#define     PCA_VECTOR              7       //003BH
#define     UART2_VECTOR            8       //0043H
#define     SPI_VECTOR              9       //004BH
#define     INT2_VECTOR             10      //0053H
#define     INT3_VECTOR             11      //005BH
#define     TMR2_VECTOR             12      //0063H
#define     USER_VECTOR             13      //006BH
#define     INT4_VECTOR             16      //0083H
#define     UART3_VECTOR            17      //008BH
#define     UART4_VECTOR            18      //0093H
#define     TMR3_VECTOR             19      //009BH
#define     TMR4_VECTOR             20      //00A3H
#define     CMP_VECTOR              21      //00ABH
#define     PWM_VECTOR              22      //00B3H
#define     PWMFD_VECTOR            23      //00BBH
#define     I2C_VECTOR              24      //00C3H
#define     P0INT_VECTOR            37      //012BH
#define     P1INT_VECTOR            38      //0133H
#define     P2INT_VECTOR            39      //013BH
#define     P3INT_VECTOR            40      //0143H
#define     P4INT_VECTOR            41      //014BH
#define     P5INT_VECTOR            42      //0153H
#define     P6INT_VECTOR            43      //015BH
#define     P7INT_VECTOR            44      //0163H
#define     M2MBMM_VECTOR           47      //017BH
#define     ADCBMM_VECTOR           48      //0183H
#define     SPIBMM_VECTOR           49      //018BH
#define     U1TXBMM_VECTOR          50      //0193H
#define     U1RXBMM_VECTOR          51      //019BH
#define     U2TXBMM_VECTOR          52      //01A3H
#define     U2RXBMM_VECTOR          53      //01ABH
#define     U3TXBMM_VECTOR          54      //01B3H
#define     U3RXBMM_VECTOR          55      //01BBH
#define     U4TXBMM_VECTOR          56      //01C3H
#define     U4RXBMM_VECTOR          57      //01CBH
#define     LCMBMM_VECTOR           58      //01D3H
#define     LCM_VECTOR              59      //01DBH

/////////////////////////////////////////////////

#endif

