import datetime
import os
try:
    now = datetime.datetime.now()
    print("Temperature recorded at {}".format(now))
    temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    temp = float(temp.split("=")[1].split("'")[0])
    # print(u"    Temperature: {:.1f}\N{DEGREE SIGN}".format(temp))
    temppath = os.path.join(os.path.dirname(
             os.path.abspath(__file__)), "temp_log.txt")
    with open(temppath, "a") as log:
        log.write(u"{},  {:.1f}\n".format(now, temp))
    print("    Temperature written")
except Exception as e:
    print(e)
