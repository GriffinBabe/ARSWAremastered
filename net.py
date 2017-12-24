import socket
from threading import Thread
from Player import Player

class Session(Thread):

    #Thread contstruction
    def __init__(self,serveraddress,players,player):
        Thread.__init__(self)
        self.players = players
        self.player = player
        self.so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.serveraddress = serveraddress #No need to bind as client

    def run(self):
        while True:
            data, server = self.so.recvfrom(4096) #And not recv(...) as we are client
            self.parse(data)

    def send(self,data):
        #print("Sending to server: "+data.decode("utf-8"))
        self.so.sendto(data,self.serveraddress)

    def moove(self):
        datastring = "MV-"+self.player.username+"-"+str(self.player.x)+"-"+str(self.player.y)\
                     +"-"+str(self.player.dx)+"-"+str(self.player.dy)+"-"+str(self.player.direction)
        self.send(datastring.encode("utf-8"))

    def parse(self,data):
        """Reads the data and acts about it."""
        PLAYER_CONNECTION = "CO"
        PLAYER_DISCONNECTION = "DC"
        PLAYER_MOOVE = "MV"

        stringdata = data.decode("utf-8")
        #print("From server: "+stringdata)
        listdata = stringdata.split("-")
        head = listdata[0]

        if listdata[1] == self.player.username: #Doesn't act bc the message had been sent by this client
            #print("Message coming from me. Ingnoring.")
            return

        if head == PLAYER_CONNECTION:
            for player in self.players: #Compares with every username as we don't want to add a new one
                if player.username == listdata[1]:
                    player.online = True
                    return
            print("New player created: "+listdata[1])
            self.players.append(Player(listdata[1])) #Adds a new Player to the game if there is no match

        if head == PLAYER_DISCONNECTION:
            for player in self.players:
                if player.username == listdata[1]:
                    player.online = False
                    print("Player disconnected: "+listdata[1])
                    return

        if head == PLAYER_MOOVE: #Sets the player x, y, dx and dy info.
            for player in self.players:
                if player.username == listdata[1]:
                    player.x = listdata[2]
                    player.y = listdata[3]
                    player.dx = listdata[4]
                    player.dy = listdata[5]
                    player.direction = listdata[6]

    def getplayer(self, username):
        for p in self.players:
            if p.username == username:
                return p
