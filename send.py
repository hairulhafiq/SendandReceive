import socket

UDP_IP = "192.168.0.105"
UDP_PORT = 5005
MESSAGE = "11"

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "Message: ", MESSAGE

sock = socket.socket(socket.AF_INET,
		     socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))