"""
Interactive script with the L&E LoRa Module Version 1
Write in MicroPython by Warayut Poomiwatracanont MAR 2023
Test on ESP32 with L&E LoRa Module Version 1
"""
from LoRaV1 import AcSIP_S76S
import gc

gc.enable()
gc.collect()
      
__UART = int(input("Which UART ID do you using ?: "))
__DEVCLASS = str(input("Which class do you prefer ? (A, C): "))
__PORT_NUM = str(input("Which port number do you want to use ? (1-223): "))
__DATA = str(input("Data to send (String): "))

LoRaV1 = AcSIP_S76S(uart_id=__UART, dev_class=__DEVCLASS, port_num=__PORT_NUM, data=__DATA)
    
try:
    while True:
        print()
        LoRaV1.doChoice() 
        print("Use CTRL-C to stop sending\n")
except KeyboardInterrupt:
    print("Interrupted!")
    LoRaV1.setLoRa()
    pass
