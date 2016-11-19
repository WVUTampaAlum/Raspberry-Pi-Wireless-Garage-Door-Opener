# Uses GPIO 21 ONLY for garage door communication

import RPi.GPIO as gpio
from sys import argv
import time

SleepTime=2

#gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(21,gpio.OUT)

# check for user input
if len(argv) > 1:
  userinput= argv[1] 
else:
  userinput= ''

print "\n Garage Door Activated."
target = open("/home/pi/code/logs/activateGarageDoor.log", 'a')


try:
  gpio.output(21,True)
  time.sleep(SleepTime)
  gpio.output(21,False)
  currentTime = time.ctime()
  line1 = "%s  Garage Door Activated by %s" % (currentTime, userinput)
  target.write(line1)
  target.write("\n")
  target.close()


except:
   # this catches ALL other exceptions including errors.
   # You won't get any error messages for debugging
   # so only use it once your code is working
   print "Other error or exception occurred!"

finally:
   print "\n Finished\n"
   gpio.cleanup()

