#include<reg51.h>
#include<intrins.h>

#define uchar unsigned char
#define int8 short
#define int8u unsigned short
#define int16 int
#define int16u unsigned int
#define int32 long
#define int32u unsigned long

sbit motor_a1 = P0^0;
sbit motor_a2 = P0^1;
sbit motor_b1 = P0^2;
sbit motor_b2 = P0^3;
sbit motor_c1 = P0^4;
sbit motor_c2 = P0^5;
sbit motor_d1 = P0^6;
sbit motor_d2 = P0^7;
sbit motor_ap = P2^0;
sbit motor_bp = P2^1;
sbit motor_cp = P2^2;
sbit motor_dp = P2^3;

//设定值
static int8 pwm0=10;

//全局变量
int8 pwma0=0,pwmb0=0,pwmc0=0,pwmd0=0;
int8 pwma,pwmb,pwmc,pwmd,pwm=0;

void ctrlm(uchar motor,uchar dire)
{
	uchar data1,data2,datap;
	switch(dire)
	{
		case 0:
			data1=0;data2=0;break;
		case 1:
			data1=1;data2=0;break;
		case 2:
			data1=0;data2=1;break;
		case 3:
			data1=1;data2=1;break;
		default:
			data1=0;data2=0;break;
	}
	switch(motor)
	{
		case 'a':
			motor_a1=data1;motor_a2=data2;motor_ap=datap;break;
		case 'b':
			motor_b1=data1;motor_b2=data2;motor_bp=datap;break;
		case 'c':
			motor_c1=data1;motor_c2=data2;motor_cp=datap;break;
		case 'd':
			motor_d1=data1;motor_d2=data2;motor_dp=datap;break;
		default:
			break;
	}
}

void delayms(unsigned int t)
{
	int16u i,j;
	for(i=0;i<t;i++)
	{
		for(j=0;j<=100;j++)
		{
			_nop_();
		}
	}
}

void InitTimer0(void)
{
	TMOD=0x01;
	TH0=0x0FC;
	TL0=0x18;
	EA=1;
	ET0=1;
	TR0=1;
}

void Timer0Interrupt(void) interrupt 1 using 3
{
	TH0=0x0FC;
	TL0=0x18;
	pwma--;
	pwmb--;
	pwmc--;
	pwmd--;
}

void main()
{
	P1=0xFF;
	P0=0xFF;
	delayms(1000);
	while(1)
	{
		if(pwm<=0)
		{
			pwm=pwm0;
			motor_ap=0;
			motor_bp=0;
			motor_cp=0;
			motor_dp=0;
			pwma=pwma0;
			pwmb=pwmb0;
			pwmc=pwmc0;
			pwmd=pwmd0;
		}
		if(pwma<=0) motor_ap=1;
		if(pwmb<=0) motor_bp=1;
		if(pwmc<=0) motor_cp=1;
		if(pwmd<=0) motor_dp=1;
	}
}