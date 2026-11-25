"""
Ex. No. 5 - IoT Sensor Data Analysis Using NumPy

Aim:
    To analyze IoT sensor readings using NumPy arrays and perform
    mathematical and statistical operations such as mean, median, minimum,
    maximum, standard deviation and threshold analysis.
"""
import numpy as np

# Temperature readings (in degree Celsius) collected from an IoT sensor
sensor_data = np.array([24.5, 25.1, 26.3, 27.0, 28.2,
                        29.1, 27.8, 26.5, 25.7, 30.2])

print("Sensor Data:", sensor_data)
print("Mean      :", round(np.mean(sensor_data), 2))
print("Median    :", round(np.median(sensor_data), 2))
print("Minimum   :", np.min(sensor_data))
print("Maximum   :", np.max(sensor_data))
print("Std. Dev. :", round(np.std(sensor_data), 2))

# Threshold analysis: boolean masking selects only the high readings
threshold = 28.0
high_values = sensor_data[sensor_data > threshold]
print("Values above", threshold, ":", high_values)
