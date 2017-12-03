#include<reg51.h>
#include<intrins.h>

#define uchar unsigned char
#define int8 short
#define int8u unsigned short
#define int16 int
#define int16u unsigned int
#define int32 long
#define int32u unsigned long

sbit motor_a1 = P1^0;
sbit motor_a2 = P1^1;
sbit motor_ap = P3^4;

sbit K1 = P3^0;
sbit K2 = P3^1;
sbit K3 = P3^2;
sbit K4 = P3^3;

static int8 pwm0=10;
unsigned char segcode[16]={0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e};
int8 pwma0;
int8 pwma,pwm;

void delayms(unsigned int t)
{
	int16u i,j;
	j=120;
	for(i=0;i<=t;i++)
	{
		while(j--);
	}
}

void InitTimer0(void)
{
	TMOD= 0x01;
	TH0 = 0xFC;
	TL0 = 0x18;
	EA  = 1;
	ET0 = 1;
	TR0 = 1;
}

void Timer0Interrupt(void) interrupt 1
{
	TH0 = 0x0FC;
	TL0 = 0x18;
	pwma--;
}

void main(void)
{
	pwma0=10;
	pwma,pwm=0;
	P1=0xFF;
	P0=0xFF;
	delayms(1000);
	motor_a1=0;
	motor_a2=1;
	InitTimer0();
	while(1)
	{
		if(pwm<=0)
		{
			pwm=pwm0;
			motor_ap=0;
			pwma=pwma0;
		}
		
		if(pwma<=0) motor_ap=1;
		
		if(K1==0)
		{
			delayms(2);
			if(K1==0)
			{
				pwma0=pwma0+1;
				if(pwma0>=11) pwma0=0;
			}
		}
		P0=segcode[pwma];
	}
}