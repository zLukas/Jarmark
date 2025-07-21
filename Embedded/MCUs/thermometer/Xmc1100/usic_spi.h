/*
 * usic_spi.h
 *
 *  Created on: May 25, 2019
 *      Author: Lukas
 */

#ifndef XMC1100_USIC_SPI_H_
#define XMC1100_USIC_SPI_H_
#include <spi_master.h>
#include "defines.h"
# include "timer.h"
/* DAVE_init initialize usic_spi*/
void spi_init(void);
uint8 usic_spi_send_read(uint8* data_to_send, uint8* data_to_read, uint8 data_send_count , uint8 data_read_count);
void spi_oled_init(void);
void spi_bme_init(void);


#endif /* XMC1100_USIC_SPI_H_ */
