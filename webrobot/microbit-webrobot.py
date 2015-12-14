from microbit import *

# Gets direction of accelerometer and convert into url 
# which is sent via serial port to a PC proxy
# The PC performs a wget and confirms response

# time to wait betweeen samples - in ms
delay = 500
# translate to left sharp, left gentle, no change, right gentle anything > right sharp
x_positions = [-500, -200, 200, 500]
# y has more positions to allow finer control, but only displayed as 5 steps on led display
# tranlate to 10 forward, 8 , 6 , 4, stop, 4, 6, 8, 10 reverse
y_positions = [-500, -400, -300, -200, 200, 300, 400, 500]

# Read from accelerometer and convert into a direction
# returns x (-2 to 2) y (-4 to 4)
def get_direction():
	x, y, z = accelerometer.get_values()
	# send to serial port
	# print ("Values are x: " + str(x) + " y: " + str(y) + " z: " + str(z))

	# convert x into -2 to +2
	# First set to the top end of the range (if other conditions not met)
	x_val = 2
	for i in range (0, 4) :
		if (x < x_positions[i]):
			x_val = i - 2
			break
	y_val = 4
	for i in range (0, 8) :
		if (y < y_positions[i]):
			y_val = i - 4
			break
	# convert y into + for forward and - for backwards
	y_val = y_val * -1
	
	return (x_val, y_val)
	

# shows status as a dot on the microbit display
def show_status(x, y):
	# show x and y on LED display
	# set all to 0
	display.clear()
	display.set_pixel(x+2, int(y* -0.5)+2, 9)
	
	
# if forward 1 then increase to 20 (or maintain speed), forward 2 = +10 (to 100)
def speed_change(speed, y) :
	return speed
	

	
def run():
	# Start speed at 0
	speed = 0
	while True:
		x, y = get_direction()
		show_status (x, y)
		print ("X " + str (x) + " , Y " + str(y))
		speed = speed_change(speed, y)
		
		sleep (delay)
	
run()