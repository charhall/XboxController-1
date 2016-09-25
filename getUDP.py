import socket

#UDP setup
HOST = '' 
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", PORT))
list = [" "]

#returns UDP data as string list
def getUDP():
    data, addr = s.recvfrom(1024)
    li = []
    li = data.split()
    return li

#main loop, will exit when xbox360 BACK button is pressed
while list[0] != "12":
        list = getUDP()

        #check for D-pad special input
        if(list[0] == "17"):
            print list[0] + " " + list[1] + " " + list[2]

        #check for normal input
        else:
            print list[0] + " " + list[1]

#required to safely close the port
s.close()
