import socket
import pickle

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())


port = 4443

sct.bind((IP, port))
sct.listen(5)
print(f"Server is running {IP} on port {port}")

class Instructions:
    url = ""
    msg = ""
    additional_param = ""

def action(data):
    decoded_data = pickle.loads(data)
    if decoded_data.additional_param:
        f=open("log.txt", "r")
        if f.mode == 'r':
            contents = f.read()
            decoded_data.msg = contents
    else:
        f = open("log.txt", "a+")
        decoded_data.msg += " \n"
        f.write(decoded_data.msg)
        f.close()
        decoded_data.msg = "Your data has been saved! Thanks for using mylog.com"
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







