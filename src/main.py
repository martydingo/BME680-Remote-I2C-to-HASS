# Import BME680 Library
import bme680

# Define the climate climateSensor here...
climateSensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)

# Configure all the sampling! 
climateSensor.set_humidity_oversample(bme680.OS_2X)
climateSensor.set_pressure_oversample(bme680.OS_4X)
climateSensor.set_temperature_oversample(bme680.OS_8X)
climateSensor.set_filter(bme680.FILTER_SIZE_3)
climateSensor.set_gas_status(bme680.ENABLE_GAS_MEAS)