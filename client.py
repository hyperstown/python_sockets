import socket
import pickle

class Instructions:
    url = ""
    msg = ""
    additional_param = ""

instruct1 = Instructions()


while True:
    print("LIST:")
    print("encryption.com")
    print("mylog.com")
    print("givemerandom.com")
    print("dadjokes.com")
    user_input = input("Please enter url or 'exit':  ")
    if(user_input == "exit"):
        break
    instruct1.url = user_input

    user_input = input("Please enter message or 'exit'. You can leave it empty: ")
    if(user_input == "exit"):
        break
    instruct1.msg = user_input

    user_input = input("Please enter additional parameters or 'exit'. You can leave it empty:  ")
    if(user_input == "exit"):
        break
    instruct1.additional_param = user_input

    msg = pickle.dumps(instruct1)
    sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sct.connect(("192.168.18.2", 4445))

    sct.sendall(msg)

    msg = sct.recv(1024)
    msg1 = pickle.loads(msg)
    print(msg1)
    sct.close()