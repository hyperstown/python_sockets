import socket
import pickle

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())


port = 4441

sct.bind((IP, port))
sct.listen(5)
print(f"Server is running {IP} on port {port}")

class Instructions:
    url = ""
    msg = ""
    additional_param = ""

def action(data):
    decoded_data = pickle.loads(data)
    words = decoded_data.msg.split()
    for i in range(len(words)):
        if words[i] == "I'm":
            words[i] = "Hello"
            words.append("I'm")
            words.append("Dad")
        
    r = " ".join(words)
    #decoded_data.msg += " Welcome to dadjokes.com"
    decoded_data.msg = r
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







