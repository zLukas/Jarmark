/*
 * main.c
 *
 *  Created on: 2019 Apr 18 22:57:52
 *  Author: Lukas
 */




#include "main.h"                //Declarations from DAVE Code Generation (includes SFR declaration)

/**

 * @brief main() - Application entry point
 *
 * <b>Details of function</b><br>
 * This routine is the application entry point. It is invoked by the device startup code. It is responsible for
 * invoking the APP initialization dispatcher routine - DAVE_Init() and hosting the place-holder for user application
 * code.
 */


int main(void)
{
	/* init all peripherials */
	digital_gpio_init();
	delay_ms(500);
	oled_init();
	bme_init();
	delay_ms(1000);
	/*first read show dump data */
	bme_read();
  /* Placeholder for user application code. The while loop below can be replaced with user application code. */
  while(1U)
  {
	bme_read();
	oled_show_weather();
	//todo : refactor timer
	for(uint8 i = 0; i < 60; i++){
		delay_ms(1000);
	}
  }
}
