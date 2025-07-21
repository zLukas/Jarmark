/*
 * bm280.h
 *
 *  Created on: May 25, 2019
 *      Author: Lukas
 */

#ifndef SENSOR_SENSOR_H_
#define SENSOR_SENSOR_H_

#include "defines.h"
#include "bme280.h"
#include "spi.h"
#include "timer.h"


#define BME_RESET_ADDRESS_VALUE 0xB6

#define OSRS_TEMPERATURE  	    0x04   //100
#define OSRS_PRESSURE     		0x02   //010
#define OSRS_HUMIDITY			0x01   //001
#define BME_NORMAL_MODE			0x03   //11
#define BME_FORCED_MODE			0x01
/* sensor handlng using bosh API*/
typedef struct{
	uint8 oversmpling;
	uint8 value;
}bme280_oversamplings;
typedef struct{
	struct bme280_dev bme_device;
	struct bme280_data bme_data;
	struct bme280_uncomp_data bme_raw_data;
	int8 initialized;
	uint16 measurement_time;
	int8 crc_test_status;
}bme_bosh_api;

void bme_init(void);
void bme_read(void);
bme_bosh_api* get_bme_pointer(void);
#endif /* SENSOR_SENSOR_H_ */
