/*
 * usic_spi.c
 *
 *  Created on: May 25, 2019
 *      Author: Lukas
 */


#include "usic_spi.h"
/*
 * oled needs transmit on rising edge,
 * DAVE CE allows to configure clock in 2 ways:
 *
 * transmit/receive -> falling/rising edge
 * transmit/receive -> rising/falling edge
 *
 *  on first configuration oled works proper but bme miss one received bit ,
 *  on secong bme works properly but oled not at all
 */
extern SPI_MASTER_t bme_spi; // configuration: transmit on falling edge, receive on rising
extern SPI_MASTER_t oled_spi;// configuration: transmit on rising edge, receive on falling

void spi_init(void){
	SPI_MASTER_Init(&SPI_MASTER_0);
	SPI_MASTER_SetMode(&SPI_MASTER_0, XMC_SPI_CH_MODE_STANDARD);
	SPI_MASTER_SetBaudRate(&SPI_MASTER_0,16000);
}

uint8 usic_spi_send_read( uint8* data_to_send, uint8* data_to_read, uint8 data_send_count , uint8 data_read_count){
	SPI_MASTER_Transmit(&SPI_MASTER_0, data_to_send, data_send_count);
	while(SPI_MASTER_IsTxBusy(&SPI_MASTER_0));
	//wait for receive
	//this delay is demanded, otherwise it not read anything
	delay_ms(50);
	SPI_MASTER_Receive(&SPI_MASTER_0, data_to_read, data_read_count);
	while(SPI_MASTER_IsRxBusy(&SPI_MASTER_0));
	return 0;

}

void spi_bme_init(void){
	SPI_MASTER_0 = bme_spi;
	spi_init();
}

void spi_oled_init(void){
	SPI_MASTER_0 = oled_spi;
	spi_init();
}


