#include<reg51.h>
#define uchar unsigned char
#define uint unsigned int
	
void delay_ms(unsigned int x)
{
	uchar t;
	while(x--)
	{
		for(t=0;t<120;t++);
	}
}

void main()
{
	P2=0xFE;
	delay_ms(500);
	while(1)
	{
		P2=0xFE;
		delay_ms(500);
		P2=0xFD;
		delay_ms(500);
		P2=0xFB;
		delay_ms(500);
	}
}