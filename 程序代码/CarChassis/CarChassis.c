#include<reg51.h>
#define uchar unsigned char
#define uint unsigned int

//lefa
sbit lefa1 = P2^1;
sbit lefa2 = P2^2;
sbit lefap = P2^0;
//lefb 2
sbit lefb1 = P2^3;
sbit lefb2 = P2^4;
sbit lefbp = P2^5;
//riga 1
sbit riga1 = P1^1;
sbit riga2 = P1^2;
sbit rigap = P1^0;
//rigb 2
sbit rigb1 = P1^3;
sbit rigb2 = P1^4;
sbit rigbp = P1^5;

void ctrlm(uchar motorn,uchar dire)
{
	//motorn 0:lefta 1:leftb 2:righta 3:rightb
	//dire means 1:goback  2:go  other:stop
	bit out1,out2,outp;
	out1=1;out2=1;outp=1;
	switch(dire)
	{
		case 0:
			out1=1;out2=1;outp=1;break;
		case 1:
			out1=1;out2=0;outp=1;break;
		case 2:
			out1=0;out2=1;outp=1;break;
		default:
			out1=1;out2=1;outp=1;break;
	}
	switch(motorn)
	{
		case 0:
			lefa1=out1;lefa2=out2;lefap=outp;break;
		case 1:
			lefb1=out1;lefb2=out2;lefbp=outp;break;
		case 2:
			riga1=out1;riga2=out2;rigap=outp;break;
		case 3:
			rigb1=out1;rigb2=out2;rigbp=outp;break;
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
	P2=0xFF;
	delay(1000);
	while(1)
	{
		ctrlm(0,1);
		delay(2000);
		ctrlm(1,1);
		delay(2000);
		ctrlm(2,1);
		delay(2000);
		ctrlm(3,1);
		delay(2000);
		ctrlm(0,0);
		delay(2000);
		ctrlm(1,0);
		delay(2000);
		ctrlm(2,0);
		delay(2000);
		ctrlm(3,0);
		delay(4000);
	}
}