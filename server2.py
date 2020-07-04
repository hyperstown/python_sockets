import socket
import pickle
import random

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())


port = 4442

sct.bind((IP, port))
sct.listen(5)
print(f"Server is running {IP} on port {port}")

class Instructions:
    url = ""
    msg = ""
    additional_param = ""

def action(data):
    decoded_data = pickle.loads(data)
    n = random.randint(-5000,50000)
    n = str(n)
    decoded_data.msg = "Welcome to givemerandom.com, here is your number " + n
    #print("done")
    return pickle.dumps(decoded_data.msg)


try:
    while True:
        clientsocket, address = sct.accept()
        print(f"Connection from {address} has been established")
        data = clientsocket.recv(1024)
        new_data = action(data)
        print("Data recived")
        
        clientsocket.sendall(new_data)
        clientsocket.shutdown(socket.SHUT_WR)
except KeyboardInterrupt:
    print("Shutting down the server")
except Exception as exc:
    print("Error ocurred: ", exc)

sct.close()







