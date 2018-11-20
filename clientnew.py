import socket
import threading




client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server = "127.45.43.1"
client.connect((server,80))
test = False
while test == True:
    message = client.recv(1048)

    if message:
        print(message.decode("utf-8") )
        test = False


def waitformessage():
        while True:
            try:
                checkterm = client.recv(1096)
                print(" User:" ,checkterm.decode("utf-8"))
            except:
                delay = True



def sendmessage():
    ThreadB = threading.Thread(target=waitformessage)
    ThreadB.start()

    while True:
        try:
            message = input()
            client.sendall(bytes(message, 'utf-8'))
        except:
            print("Message Failed")




ThreadA = threading.Thread(target=sendmessage)

ThreadA.start()
ThreadA.join()

    #p2.start()


#    p1.start()





wait = input("Press enter to exit")
