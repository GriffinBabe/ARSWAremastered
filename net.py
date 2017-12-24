import socket
from threading import Thread

class Session(Thread):

    #Thread contstruction
    def __init__(self,serveraddress):
        Thread.__init__(self)
        self.so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.serveraddress = serveraddress #No need to bind as client

    def run(self):
        while True:
            print("Waiting for packets...")
            data, server = self.so.recvfrom(4096) #And not recv(...) as we are client
            print(data)

    def send(self,data):
        print("try to send "+data.decode("utf-8"))
        self.so.sendto(data,self.serveraddress)