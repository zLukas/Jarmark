/*
 * pins.c
 *
 *  Created on: May 12, 2019
 *      Author: Lukas
 */


#include "pins.h"

io_application_layer io_hardware ={
		.set_pin = digital_set_pin,
		.reset_pin = digital_reset_pin
};



void set_pin_state(PIN_TYPEDEF pin, pin_states state){
	(state == pin_set)? io_hardware.set_pin(pin) : io_hardware.reset_pin(pin);
}
