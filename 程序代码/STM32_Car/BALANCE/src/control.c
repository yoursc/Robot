#include "control.h"	
  /**************************************************************************
���ߣ�ƽ��С��֮��
�ҵ��Ա�С�꣺http://shop114407458.taobao.com/
**************************************************************************/
#define T 0.156f
#define L 0.1445f
#define K 311.4f
u8 Flag_Target;
int Voltage_Temp,Voltage_Count,Voltage_All,sum;
/**************************************************************************
�������ܣ����еĿ��ƴ��붼��������
         5ms��ʱ�ж���MPU6050��INT���Ŵ���
         �ϸ�֤���������ݴ����ʱ��ͬ��				 
**************************************************************************/
void TIM1_UP_IRQHandler(void)  
{    
	if(TIM1->SR&0X0001)//��ʱ�ж�
	{   
		  TIM1->SR&=~(1<<0);             //===�����ʱ���жϱ�־λ	       
		  Flag_Target=!Flag_Target;
				 if(Flag_Target==1)                                                  
				{
					if(Usart_Flag==0 )  memcpy(rxbuf,Urxbuf,4*sizeof(u8));	//�������
					Usart_Control();                              //===���մ��ڿ���ָ��
					 Key();                                       //===ɨ�谴��״̬ ����˫�����Ըı�С������״̬
					 Voltage_Temp=Get_battery_volt();		                                 //=====��ȡ��ص�ѹ		
				 	 Voltage_Count++;                                                     //=====ƽ��ֵ������
					 Voltage_All+=Voltage_Temp;                                           //=====��β����ۻ�
					 if(Voltage_Count==100) Voltage=Voltage_All/100,Voltage_All=0,Voltage_Count=0;//=====��ƽ��ֵ	
				}
				 if(Flag_Target==0) 
			 { 
						Encoder_Left=Read_Encoder(2);                                       //===��ȡ��������ֵ							 //Ϊ�˱�֤M�����ٵ�ʱ���׼�����ȶ�ȡ����������
						Encoder_Right=-Read_Encoder(3);                                      //===��ȡ��������ֵ
						if(Turn_Off(Voltage)==0)                              							 //===����������쳣
						{
							Motor_A=Incremental_PI_A(Encoder_Left,Target_A);                   //===�ٶȱջ����Ƽ�����A����PWM
							Motor_B=Incremental_PI_B(Encoder_Right,Target_B);                  //===�ٶȱջ����Ƽ�����B����PWM 
							Xianfu_Pwm();                                                      //===PWM�޷�
							Set_Pwm(Motor_A,Motor_B);                                 	 //===��ֵ��PWM�Ĵ���  
						}
						else
						Set_Pwm(0,0);                                 						 //===��ֵ��PWM�Ĵ���  	                               
			 }   
		 if(Flag_Show==0)				Led_Flash(100);
		 else if(Flag_Show==1)	Led_Flash(0);
	}		 
} 


/**************************************************************************
�������ܣ���ֵ��PWM�Ĵ���
��ڲ���������PWM������PWM
����  ֵ����
**************************************************************************/
void Set_Pwm(int motor_a,int motor_b)
{
    	if(motor_a<0)			PWMA1=7200,PWMA2=7200+motor_a;
			else 	            PWMA2=7200,PWMA1=7200-motor_a;
		
		  if(motor_b<0)			PWMB1=7200,PWMB2=7200+motor_b;
			else 	            PWMB2=7200,PWMB1=7200-motor_b;
}

/**************************************************************************
�������ܣ�����PWM��ֵ 
��ڲ�������
����  ֵ����
**************************************************************************/
void Xianfu_Pwm(void)
{	
	  int Amplitude=6900;    //===PWM������7200 ������6900
    if(Motor_A<-Amplitude) Motor_A=-Amplitude;	
		if(Motor_A>Amplitude)  Motor_A=Amplitude;	
	  if(Motor_B<-Amplitude) Motor_B=-Amplitude;	
		if(Motor_B>Amplitude)  Motor_B=Amplitude;		
}
/**************************************************************************
�������ܣ������޸�С������״̬ 
��ڲ�������
����  ֵ����
**************************************************************************/
void Key(void)
{	
	u8 tmp,tmp2;
	tmp=click_N_Double(50); 
	if(tmp==1)Flag_Stop=!Flag_Stop;//��������С������ͣ
	if(tmp==2)Flag_Show=!Flag_Show;//˫������С������ʾ״̬
	//tmp2=Long_Press();          
  //if(tmp2==1)Flag_Show=!Flag_Show;//����С������ʾ״̬
}

/**************************************************************************
�������ܣ��쳣�رյ��
��ڲ�������ѹ
����  ֵ��1���쳣  0������
**************************************************************************/
u8 Turn_Off( int voltage)
{
	    u8 temp;
			if(voltage<740||Flag_Stop==1)//��ص�ѹ����7.4V�رյ��
			{	                                                
      temp=1;                                            
      }
			else
      temp=0;
      return temp;			
}
/**************************************************************************
�������ܣ�����ֵ����
��ڲ�����int
����  ֵ��unsigned int
**************************************************************************/
int myabs(int a)
{ 		   
	  int temp;
		if(a<0)  temp=-a;  
	  else temp=a;
	  return temp;
}
/**************************************************************************
�������ܣ�����PI������
��ڲ���������������ֵ��Ŀ���ٶ�
����  ֵ�����PWM
��������ʽ��ɢPID��ʽ 
pwm+=Kp[e��k��-e(k-1)]+Ki*e(k)+Kd[e(k)-2e(k-1)+e(k-2)]
e(k)������ƫ�� 
e(k-1)������һ�ε�ƫ��  �Դ����� 
pwm�����������
�����ǵ��ٶȿ��Ʊջ�ϵͳ���棬ֻʹ��PI����
pwm+=Kp[e��k��-e(k-1)]+Ki*e(k)
**************************************************************************/
int Incremental_PI_A (int Encoder,int Target)
{ 	
	 static int Bias,Pwm,Last_bias;
	 Bias=Target-Encoder;                //����ƫ��
	 Pwm+=Velocity_KP*(Bias-Last_bias)+Velocity_KI*Bias;   //����ʽPI������
	 Last_bias=Bias;	                   //������һ��ƫ�� 
	 return Pwm;                         //�������
}
int Incremental_PI_B (int Encoder,int Target)
{ 	
	 static int Bias,Pwm,Last_bias;
	 Bias=Target-Encoder;                //����ƫ��
	 Pwm+=Velocity_KP*(Bias-Last_bias)+Velocity_KI*Bias;   //����ʽPI������
	 Last_bias=Bias;	                   //������һ��ƫ�� 
	 return Pwm;                         //�������
}

/**************************************************************************
�������ܣ����� ���ڿ���ָ����д���
��ڲ�������
����  ֵ����
**************************************************************************/
void Usart_Control(void)
{
	 int flag_left, flag_right;
	 if(rxbuf[1])flag_left=1;   else flag_left=-1;  //�������λ
	 if(rxbuf[3])flag_right=1;  else flag_right=-1;  //�������λ
	 Target_A=flag_left*rxbuf[0];
	 Target_B=flag_right*rxbuf[2];
}
