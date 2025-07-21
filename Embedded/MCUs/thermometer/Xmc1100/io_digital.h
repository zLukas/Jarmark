/*
 * digital_io.h
 *
 *  Created on: May 12, 2019
 *      Author: Lukas
 */

#ifndef XMC1100_IO_DIGITAL_H_
#define XMC1100_IO_DIGITAL_H_
#include <digital_io.h>
#include"defines.h"

void digital_gpio_init(void);
void digital_set_pin(const DIGITAL_IO_t* digital_io_pin );
void digital_reset_pin(const DIGITAL_IO_t* digital_io_pin);





#endif /* XMC1100_IO_DIGITAL_H_ */
