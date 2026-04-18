The Telemetry Module provides four types of data over the mesh: Device metrics (Battery Level, Voltage, Channel Utilization and Airtime) from your Meshtastic device, Environment Metrics, Air Quality Metrics, and Health metrics (Heart rate, Oxygen Saturation and body temperature).

> [!-secondary] -secondary
> note
> 
> Health telemetry sensor support and configuration options are available only by compiling firmware with the required macros enabled.

Supported sensors connected to the I2C bus of the device will be automatically detected at startup. The Environment Telemetry, Air Quality, and Health Telemetry modules must be enabled for them to be instrumented and their readings sent over the mesh.

### Currently Supported Sensor Types

| Sensor | I <sup>2</sup> C Address | Data Points |
| --- | --- | --- |
| AHT10, AHT20 | 0x38 | Temperature and humidity |
| BMP085 | 0x76, 0x77 | Temperature and barometric pressure |
| BMP180 | 0x76, 0x77 | Temperature and barometric pressure |
| BMP280 | 0x76, 0x77 | Temperature and barometric pressure |
| BME280 | 0x76, 0x77 | Temperature, barometric pressure and humidity |
| BMP388 | 0x76, 0x77 | Barometric pressure, Temperature |
| BMP390 | 0x76, 0x77 | Barometric pressure, Temperature |
| BME68x | 0x76, 0x77 | Temperature, barometric pressure, humidity and air resistance |
| DPS310 | 0x76, 0x77 | Barometric pressure, Temperature |
| MCP9808 | 0x18 | Temperature |
| INA219 | 0x40, 0x41, 0x43 | Current and Voltage |
| INA226 | 0x40, 0x41, 0x43 | Current and Voltage |
| INA260 | 0x40, 0x41, 0x43 | Current and Voltage |
| INA3221 | 0x42 | 3-channel Current and Voltage |
| LPS22 | 0x5D, 0x5C | Barometric pressure |
| SHTC3 | 0x70 | Temperature and humidity |
| SHT31 | 0x44, 0x45 | Temperature and humidity |
| SHT4X | 0x44, 0x45 | Temperature and humidity |
| OPT3001 | 0x44, 0x45 | Light intensity |
| VEML7700 | 0x10 | Light intensity |
| TSL2591 | 0x29 | Light intensity |
| LTR390UV | 0x53 | UV Light intensity |
| RCWL9620 | 0x57 | Ultrasonic Distance Sensor |
| PMSA003I | 0x12 | Concentration units by size and particle counts by size |
| DFROBOT\_LARK | 0x42 | Temperature, barometric pressure, humidity, wind direction, wind speed |
| DFROBOT\_RAIN | 0x1d | Tip Bucket Rain counter |
| RadSens | 0x66 | Radio Dosimeter |
| MAX30102 | 0x57 | Heart Rate, Oxygen Saturation, and body temperature |
| MLX90614 | 0x5A | Body temperature |
| MLX90632 | 0x3A | Body temperature |
| NAU7802 | 0x2A | 24-Bit differential ADC for Wheatstone bridge |

## Module Config Values

### Environment Telemetry Enabled

Enable the Environment Telemetry (Sensors).

### Environment Metrics Update Interval

How often we should send Environment(Sensor) Metrics over the mesh.

Default is `1800` seconds (30 minutes).

> [!-secondary] -secondary
> note
> 
> Health telemetry options are available only when compiling firmware with the required macros enabled.

### Device Metrics Update Interval

How often we should send Device Metrics over the mesh.

Default is `1800` seconds (30 minutes).

Device Metrics to a connected client app will always be sent once per minute, regardless of this setting.

### Environment Screen Enabled

Show the environment telemetry data on the device display.

Default is `false`.

### Display Fahrenheit

The sensor is always read in Celsius, but the user can opt to display in Fahrenheit (on the device display only) using this setting.

Default is `false`.

### Air Quality Enabled

This option is used to enable/disable the sending of air quality metrics from an attached supported sensor over the mesh network.

Default is `false`.

### Air Quality Interval

This option is used to configure the interval (in seconds) that should be used to send air quality metrics from an attached supported sensor over the mesh network.

Default is `1800` seconds (30 minutes).

### Power Metrics Enabled

This option is used to enable/disable the sending of power telemetry as gathered by an attached supported voltage/current sensor. Note that this does not need to be enabled to monitor the voltage of the battery.

Default is `false`.

### Power Metrics Interval

This option is used to configure the interval (in seconds) that should be used to send power metrics from an attached supported sensor over the mesh network.

### Health Telemetry Enabled

This option is used to enable/disable the sending of health data from an attached supported sensor over the mesh network.

Default is `false`.

### Health Telemetry Interval

This option is used to configure the interval (in seconds) that should be used to send health data from an attached supported sensor over the mesh network.

Default is `1800` seconds (30 minutes).

## Telemetry Config Client Availability

- Android
- Apple
- CLI
- Web

#### Apple

> [!-info] -info
> info
> 
> All telemetry module config options are available on iOS, iPadOS and macOS at Settings > Module Configuration > Telemetry (Sensors).

## Examples

### RAK 4631 with BME680 Environment Sensor

Setup of a RAK 4631 with Environment Sensor

[![](https://meshtastic.org/img/hardware/rak/RAK4631_with_EnvSensor.webp)](https://meshtastic.org/assets/files/RAK4631_with_EnvSensor-c7fcd4fea9aba4ef7b132b4699696278.webp/)

Requirements:

- RAK4631
- Environment Sensor

Steps:

- configure the device:
```shell
meshtastic --set telemetry.environment_measurement_enabled true --set telemetry.environment_screen_enabled true --set telemetry.environment_display_fahrenheit true
```

> [!-success] -success
> tip
> 
> While the above values serve as an example and can be modified to fit your specific needs, it is advisable to chain multiple commands together, as demonstrated in the example. This approach will minimize the number of necessary reboots.

- Device will reboot after command is sent.
- When the device boots again it should say "Telemetry" and it may show the sensor data
- If this does not appear to have any effects, run:
```shell
meshtastic --noproto
```

And examine the serial logs for Telemetry diagnostic information.

## Supporting Additional Sensors

### Environment Metrics

The environment metrics in the telemetry module supports a limited amount of fields as they are stored in memory on the device. Support for sensors that provide one or more of the following fields can potentially be added to the main firmware provided there is a GPL licensed library for us to include to support it, and the library size is not prohibitive.

### Supporting Other Sensor types

For other interesting sensor types and use cases we need to add a portnum for more generic telemetry packets and a second MCU will be required to interact with the sensor and process the data to be sent over the mesh. This data will not be stored in the nodedb on the device.