import socket
import pickle

class Instructions:
    url = ""
    msg = ""
    additional_param = ""

def redirect(data):
    data = pickle.loads(data)
    print(data.url)
    dns = {
        "encryption.com": {"192.168.18.2":4444},
        "mylog.com": {"192.168.18.2":4443},
        "givemerandom.com": {"192.168.18.2":4442},
        "dadjokes.com": {"192.168.18.4":4441},
    }

    IP = {}

    for x, y in dns.items():
        if(x == data.url):
            IP = y

    if not IP:
        msg = f"This site is unreachable. The server IP address with the {data.url} website could not be found."
        return pickle.dumps(msg)
    else:
        sct_re = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for x, y in IP.items():
            ip = x
            port = y
        print("Connecting to: ", ip, " on port ", port)
        sct_re.connect((ip, port))
        sct_re.sendall(pickle.dumps(data))
        msg = sct_re.recv(1024)
        sct_re.close()
        return msg









sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())


port = 4445

sct.bind((IP, port))
sct.listen(5)
print(f"Proxy is running {IP} on port {port}")




try:
    while True:
        print("Waiting for clients..")
        clientsocket, address = sct.accept()
        print(f"Connection from {address} has been established")
        data = clientsocket.recv(1024)
        print("Data recived!")
        new_data = redirect(data)
        clientsocket.sendall(new_data)
        clientsocket.shutdown(socket.SHUT_WR)
except KeyboardInterrupt:
    print("Shutting down the server")
except Exception as exc:
    print("Error ocurred: ", exc)

sct.close()







