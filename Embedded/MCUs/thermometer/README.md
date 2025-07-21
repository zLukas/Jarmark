# Weather module
simple weather applicaton written in DAVE 4.4.2 enviroment.

Components used:
* [XMC1100 (XMC2GO eval board)](https://pl.farnell.com/infineon/kitxmc2goxmc1100v1tobo1/evaluation-board-cortex-m0-mcu/dp/2422880?st=xmc)
* [bosh BME280 weather sensor](https://www.amazon.com/GY-BME280-3-3-Precision-Barometric-Temperature-Raspberry/dp/B01MUD07SX)
* [SSD1306 oled screen](https://www.amazon.com/Waveshare-0-96inch-OLED-horizontal-Controller/dp/B00MHD5ZCQ)

Communication interface is 4-wire SPI.

For both,  oled and sensor producents APIs were used:

* BME280 : https://github.com/BoschSensortec/BME280_driver
* SSD1306 oled: https://www.waveshare.com/wiki/File:0.96inch-OLED-Code.7z

Each of this APIs was slightly changed.

