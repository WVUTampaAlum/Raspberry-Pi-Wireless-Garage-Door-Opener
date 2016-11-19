# Raspberry-Pi-Wireless-Garage-Door-Opener

The single python script will activate a wireless garage door opener.  This will allow you to open and close your garage door from a raspberry pi.  If you have an extra wireless garage door opener you simply hard wire the raspberry pi into the opener.  This will supply 5v to the wireless opener and send the signal from pi on gpio 21 to the opener.  

Wiring Pi to Wireless Garage Opener.  Colors listed are simply for pictures of my setup. <br>
Pi 3v3 (white) to Positive Battery Post on Wireless garage door controller
Pi Neg (gray)  to Negative Battery Post on Wireless garage door controller
Pi GPIO 21 (orange) to Activing switch post on wireless garage door opener.  You might have to test out which 'side' of the switch works for you.  


The youtube video does not correctly show how I have now wired the pi into the garage door opener.  I have slightly changed the wiring from my original because it would sometimes not work as it seemed to need to charge up the caps on the wireless opener.  My new wiring method works 100% of the time.  The ONLY time I have issues is if I am switching between wifi and phone data and I am trying to run the script.

Activating from worldwide on a smartphone.
Use tasker app along with paid ssh tasker add on.  Simply create a new task and call the python script.
Example:  sudo python /home/pi/code/activateGarageDoor.py MyCellPhone

The activateGarageDoor script logs every call made to it.  You can either send a parameter or not.  Example calls to script.

sudo python /home/pi/code/activateGarageDoor.py MyCellPhone
sudo python /home/pi/code/activateGarageDoor.py WifesCellPhone
sudo python /home/pi/code/activateGarageDoor.py MyTablet
sudo python /home/pi/code/activateGarageDoor.py 

