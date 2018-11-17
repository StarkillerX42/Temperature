import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
times = []
temps = []
with open("temp_log.txt", "r") as fil:
    for i, line in enumerate(fil):
        t, temp = line.split(",")
        times.append(Time(t).plot_date)
        temps.append(float(temp))
times = np.array(times)
temps = np.array(temps)
fig = plt.figure(figsize=(10, 6))
ax = fig.gca()
ax.plot_date(times, temps,"o", tz=None,
             xdate=True, ydate=False, drawstyle="steps-post")
ax.set_title("CPU Temperature Over Time")
ax.set_xlabel("Date")
ax.set_ylabel(u"Temperature (\N{DEGREE SIGN})")
fig.savefig("temps.png")
