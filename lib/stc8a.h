#ifndef __STC8A_H__
#define __STC8A_H__

#if defined (SDCC) || defined (__SDCC)
    #include <stdbool.h>
    #include <lint.h>
    # define __IDATA __idata
    # define __XDATA __xdata
    # define SBIT(name, addr, bit)  __sbit  __at(addr+bit)                    name
    # define SFR(name, addr)        __sfr   __at(addr)                        name
    # define INTERRUPT(name, vector) void name (void) __interrupt (vector)
    # define INTERRUPT_USING(name, vector, regnum) void name (void) __interrupt (vector) __using (regnum)
    // NOP () macro support
    #define NOP() __asm NOP __endasm

#elif defined __CX51__
	# define __IDATA idata
    # define __XDATA xdata
    # define SBIT(name, addr, bit)  sbit  name = addr^bit
    # define SFR(name, addr)        sfr   name = addr
    # define INTERRUPT(name, vector) void name (void) interrupt vector
    # define INTERRUPT_USING(name, vector, regnum) void name (void) interrupt vector using regnum
    // NOP () macro support
    extern void _nop_ (void);
    #define NOP() _nop_()

#else
    # warning unrecognized compiler
    # define SBIT(name, addr, bit)  volatile bool           name
    # define SFR(name, addr)        volatile unsigned char  name

#endif

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
SFR(AUXR2,              0x97);
#define  TXLNRX             0x10
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
SFR(VOCTRL,             0xBB);
SFR(ADC_CONTR,          0xBC);
#define  ADC_POWER          0x80
#define  ADC_START          0x40
#define  ADC_FLAG           0x20
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
SFR(ISP_DATA,           0xC2);
SFR(ISP_ADDRH,          0xC3);
SFR(ISP_ADDRL,          0xC4);
SFR(ISP_CMD,            0xC5);
SFR(ISP_TRIG,           0xC6);
SFR(ISP_CONTR,          0xC7);
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
SBIT(F1,                _PSW, 1);
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
SFR(TH4,                0xD2);
SFR(TL4,                0xD3);
SFR(TH3,                0xD4);
SFR(TL3,                0xD5);
SFR(TH2,                0xD6);
SFR(TL2,                0xD7);
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
SFR(CCAPM3,             0xDD);
#define  ECOM3              0x40
#define  CCAPP3             0x20
#define  CCAPN3             0x10
#define  MAT3               0x08
#define  TOG3               0x04
#define  PWM3               0x02
#define  ECCF3              0x01
SFR(ADCCFG,             0xDE);
#define  ADC_RESFMT         0x20
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
#define  PIS                0x08
#define  NIS                0x04
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
SFR(CCAP3L,             0xED);
SFR(AUXINTIF,           0xEF);
#define  INT4IF             0x40
#define  INT3IF             0x20
#define  INT2IF             0x10
#define  T4IF               0x04
#define  T3IF               0x02
#define  T2IF               0x01
SFR(B,                  0xF0);
SFR(PWMCFG,             0xF1);
#define  CBIF               0x80
#define  ETADC              0x40
SFR(PCA_PWM0,           0xF2);
SFR(PCA_PWM1,           0xF3);
SFR(PCA_PWM2,           0xF4);
SFR(PCA_PWM3,           0xF5);
SFR(PWMIF,              0xF6);
#define  C7IF               0x80
#define  C6IF               0x40
#define  C5IF               0x20
#define  C4IF               0x10
#define  C3IF               0x08
#define  C2IF               0x04
#define  C1IF               0x02
#define  C0IF               0x01
SFR(PWMFDCR,            0xF7);
#define  INVCMP             0x80
#define  INVIO              0x40
#define  ENFD               0x20
#define  FLTFLIO            0x10
#define  EFDI               0x08
#define  FDCMP              0x04
#define  FDIO               0x02
#define  FDIF               0x01
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
SFR(CCAP3H,             0xFD);
SFR(PWMCR,              0xFE);
#define  ENPWM              0x80
#define  ECBI               0x40
SFR(RSTCFG,             0xFF);

#define T24M          (*(unsigned  char __IDATA *)0xFB)
#define T22M1184      (*(unsigned  char __IDATA *)0xFA)
#define F32K          (*(unsigned short __IDATA *)0xF8)
#define UUID_ADDR       (unsigned  char __IDATA *)0xF1
#define BANDGAP       (*(unsigned short __IDATA *)0xEF)

#define P0PU        (*(unsigned char volatile __XDATA *)0xfe10)
#define P1PU        (*(unsigned char volatile __XDATA *)0xfe11)
#define P2PU        (*(unsigned char volatile __XDATA *)0xfe12)
#define P3PU        (*(unsigned char volatile __XDATA *)0xfe13)
#define P4PU        (*(unsigned char volatile __XDATA *)0xfe14)
#define P5PU        (*(unsigned char volatile __XDATA *)0xfe15)
#define P6PU        (*(unsigned char volatile __XDATA *)0xfe16)
#define P7PU        (*(unsigned char volatile __XDATA *)0xfe17)
#define P0NCS       (*(unsigned char volatile __XDATA *)0xfe18)
#define P1NCS       (*(unsigned char volatile __XDATA *)0xfe19)
#define P2NCS       (*(unsigned char volatile __XDATA *)0xfe1a)
#define P3NCS       (*(unsigned char volatile __XDATA *)0xfe1b)
#define P4NCS       (*(unsigned char volatile __XDATA *)0xfe1c)
#define P5NCS       (*(unsigned char volatile __XDATA *)0xfe1d)
#define P6NCS       (*(unsigned char volatile __XDATA *)0xfe1e)
#define P7NCS       (*(unsigned char volatile __XDATA *)0xfe1f)

#define CKSEL       (*(unsigned char volatile __XDATA *)0xfe00)
#define CLKDIV      (*(unsigned char volatile __XDATA *)0xfe01)
#define IRC24MCR    (*(unsigned char volatile __XDATA *)0xfe02)
#define XOSCCR      (*(unsigned char volatile __XDATA *)0xfe03)
#define IRC32KCR    (*(unsigned char volatile __XDATA *)0xfe04)

#define PWMC        (*(unsigned int  volatile __XDATA *)0xfff0)
#define PWMCH       (*(unsigned char volatile __XDATA *)0xfff0)
#define PWMCL       (*(unsigned char volatile __XDATA *)0xfff1)
#define PWMCKS      (*(unsigned char volatile __XDATA *)0xfff2)
#define TADCP       (*(unsigned char volatile __XDATA *)0xfff3)
#define TADCPH      (*(unsigned char volatile __XDATA *)0xfff3)
#define TADCPL      (*(unsigned char volatile __XDATA *)0xfff4)
#define PWM0T1      (*(unsigned int  volatile __XDATA *)0xff00)
#define PWM0T1H     (*(unsigned char volatile __XDATA *)0xff00)
#define PWM0T1L     (*(unsigned char volatile __XDATA *)0xff01)
#define PWM0T2      (*(unsigned int  volatile __XDATA *)0xff02)
#define PWM0T2H     (*(unsigned char volatile __XDATA *)0xff02)
#define PWM0T2L     (*(unsigned char volatile __XDATA *)0xff03)
#define PWM0CR      (*(unsigned char volatile __XDATA *)0xff04)
#define PWM0HLD     (*(unsigned char volatile __XDATA *)0xff05)
#define PWM1T1      (*(unsigned int  volatile __XDATA *)0xff10)
#define PWM1T1H     (*(unsigned char volatile __XDATA *)0xff10)
#define PWM1T1L     (*(unsigned char volatile __XDATA *)0xff11)
#define PWM1T2      (*(unsigned int  volatile __XDATA *)0xff12)
#define PWM1T2H     (*(unsigned char volatile __XDATA *)0xff12)
#define PWM1T2L     (*(unsigned char volatile __XDATA *)0xff13)
#define PWM1CR      (*(unsigned char volatile __XDATA *)0xff14)
#define PWM1HLD     (*(unsigned char volatile __XDATA *)0xff15)
#define PWM2T1      (*(unsigned int  volatile __XDATA *)0xff20)
#define PWM2T1H     (*(unsigned char volatile __XDATA *)0xff20)
#define PWM2T1L     (*(unsigned char volatile __XDATA *)0xff21)
#define PWM2T2      (*(unsigned int  volatile __XDATA *)0xff22)
#define PWM2T2H     (*(unsigned char volatile __XDATA *)0xff22)
#define PWM2T2L     (*(unsigned char volatile __XDATA *)0xff23)
#define PWM2CR      (*(unsigned char volatile __XDATA *)0xff24)
#define PWM2HLD     (*(unsigned char volatile __XDATA *)0xff25)
#define PWM3T1      (*(unsigned int  volatile __XDATA *)0xff30)
#define PWM3T1H     (*(unsigned char volatile __XDATA *)0xff30)
#define PWM3T1L     (*(unsigned char volatile __XDATA *)0xff31)
#define PWM3T2      (*(unsigned int  volatile __XDATA *)0xff32)
#define PWM3T2H     (*(unsigned char volatile __XDATA *)0xff32)
#define PWM3T2L     (*(unsigned char volatile __XDATA *)0xff33)
#define PWM3CR      (*(unsigned char volatile __XDATA *)0xff34)
#define PWM3HLD     (*(unsigned char volatile __XDATA *)0xff35)
#define PWM4T1      (*(unsigned int  volatile __XDATA *)0xff40)
#define PWM4T1H     (*(unsigned char volatile __XDATA *)0xff40)
#define PWM4T1L     (*(unsigned char volatile __XDATA *)0xff41)
#define PWM4T2      (*(unsigned int  volatile __XDATA *)0xff42)
#define PWM4T2H     (*(unsigned char volatile __XDATA *)0xff42)
#define PWM4T2L     (*(unsigned char volatile __XDATA *)0xff43)
#define PWM4CR      (*(unsigned char volatile __XDATA *)0xff44)
#define PWM4HLD     (*(unsigned char volatile __XDATA *)0xff45)
#define PWM5T1      (*(unsigned int  volatile __XDATA *)0xff50)
#define PWM5T1H     (*(unsigned char volatile __XDATA *)0xff50)
#define PWM5T1L     (*(unsigned char volatile __XDATA *)0xff51)
#define PWM5T2      (*(unsigned int  volatile __XDATA *)0xff52)
#define PWM5T2H     (*(unsigned char volatile __XDATA *)0xff52)
#define PWM5T2L     (*(unsigned char volatile __XDATA *)0xff53)
#define PWM5CR      (*(unsigned char volatile __XDATA *)0xff54)
#define PWM5HLD     (*(unsigned char volatile __XDATA *)0xff55)
#define PWM6T1      (*(unsigned int  volatile __XDATA *)0xff60)
#define PWM6T1H     (*(unsigned char volatile __XDATA *)0xff60)
#define PWM6T1L     (*(unsigned char volatile __XDATA *)0xff61)
#define PWM6T2      (*(unsigned int  volatile __XDATA *)0xff62)
#define PWM6T2H     (*(unsigned char volatile __XDATA *)0xff62)
#define PWM6T2L     (*(unsigned char volatile __XDATA *)0xff63)
#define PWM6CR      (*(unsigned char volatile __XDATA *)0xff64)
#define PWM6HLD     (*(unsigned char volatile __XDATA *)0xff65)
#define PWM7T1      (*(unsigned int  volatile __XDATA *)0xff70)
#define PWM7T1H     (*(unsigned char volatile __XDATA *)0xff70)
#define PWM7T1L     (*(unsigned char volatile __XDATA *)0xff71)
#define PWM7T2      (*(unsigned int  volatile __XDATA *)0xff72)
#define PWM7T2H     (*(unsigned char volatile __XDATA *)0xff72)
#define PWM7T2L     (*(unsigned char volatile __XDATA *)0xff73)
#define PWM7CR      (*(unsigned char volatile __XDATA *)0xff74)
#define PWM7HLD     (*(unsigned char volatile __XDATA *)0xff75)

//I2C特殊功能寄存器
#define I2CCFG      (*(unsigned char volatile __XDATA *)0xfe80)
#define ENI2C       0x80
#define MSSL        0x40
#define I2CMSCR     (*(unsigned char volatile __XDATA *)0xfe81)
#define EMSI        0x80
#define I2CMSST     (*(unsigned char volatile __XDATA *)0xfe82)
#define MSBUSY      0x80
#define MSIF        0x40
#define MSACKI      0x02
#define MSACKO      0x01
#define I2CSLCR     (*(unsigned char volatile __XDATA *)0xfe83)
#define ESTAI       0x40
#define ERXI        0x20
#define ETXI        0x10
#define ESTOI       0x08
#define SLRST       0x01
#define I2CSLST     (*(unsigned char volatile __XDATA *)0xfe84)
#define SLBUSY      0x80
#define STAIF       0x40
#define RXIF        0x20
#define TXIF        0x10
#define STOIF       0x08
#define TXING       0x04
#define SLACKI      0x02
#define SLACKO      0x01
#define I2CSLADR    (*(unsigned char volatile __XDATA *)0xfe85)
#define I2CTXD      (*(unsigned char volatile __XDATA *)0xfe86)
#define I2CRXD      (*(unsigned char volatile __XDATA *)0xfe87)


#endif
