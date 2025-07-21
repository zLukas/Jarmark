/*
 * oled.c
 *
 *  Created on: Apr 23, 2019
 *      Author: Lukas
 */
#include "oled.h"

char temperature[20];
char humidity[20];
char pressure[20];

void oled_init(void){
	spi_oled_init();
	ssd1306_initalization();

	ssd1306_clear_screen(0xFF);
	delay_ms(1000);
	ssd1306_clear_screen(0x00);
delay_ms(1000);
}


void oled_show_weather(void){
	bme_bosh_api* bme =  get_bme_pointer();
	spi_oled_init();
	ssd1306_clear_screen(0x00);
	delay_ms(10);
	snprintf(temperature, 15, "T %.2f      C", (float)bme->bme_data.temperature);
	snprintf(pressure, 15,    "P %.0f     hPa", (float)bme->bme_data.pressure/100.0);
	snprintf(humidity, 15,    "H %.2f     %%", (float)bme->bme_data.humidity);
	ssd1306_display_string(5, 16, (uint8 *)temperature, 16, 1);
	ssd1306_display_string(5, 32, (uint8 *)pressure, 16, 1);
	ssd1306_display_string(5, 48, (uint8 *)humidity, 16, 1);
	ssd1306_refresh_gram();
}

//todo Lukas : replace delay in ssd sample

