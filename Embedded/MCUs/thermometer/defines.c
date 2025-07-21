/*
 * defines.c
 *
 *  Created on: May 25, 2019
 *      Author: Lukas
 */


#include "defines.h"
void delay_us(volatile uint32 time){
	while(time != 0){
		time--;
	}
}
