import socket

class Session:

    def __init__(self,serveraddress):
        self.so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.serveraddress = serveraddress
