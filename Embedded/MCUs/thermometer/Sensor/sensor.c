/*
 * bm280.c
 *
 *  Created on: May 25, 2019
 *      Author: Lukas
 */

#include "sensor.h"

bme_bosh_api bme_sensor;
bme280_oversamplings convertion_table[] ={
		{.oversmpling= BME280_OVERSAMPLING_1X, .value = 1},
		{.oversmpling= BME280_OVERSAMPLING_2X, .value = 2},
		{.oversmpling= BME280_OVERSAMPLING_4X, .value = 4},
		{.oversmpling= BME280_OVERSAMPLING_8X, .value = 8},
		{.oversmpling= BME280_OVERSAMPLING_16X, .value = 16}
};


bme_bosh_api* get_bme_pointer(void){
	return &bme_sensor;
}

void set_bme(void){
	bme_bosh_api* bme = get_bme_pointer();
	uint8 settings_to_update;
	bme280_set_sensor_mode(BME280_SLEEP_MODE, &bme->bme_device);

	/* assign values */
	bme->bme_device.settings.osr_h = BME280_OVERSAMPLING_1X;
	bme->bme_device.settings.osr_p = BME280_OVERSAMPLING_16X;
	bme->bme_device.settings.osr_t = BME280_OVERSAMPLING_2X;
	bme->bme_device.settings.filter= BME280_FILTER_COEFF_16;

	/* add setting to be updated */
	settings_to_update = BME280_OSR_PRESS_SEL;
	settings_to_update |= BME280_OSR_TEMP_SEL;
	settings_to_update |= BME280_OSR_HUM_SEL;
	settings_to_update |= BME280_FILTER_SEL;

	bme280_set_sensor_settings(settings_to_update, &bme->bme_device);
	bme->bme_device.delay_ms(10);
	bme280_get_sensor_settings(&bme->bme_device);
}


void  bme_init(void){
	spi_bme_init();
	bme_bosh_api* bme = get_bme_pointer();
	bme->initialized= 1 ;
	bme->bme_device.dev_id = 0;
	bme->bme_device.chip_id = 0;
	bme->bme_device.write = spi_send;
	bme->bme_device.read = spi_read;
	bme->bme_device.delay_ms = delay_ms;
	bme->initialized  = bme280_init(&(bme->bme_device));
	bme->crc_test_status =  bme280_crc_selftest(&(bme->bme_device));
}

void bme_read(void){
	spi_bme_init();
	set_bme();
	bme_bosh_api* bme = get_bme_pointer();
	bme280_set_sensor_mode(BME280_FORCED_MODE, &bme->bme_device);
	bme->bme_device.delay_ms(40);
	bme280_get_sensor_data(BME280_ALL, &(bme->bme_data), &(bme->bme_device));
}
