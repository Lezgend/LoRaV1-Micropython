# LoRaV1-Micropython
A very simple library and useful for L&amp;E LoRa Module V1 on ESP32 or ESP8266 using MicroPython

| Back | Front |
|------|-------|
| <img src="https://github.com/Lezgend/LoRaV1-Micropython/blob/main/docs/L%26E%20LoRa%20Module%20V1_Back.jpg" width="400" height="600"> | <img src="https://github.com/Lezgend/LoRaV1-Micropython/blob/main/docs/L%26E%20LoRa%20Module%20V1_Front.jpg" width="400" height="600"> |

[(L&E) Lighting and Equipment Public Company Limited 💡](https://www.mydevdemosites.com/)

# Datasheet
[L&E LoRa Module V1 Datasheet 📚](https://github.com/Lezgend/LoRaV1-Micropython/blob/main/docs/LoRa-Module-V1.pdf)

# Specifications

## AcSIP S76S 
* Model name: S76S
* Product Desc.: LoRa Wireless Communication Module
* Host Interface: UART
* Temp. Storage -50 to 105 degree Celsius
* Temp. Operating: -40 to 85 degree Celsius
* Humid. Storage: 10 to 95 % (non-condensing)
* Humid. Operating: 5 to 95 % (non-condensing)
* Dimension: 13 mm x 11 mm x 1.14 mm
* Package: LGA
* Supply voltage: 3.3 V (typical)
* Supply current: 5 uA (sleep), 9.6 mA (standby), 17.5 mA (receive), 127 mA (transmit)

Ref: [AcSIP Product brief 📑](https://www.acsip.com.tw/index.php?action=products-detail&fid1=19&fid2=&fid3=&id=79)

## Command Set
[S76S/S78S Commands Set Reference v1.6.5 📓](https://edit.wpgdadawant.com/uploads/news_file/program/2019/35461/tech_files/S7678S_Commands_Set_Reference_1.6.5.pdf)

---

## Neoway G7A

| Frequency bands       | GPS L1/ BDS L1 /GLONASS L1                                                                                                                   |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Operating voltage     | VBAT: 2.7 V to 3.6 V, Typ.: 3.3 V<br>VDD_IO: 2.7 V to 3.6 V, Typ.: 3.3 V<br>VBCKUP: 1.4 V to 3.6 V, Typ.: 3.3 V                            |
| Dimensions            | 10.6 mm x 9.7 mm x 2.2 mm                                                                                                                  |
| Package               | 18-pin LCC                                                                                                                                 |
| Interfaces            | UART x 1<br>1PPS x 1<br>RESERVED x 5<br>V_BACKUP                                                                                           |
| Power consumption     | Capturing: 30 mA @ 3.3 V<br>Track: 28 mA @ 3.3 V<br>Standby: 10 uA @ 3.3 V                                                                 |
| ESD                   | VBAT: ±8 kV /±15 kV<br>GND: ±8 kV / ±15 kV<br>ANT: ±8 kV / ±15 kV<br>Cover: ± 8kV / ±15 kV<br>UART: ±2 kV / ±4 kV<br>Others: ±2 kV / ±4 kV |
| Sensitivity           | Cold-start Capturing: -148 dBm<br>Hold-start Capturing: -156 dBm<br>Re-capturing: -160 dBm<br>Track: -162 dBm                              |
| Operating temperature | -40°C to 85°C                                                                                                                              |
| Storage temperature   | -50°C to 125°C       

Ref: [Neoway G7A Product brief 📑](https://cn.neoway.com/details/product_en/1099.html)

---

# Usage

The pin mapping table for this hardware (L&E LoRa Module V1) and ESP32 with UART2 (UART_ID=2) is as follows:

| L&E LoRa V1 | ESP32   |
|-------------|---------|
| RX          | GPIO 17 |
| TX          | GPIO 16 |
| 5V          | 5V      |
| GND         | GND     |
| R           | GPIO 33 |
| S           | GPIO 32 |

# Micropython class UART Reference

Ref: [class UART](https://docs.micropython.org/en/latest/library/machine.UART.html)

## ESP32
|    | UART0 | UART1 | UART2 |
|----|-------|-------|-------|
| TX |   1   |   10  |   17  |
| RX |   3   |   9   |   16  |

The ESP32 has three hardware UARTs: UART0, UART1 and UART2. They each have default GPIO assigned to them.

Ref: [ESP32 UART 📗](https://docs.micropython.org/en/latest/esp32/quickref.html#uart-serial-bus)

## ESP8266
|    | UART0 | UART1 |
|----|-------|-------|
| TX |   1   |   2   |
| RX |   3   |   8   |

UART0 is bidirectional. \
UART1 is on Pins 2 (TX) and 8 (RX) however Pin 8 is used to connect the flash chip, so UART1 is TX only.

Ref: [ESP8266 UART 📘](https://docs.micropython.org/en/latest/esp8266/quickref.html?highlight=dht#uart-serial-bus)

# Example

## Result when run up the python script (test.py).
```
Which UART ID do you using ?: 2
Which class do you prefer ? (A, C): C
Which port number do you want to use ? (1-223): 10
Data to send (String): HELLO_WORLD
1. Check Module Infomation
2. Auto Config Module
3. Show Key
4. Send Data
5. GPS
6. Quit
Please select your choice:
```

## Result of choice number 1
```
Please select your choice: 1
Roger That!
Command: sip get_hw_model_ver
>> module=S76S ver=v1.6.5
Command: mac get_band
>> 923
Use CTRL-C to stop sending
```

## Result of choice number 2
```
Please select your choice: 2
Roger That!
Starting Reset Factory
Command: sip reset
>> Ok
                             
     ___        _____ _ ____ 
    /   | _____/ ___/(_) __ \
   / /| |/ ___/\__ \/ / /_/ / Tech Co., LTD
  / ___ / /__ ___/ / / ____/   LoRaWAN v1.0.2 Ready
 /_/  |_\___//____/_/_/         (Class A & C)
>> S76S - v1.6.5 - AS923 - Jun 25 2018 - 14:33:19 
Setting up frequency
Command: mac set_ch_freq 0 923200000
>> Ok
Command: mac set_ch_freq 1 923400000
>> Ok
Command: mac set_ch_freq 2 922000000
>> Ok
Command: mac set_ch_freq 3 922200000
>> Ok
Command: mac set_ch_freq 4 922400000
>> Ok
Command: mac set_ch_freq 5 922600000
>> Ok
Command: mac set_ch_freq 6 922800000
>> Ok
Command: mac set_ch_freq 7 923000000
>> Ok
Command: mac set_rx2 2 923200000
>> Ok
Setting up device class
Command: mac set_class C
>> Ok
Command: mac save
>> Ok
Config Module Successfully!
Use CTRL-C to stop sending
```

## Result of choice number 3
You have to use both keys (DevEUI and AppKey) to register and activate your end device on the LoRa Server first before sending any data.
* <b>Note that the DevEUI in this example is hidden for security reasons.</b>
```
Please select your choice: 3
Roger That!
----------For OTAA----------
Command: mac get_deveui
>> 9c65************
Command: mac set_appkey 5c608d4ad87a5d90dd203ccb83af3df2
>> Ok
DevEUI for OTAA Athentication: 9c65************
AppKey for OTAA Athentication: 5c608d4ad87a5d90dd203ccb83af3df2
---------------------------
Use CTRL-C to stop sending
```

## Result of choice number 4
<b>Ctrl + C</b> keyboard shortcut; will interrupt the program.
```
Please select your choice: 4
Roger That!
Command: mac get_join_status
>> unjoined
Command: mac tx ucnf 10 48454c4c4f5f574f524c44
>> not_joined
Command: mac get_join_status
>> accepted
>> joined
Command: mac tx ucnf 10 48454c4c4f5f574f524c44
>> Ok
Command: mac get_join_status
>> mac command (downlink) 0302030001
>> tx_ok
>> joined
Command: mac tx ucnf 10 48454c4c4f5f574f524c44
>> mac command (uplink) 0307
>> Ok
Interrupted!
```

## Result of choice number 5
<b>Ctrl + C</b> keyboard shortcut; will interrupt the program.
```
UTC Timestamp: [11, 25, 26.0]
Date: April 2nd, 2023
Satellites: 8
Altitude: 83.8
Latitude: [16, 28.36162, 'N']
Longitude: 102° 49.52352' E
Horizontal Dilution of Precision 1.5

UTC Timestamp: [11, 25, 26.0]
Date: April 2nd, 2023
Satellites: 8
Altitude: 83.8
Latitude: [16, 28.36162, 'N']
Longitude: 102° 49.52352' E
Horizontal Dilution of Precision 1.5

UTC Timestamp: [11, 25, 26.0]
Date: April 2nd, 2023
Satellites: 8
Altitude: 83.8
Latitude: [16, 28.36162, 'N']
Longitude: 102° 49.52352' E
Horizontal Dilution of Precision 1.5

UTC Timestamp: [11, 25, 26.0]
Date: April 2nd, 2023
Satellites: 8
Altitude: 83.8
Latitude: [16, 28.36162, 'N']
Longitude: 102° 49.52352' E
Horizontal Dilution of Precision 1.5

UTC Timestamp: [11, 25, 26.0]
Date: April 2nd, 2023
Satellites: 8
Altitude: 83.8
Latitude: [16, 28.36162, 'N']
Longitude: 102° 49.52352' E
Horizontal Dilution of Precision 1.5
```

## Result of choice number 6
```
Please select your choice: 6
Roger That!
----------Bye----------
```
