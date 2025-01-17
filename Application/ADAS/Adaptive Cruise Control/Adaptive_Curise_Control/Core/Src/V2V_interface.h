/*******************************************************************************************/
/*  Module       :   Vehicle to Vehicle Communication (V2V)                                */
/*  File Name    :   V2V_Interface.h                                                       */
/*  Description  :   Interface File of the V2V  Driver                                     */
/*  Author       :   AHMED_REDA                                                            */
/*  Date         :   2/2/2024                                                             */
/*******************************************************************************************/

#ifndef SRC_V2V_INTERFACE_H_
#define SRC_V2V_INTERFACE_H_

/********************************************************************************************/
/************************************** APIs Proto-Types ************************************/
/********************************************************************************************/

#include "nrf24l01p.h"

typedef enum V2V_state
{
	RECIEVER = 0,TRANSMITTER

}V2VState_t;



/********************************************************************************
 * Name : V2V_voidInit
 * Arguments : V2VState_t state (RECIEVER or TRANSMITTER)
 * Return : Void
 * Description :  The purpose of the V2V_voidInit() function is to initialize
 * the vehicle-to-vehicle (V2V) communication module based on the specified state,
 *  either as a receiver or a transmitter.
 ********************************************************************************/



void V2V_voidInit(V2VState_t state);

/********************************************************************************
 * Name : V2V_voidSendData
 * Arguments : uint8_t* Copy_u8Data (Pointer to array of Chars)
 * Return : Void
 * Description :  The purpose of the V2V_voidSendData() function is to transmit
 * data using the vehicle-to-vehicle (V2V) communication module.
 ********************************************************************************/


void V2V_voidSendData(uint8_t* Copy_u8Data);


/********************************************************************************
 * Name : V2V_u8RecieveData
 * Arguments : uint8_t * Copy_p8Buffer (Pointer to array of Chars)
 * Return : Void
 * Description :  The purpose of the V2V_u8RecieveData() function is to receive data
 * using the vehicle-to-vehicle (V2V) communication module.
 ********************************************************************************/


uint8_t V2V_u8RecieveData(uint8_t * Copy_p8Buffer );




#endif /* SRC_V2V_INTERFACE_H_ */
