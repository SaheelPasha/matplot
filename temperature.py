import numpy as np
import matplotlib.pyplot as plt
dates = ["JUL11", "JUL12", "JUL13", "JUL14", "JUL15", "JUL16", "JUL16", "JUL18", "JUL19", "JUL5"]
temperature = [28, 28, 28, 29, 29, 29, 29, 27, 28, 20]
wind = [23, 25, 23, 18, 19, 18, 21, 22, 23, 21]
ypos = np.arange(len(dates))
plt.bar(ypos - 0.2, temperature, color='r', width=0.4, label="Temperature")
plt.bar(ypos + 0.2, wind, color='b', width=0.4, label="Wind")
plt.xticks(ypos, dates)
plt.xlabel("Dates")
plt.ylabel("Temperature and Wind")
plt.title("Temperature and Wind Speed")
plt.legend()
plt.show()
