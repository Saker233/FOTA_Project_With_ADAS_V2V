/*******************************************************************************
**  FILENAME     : CAN_CONFIG.c         			                          **
**                                                                            **
**  VERSION      : 1.0.0                                                      **
**                                                                            **
**  DATE         : 2024-01-26                                                 **
**                                                                            **
**                                                                            **
**  AUTHOR       : Mohamed Saker	                                          **
**                                                                            **
**  DESCRIPTION  : CAN Driver config file                                     **
**                                                                            **
*******************************************************************************/

#include "CAN_INTERFACE.h"

/*FOR BIT RATE 500KHZ , PRESCALE = 1, SJW = 0 ,SEG1 = 0X0C , SEG2 = 0X01 , SAMPLE PIONT AT 87.5 , BTR=  0x001C0000


 FOR BIT RATE 500KHZ , PRESCALE = 1, SJW = 16 ,SEG1 = 0X0D , SEG2 = 0X02 , SAMPLE PIONT AT 87.5 , BTR=  0x001C0000 */
CAN_InitTypeDef CAN_InitStruct ={
		1, 				//prescalr
		0, 				//mode
		0x10, 			// sjw
		0x0D, 			//bs1
		0x02, 			//bs2
		DISABLE,
		DISABLE,
		DISABLE,
		DISABLE,
		DISABLE,
		DISABLE,
};

CAN_FilterInitTypeDef CAN_FilterInitStruct_0 = {
		(0x65D)<<5,
		0x0000,
		(0x65D)<<5,
		0x0000,
		CAN_FILTER_FIFO0,
		0,
		CAN_FILTERSCALE_32BIT,
		ENABLE
};

CAN_FilterInitTypeDef CAN_FilterInitStruct_2 = {
		0x00400000,
		0x00400000,
		CAN_FilterMode_IdMask,
		2,
		CAN_FilterScale_32bit,
		CAN_Filter_FIFO0,
		ENABLE
};

CAN_FilterInitTypeDef CAN_FilterInitStruct_3 = {
		0x00800000,
		0x00800000,
		CAN_FilterMode_IdMask,
		3,
		CAN_FilterScale_32bit,
		CAN_Filter_FIFO0,
		ENABLE
};

CAN_FilterInitTypeDef CAN_FilterInitStruct_4 = {
		0x00800000,
		0x00800000,
		CAN_FilterMode_IdMask,
		3,
		CAN_FilterScale_32bit,
		CAN_Filter_FIFO0,
		ENABLE
};

CAN_FilterInitTypeDef CAN_FilterInitStruct_5 = {
		0x00C00000,
		0x00C00000,
		CAN_FilterMode_IdMask,
		5,
		CAN_FilterScale_32bit,
		CAN_Filter_FIFO0,
		ENABLE
};


//const Can_ConfigType Can_Configurations =
//{
//    CAN_InitStruct,
//
//    CAN_FilterInitStruct_1,
//};





























