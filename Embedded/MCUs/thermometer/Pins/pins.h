/*
 * pins.h
 *
 *  Created on: May 12, 2019
 *      Author: Lukas
 */

#ifndef PINS_PINS_H_
#define PINS_PINS_H_

#include"io_digital.h"

/* hardware depend typedef */
#define PIN_TYPEDEF DIGITAL_IO_t*

typedef struct{
	void(*init)(void);
	void(*set_pin)(PIN_TYPEDEF);
	void(*reset_pin)(PIN_TYPEDEF);
}io_application_layer;

typedef enum{
	pin_reset =0,
	pin_set
}pin_states;


void set_pin_state(PIN_TYPEDEF pin, pin_states state);

#endif /* PINS_PINS_H_ */
