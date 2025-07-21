/*
 * spi.c
 *
 *  Created on: May 25, 2019
 *      Author: Lukas
 */


#include "spi.h"

spi_functions hardware_spi ={
		.exchange_data= usic_spi_send_read,
		.set_pin = digital_set_pin,
		.reset_pin =digital_reset_pin
};

int8 spi_send(uint8 register_address, uint8* data_to_exchange, uint8 data_send_count){
	hardware_spi.reset_pin(&SENSOR_CS);
	delay_us(2);
	uint8*  combined_data = (uint8*)calloc(data_send_count + 1, sizeof(uint8));
	combined_data[0] = register_address;
	for(uint8 i = 1 ;i < data_send_count + 1; i++){
		combined_data[i] = data_to_exchange[i-1];
	}
	 //exchange_data(*data_to_send, *data_to_read, data_send_count, data_read_count);
	uint8 result = hardware_spi.exchange_data(combined_data, NULL, data_send_count + 1, 0);
	free(combined_data);
	delay_us(2);
	hardware_spi.set_pin(&SENSOR_CS);
	return  result;
}

int8 spi_read(uint8 register_address, uint8* data_to_exchange, uint8 data_count){

	hardware_spi.reset_pin(&SENSOR_CS);
	delay_us(2);
	 //exchange_data(*data_to_send, *data_to_read, data_send_count, data_read_count);
	uint8 result = hardware_spi.exchange_data(&register_address, data_to_exchange, 1, data_count);
	delay_us(2);
	hardware_spi.set_pin(&SENSOR_CS);
	return result;
}
