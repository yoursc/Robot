#include<reg51.h>
#define uchar unsigned char
#define uint unsigned int

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

void delay(unsigned int x)
{
	uchar t;
	while(x--)
	{
		for(t=0;t<120;t++);
	}
}

void main()
{
	P1=0xFF;
	P0=0xFF;
	delay(1000);
	while(1)
	{
		ctrlm('a',1);
		delay(2000);
		ctrlm('b',1);
		delay(2000);
		ctrlm('c',1);
		delay(2000);
		ctrlm('d',1);
		delay(2000);
		ctrlm('a',3);
		delay(2000);
		ctrlm('b',3);
		delay(2000);
		ctrlm('c',3);
		delay(2000);
		ctrlm('d',3);
		delay(2000);
		P0=0xFF;
	}
}