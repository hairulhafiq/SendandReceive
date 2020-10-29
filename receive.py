import socket
import RPi.GPIO as gpio
import time
import fr

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(11,gpio.OUT)
gpio.setwarnings(False)
gpio.setup(19,gpio.OUT)
gpio.setwarnings(False)

UDP_IP = "192.168.0.105"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

gpio.output(11, False)
gpio.output(19, False)

while True:
	data, addr = sock.recvfrom(1024)
	print "received message: ", data
	data = int(data)
	gpio.output(data,True)
	time.sleep(0.3)
	gpio.output(data,False)
#	fr.fr()