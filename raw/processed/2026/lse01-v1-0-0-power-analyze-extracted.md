---
title: "Lse01 V1 0 0 Power Analyze (extracted from PDF)"
source_pdf: raw/processed/2026/lse01-v1-0-0-power-analyze.pdf
extracted: 2026-04-18
page_count: 19
note: Machine-extracted text; verify against the PDF for tables, figures, and typography.
---

# Lse01 V1 0 0 Power Analyze

**Source PDF:** [`lse01-v1-0-0-power-analyze.pdf`](./lse01-v1-0-0-power-analyze.pdf) — repo path `/raw/processed/2026/lse01-v1-0-0-power-analyze.pdf`


## Page 1

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1

## Page 2

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
2
目录 
1.Introduction ................................................................................................................................... 3 
2.EU868 Power consumption test results ......................................................................................... 3 
2.1 Deep Sleep Mode ................................................................................................................ 3 
2.2 Watchdog Power ................................................................................................................. 4 
2.3 DR=0,TXP=0 ......................................................................................................................... 5 
2.4 DR=5,TXP=0 ......................................................................................................................... 6 
3. EU868 Power consumption test results （Device connection DS18B20 Temperature and 
humidity sensor） ............................................................................................................................ 7 
3.1 Deep Sleep Mode ................................................................................................................ 7 
3.2 Watchdog Power ................................................................................................................. 8 
3.3 DR=0,TXP=0 ......................................................................................................................... 9 
3.4 DR=5,TXP=0 ....................................................................................................................... 10 
4. US915 Power consumption test results ...................................................................................... 11 
4.1 Deep Sleep Mode .............................................................................................................. 11 
4.2 Watchdog Power ............................................................................................................... 12 
4.3 DR=0,TXP=0 ....................................................................................................................... 13 
4.4 DR=3,TXP=0 ....................................................................................................................... 14 
5. US915 Power consumptio7n test results （Device connection DS18B20 Temperature and 
humidity sensor） .......................................................................................................................... 15 
5.1 Deep Sleep Mode .............................................................................................................. 15 
5.2 Watchdog Power ............................................................................................................... 16 
5.3 DR=0,TXP=0 ....................................................................................................................... 17 
5.4 DR=3,TXP=0 ....................................................................................................................... 18

## Page 3

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
3
1.Introduction 
 This article is a test report for Dragino LSE01 Sensor Node power consumption. It is to provide 
reference for system integrator to install the sensor node.  
With the test result here, system integrator can estimate the battery life time for LSE01. 
 
Hardware version：V2.0 
Software version：V1.0 
 
2.EU868 Power consumption test results 
2.1 Deep Sleep Mode 
Average: 8.6uA.

## Page 4

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
4
 
 
2.2 Watchdog Power 
Max 10mA  Average 4.26506mA in 1ms for every 18 seconds (watchdog period)

## Page 5

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
5
 
 
2.3 DR=0,TXP=0 
Transmit Time: 7s 
Average Current in transmit time: 28.6974mA 
The total current to send a packet is 
     28.6974mA * 7s = 200.8818mA*s 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=0. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current : 0.0086mA*20*60s= (10.32mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 200.8818mA*s 
                                              
So total Average Current is :(200.8818+10.32+0.2843)/(20*60)= 0.1762mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.1762mA * 24 * 365 * y 
 
So Y = 4000/ (0.1762*24*365+80) =2.4(Years)

## Page 6

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
6
 
 
2.4 DR=5,TXP=0 
Transmit Time: 6s 
Average Current in transmit time: 14.6474mA 
The total current to send a packet is 
    14.6474mA *6s = 87.8844mA*s 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=5. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current : 0.0086mA*20*60s= (10.32mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 87.8844mA*s 
                                              
So total Average Current is :(87.8844+10.32+0.2843)/(20*60)= 0.0821mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.0821mA * 24 * 365 * y 
 
So Y = 4000/ (0.0821*24*365+80) =5(Years)

## Page 7

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
7
 
 
3. EU868 Power consumption test results （Device 
connection DS18B20 Temperature and humidity sensor） 
3.1 Deep Sleep Mode 
Average: 9.7uA

## Page 8

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
8
3.2 Watchdog Power 
Max 10mA  Average 4.26506mA in 1ms for every 18 seconds (watchdog period)

## Page 9

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
9
3.3 DR=0,TXP=0 
Transmit Time: 6s 
Average Current in transmit time: 28.7612mA 
The total current to send a packet is  
      28.7612mA * 8s =230.0896 mA 
 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=0. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current : 0.0097mA*20*60s= (11.64mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 87.8844mA*s 
                                              
So total Average Current is :(230.0896+11.64+0.2843)/(20*60)= 0.2017mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.2017mA * 24 * 365 * y 
 
So Y = 4000/ (0.2017*24*365+80) =2.1(Years)

## Page 10

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
3.4 DR=5,TXP=0 
Transmit Time: 7s 
Average Current in transmit time:15.7792mA 
The total current to send a packet is  
      15.7792mA * 7s =110.4544 mA 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=5. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current : 0.0097mA*20*60s= (11.64mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 110.4544mA*s 
                                              
So total Average Current is :(110.4544+11.64+0.2843)/(20*60)= 0.102mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.102mA * 24 * 365 * y 
 
So Y = 4000/ (0.102*24*365+80) =4.1(Years)

## Page 11

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
4. US915 Power consumption test results 
4.1 Deep Sleep Mode 
Average: 8uA

## Page 12

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
4.2 Watchdog Power 
Max 10mA  Average 4.26506mA in 1ms for every 18 seconds (watchdog period)

## Page 13

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
4.3 DR=0,TXP=0 
Transmit Time: 6s 
Average Current in transmit time: 20.3222mA 
The total current to send a packet is  
     20.3222mA * 6s =121.9332 mA*s 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=0. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current : 0.008mA*20*60s= (9.6mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 121.9332mA*s 
                                              
So total Average Current is :(121.9332+9.6+0.2843)/(20*60)= 0.1098mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.1098mA * 24 * 365 * y 
 
So Y = 4000/ (0.1098*24*365+80) =3.8(Years)

## Page 14

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
 
 
4.4 DR=3,TXP=0 
Transmit Time: 6s 
Average Current in transmit time: 15.2585mA 
The total current to send a packet is  
     15.2585mA * 6s =91.551 mA*s 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=3. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current : 0.008mA*20*60s= (9.6mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 91.551mA*s 
                                              
So total Average Current is :(91.551+9.6+0.2843)/(20*60)= 0.0845mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.0845mA * 24 * 365 * y 
 
So Y = 4000/ (0.0845*24*365+80) =4.8(Years)

## Page 15

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
 
 
5. US915 Power consumptio7n test results （Device 
connection DS18B20 Temperature and humidity sensor） 
5.1 Deep Sleep Mode 
 
Average: 9uA

## Page 16

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
 
 
 
5.2 Watchdog Power 
Max 10mA  Average 4.26506mA in 1ms for every 18 seconds (watchdog period)

## Page 17

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
 
 
 
5.3 DR=0,TXP=0 
Transmit Time: 7s 
Average Current in transmit time: 20.6362mA 
The total current to send a packet is  
     20.6362mA * 7s =144.4534 mA*s 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=0. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current :0.0088mA*20*60s = (10.56mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 144.4534mA*s 
                                              
So total Average Current is :(10.56 + 0.2843 +144.4534)/(20*60)= 0.1294mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.1294mA * 24 * 365 * y 
 
So Y =4000/ (0.1294 *24*365+80) = 3.2(Years)

## Page 18

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
 
 
 
 
 
5.4 DR=3,TXP=0 
Transmit Time: 7s 
Average Current in transmit time: 16.1187mA 
The total current to send a packet is  
      16.1187mA * 7s =112.8309 mA*s 
 
Analyze Result  
With Above test result and battery info, we can estimate the battery life.  
and let is working in set up DR=3. Transmit one uplink every 20 minutes.  
 
✓ 
Deep Sleep Mode Current :0.0088mA*20*60s = (10.56mA*s) 
✓ 
Watch Dog Current: 0.001s*4.2651mA*(20*60s/18s) = (0.2843mA*s) 
✓ 
The total current to send a packet is : 112.8309mA*s 
                                              
So total Average Current is :(10.56 + 0.2843 +112.8309)/(20*60)= 0.103mA.  
The battery used in LSE01 is 4000mAh and of stable voltage in the most of life. With considering a 
max 2% discharge rate from the battery spec.So the battery life is y. so  
 
4000(1 - 2%*y) = 0.103mA * 24 * 365 * y 
 
So Y =4000/ (0.103 *24*365+80) = 4(Years)

## Page 19

www.dragino.com 
LSE01 LoRaWAN Soil Moisture & EC Sensor User Manual 
1
