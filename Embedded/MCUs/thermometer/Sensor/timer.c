/*
 * timer.c
 *
 *  Created on: May 28, 2019
 *      Author: Lukas
 */
//todo Lukas: move timer to XMC timers
# include "timer.h"
void delay_ms(volatile uint32 time){
	time *=time;
	while(time){
		time--;
	}
}
