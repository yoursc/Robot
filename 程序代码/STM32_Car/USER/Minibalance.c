#include "sys.h"
/**************************************************************************
作者：曹沛文
参考：平衡小车之家
**************************************************************************/

u8 Flag_Way=0,Flag_Show=0,Flag_Stop=1;  //停止标志位和 显示标志位 默认停止 显示打开
int Encoder_Left,Encoder_Right;         //左右编码器的脉冲计数
float Velocity,Velocity_Set,Turn,Angle_Set;
int Motor_A,Motor_B,Target_A,Target_B;  //电机舵机控制相关           
int Voltage;                            //电池电压采样相关的变量
float Velocity_KP=62,Velocity_KI=62;	  //速度控制PID参数
u8 Urxbuf[4],rxbuf[4],Usart_Flag;
int main(void)
{ 
	int ua_Encoder,ub_Encoder;
	Stm32_Clock_Init(9);            //=====系统时钟设置
	delay_init(72);                 //=====延时初始化
	JTAG_Set(JTAG_SWD_DISABLE);     //=====关闭JTAG接口
	LED_Init();                     //=====初始化与 LED 连接的硬件接口
	KEY_Init();                     //=====按键初始化
	OLED_Init();                    //=====OLED初始化
	Encoder_Init_TIM2();            //=====编码器接口
	Encoder_Init_TIM3();            //=====初始化编码器 
	delay_ms(300);                  //=====延时启动
	uart_init(72,115200);           //=====初始化串口1
  Motor_PWM_Init(7199,0);  				//=====初始化PWM 10KHZ，用于驱动电机 
	Adc_Init();                     //=====电池电压采样adc初始化
	uart2_init(36,115200); 				  //=====串口3初始化 蓝牙
	Timer_Init(49,7199);            //=====定时中断初始化 
	while(1)
		{     	
					if(Flag_Show==0)         //使用MiniBalance APP和OLED显示屏
					{	
							oled_show();          //===显示屏打开
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
