#include "sys.h"
/**************************************************************************
���ߣ�������
�ο���ƽ��С��֮��
**************************************************************************/

u8 Flag_Way=0,Flag_Show=0,Flag_Stop=1;  //ֹͣ��־λ�� ��ʾ��־λ Ĭ��ֹͣ ��ʾ��
int Encoder_Left,Encoder_Right;         //���ұ��������������
float Velocity,Velocity_Set,Turn,Angle_Set;
int Motor_A,Motor_B,Target_A,Target_B;  //�������������           
int Voltage;                            //��ص�ѹ������صı���
float Velocity_KP=62,Velocity_KI=62;	  //�ٶȿ���PID����
u8 Urxbuf[4],rxbuf[4],Usart_Flag;
int main(void)
{ 
	int ua_Encoder,ub_Encoder;
	Stm32_Clock_Init(9);            //=====ϵͳʱ������
	delay_init(72);                 //=====��ʱ��ʼ��
	JTAG_Set(JTAG_SWD_DISABLE);     //=====�ر�JTAG�ӿ�
	LED_Init();                     //=====��ʼ���� LED ���ӵ�Ӳ���ӿ�
	KEY_Init();                     //=====������ʼ��
	OLED_Init();                    //=====OLED��ʼ��
	Encoder_Init_TIM2();            //=====�������ӿ�
	Encoder_Init_TIM3();            //=====��ʼ�������� 
	delay_ms(300);                  //=====��ʱ����
	uart_init(72,115200);           //=====��ʼ������1
  Motor_PWM_Init(7199,0);  				//=====��ʼ��PWM 10KHZ������������� 
	Adc_Init();                     //=====��ص�ѹ����adc��ʼ��
	uart2_init(36,115200); 				  //=====����3��ʼ�� ����
	Timer_Init(49,7199);            //=====��ʱ�жϳ�ʼ�� 
	while(1)
		{     	
					if(Flag_Show==0)         //ʹ��MiniBalance APP��OLED��ʾ��
					{	
							oled_show();          //===��ʾ����
					}		
				ua_Encoder=Encoder_Left+500;
				ub_Encoder=Encoder_Right+500;
				usart1_send(0xff);		
				usart1_send(0xfe);	
				usart1_send(ua_Encoder>>8);
				usart1_send(ua_Encoder&0x00ff);
				usart1_send(ub_Encoder>>8);
				usart1_send(ub_Encoder&0x00ff);		

//				usart2_send(0xff);		
//				usart2_send(0xfe);	
//				usart2_send(ua_Encoder>>8);
//				usart2_send(ua_Encoder&0x00ff);
//				usart2_send(ub_Encoder>>8);
//				usart2_send(ub_Encoder&0x00ff);								
	}
}
