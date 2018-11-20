import socket
import threading

HOST = '127.45.43.1'
LPORT = 12345
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
try:
    server.bind((HOST ,80))
    server.listen(5)
    print("The listener is open")
except:
    print("The lister has failed")






def waitformessage():
        while True:
            try:
                checkterm = clientConnect.recv(1096)
                print(" User:" , checkterm.decode("utf-8"))
            except:
                delay = True



def sendmessage():
    ThreadB = threading.Thread(target=waitformessage)
    ThreadB.start()

    while True:
        try:
            message = input()
            clientConnect.sendall(bytes(message, 'utf-8'))
        except:
            print("Message Failed")


clients = 0
while clients < 6 :
    clientConnect , address = server.accept()
    print("A client with ip " , address , "connected")
    clients = 12



ThreadA = threading.Thread(target=sendmessage)

ThreadA.start()
ThreadA.join()

wait = input("Press enter to exit")


#message = input("Please type your message: ")
#clientConnect.sendall(bytes(message, 'utf-8'))

#create an INET, STREAMing socket
#serversocket = socket.socket(
#    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
#serversocket.bind((socket.gethostname(), 80))
#become a server socket
#serversocket.listen(5)
