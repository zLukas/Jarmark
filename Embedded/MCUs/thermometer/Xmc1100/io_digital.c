/*
 * io_digital.c
 *
 *  Created on: May 12, 2019
 *      Author: Lukas
 */
#include "io_digital.h"



void digital_gpio_init(void){
	DIGITAL_IO_Init(&OLED_DC);
	DIGITAL_IO_Init(&OLED_RESET);
	DIGITAL_IO_Init(&OLED_CS);
	DIGITAL_IO_Init(&SENSOR_CS);
}

void digital_set_pin(const DIGITAL_IO_t* digital_io_pin ){
 DIGITAL_IO_SetOutputHigh(digital_io_pin);
}
void digital_reset_pin(const DIGITAL_IO_t* digital_io_pin ){
	DIGITAL_IO_SetOutputLow(digital_io_pin);
}

