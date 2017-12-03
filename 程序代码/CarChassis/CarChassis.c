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
sbit motor_b1 = P1^2;
sbit motor_b2 = P1^3;
sbit motor_c1 = P1^4;
sbit motor_c2 = P1^5;
sbit motor_d1 = P1^6;
sbit motor_d2 = P1^7;
sbit motor_ap = P3^4;
sbit motor_bp = P3^5;
sbit motor_cp = P3^6;
sbit motor_dp = P3^7;
sbit K1 = P3^0;
sbit K2 = P3^1;
sbit K3 = P3^2;
sbit K4 = P3^3;

//设定值
static int8 pwm0=10;

//全局变量
int8 pwma0,pwmb0,pwmc0,pwmd0;
int8 pwma,pwmb,pwmc,pwmd,pwm;

void ctrlm(uchar motor,uchar dire)
{
	uchar data1,data2;
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
			motor_a1=data1;motor_a2=data2;break;
		case 'b':
			motor_b1=data1;motor_b2=data2;break;
		case 'c':
			motor_c1=data1;motor_c2=data2;break;
		case 'd':
			motor_d1=data1;motor_d2=data2;break;
		default:
			break;
	}
}

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

void Timer0Interrupt(void) interrupt 1 using 3
{
	TH0 = 0x0FC;
	TL0 = 0x18;
	pwma--;
	pwmb--;
	pwmc--;
	pwmd--;
}

void main(void)
{
	pwma0=10,pwmb0=10,pwmc0=10,pwmd0=10;
	pwma,pwmb,pwmc,pwmd,pwm=0;
	P1=0xFF;
	P0=0xFF;
	delayms(1000);
	ctrlm('a',1);
	ctrlm('b',2);
	ctrlm('c',2);
	ctrlm('d',1);
	InitTimer0();
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
		
		if(K1==0)
		{
			delayms(2);
			if(K1==0)
			{
				pwma0=pwma0+1;
				if(pwma0>=11) pwma0=0;
			}
		}
		if(K2==0)
		{
			delayms(2);
			if(K2==0)
			{
				pwmb0=pwmb0+1;
				if(pwmb0>=11) pwmb0=0;
			}
		}
		if(K3==0)
		{
			delayms(2);
			if(K3==0)
			{
				pwmc0=pwmc0+1;
				if(pwmc0>=11) pwmc0=0;
			}
		}
		if(K4==0)
		{
			delayms(2);
			if(K4==0)
			{
				pwmd0=pwmd0+1;
				if(pwmd0>=11) pwmd0=0;
			}
		}
	}
}