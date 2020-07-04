import socket
import pickle
import base64
import hashlib
import sys

# create a list of all the characters in base64 w/ padding
b64_chars = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=']

def convert(string, type, KEY):
    
	# take a sha512 hash of the key
	hash = hashlib.sha512(KEY).hexdigest()

	# initial cipher is a copy of the base64 characters
	cipher = b64_chars[:]

	# loop over each element in the hash and rearrange the cipher
	for c in hash:
		char_int = int(c, 16)
		pos = 65 * (char_int / 15)

		# move the element to the beginning of the list and reverse the list
		cipher.insert(0, cipher.pop(int(pos)-1))
		cipher = cipher[::-1]

	sbox = {}

	# create the mapping between base64 characters and the rearranged base64 characters
	for i, c in enumerate(b64_chars):
		sbox[c] = cipher[i]

	# if this operation is a decryption, keys/values must be reverse
	if type == 'd':
		   sbox = dict((v, k) for k, v in sbox.items())

	# substitute characters in the string according to the sbox
	for i, c in enumerate(string):
		string[i] = sbox[c]

	return ''.join(string)

def encrypt(string, KEY):
	# base64 encode plaintext and convert to list of characters
	string = [c for c in base64.b64encode(string.encode()).decode()]

	return convert(string, 'e', KEY.encode())

def decrypt(string, KEY):
	string = [c for c in string.strip()]

	return base64.b64decode(convert(string, 'd', KEY.encode())).decode()


# SERVER

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostbyname(socket.gethostname())


port = 4444

sct.bind((IP, port))
sct.listen(5)
print(f"Server is running {IP} on port {port}")

class Instructions:
    url = ""
    msg = ""
    additional_param = ""

def action(data):
    decoded_data = pickle.loads(data)
    if not decoded_data.additional_param:
        decoded_data.msg = "Expected additonal parameters"
    else:
        param = decoded_data.additional_param.split()
        if len(param) < 2:
            decoded_data.msg = "No password given"
        else:
            if param[0] == "e":
                decoded_data.msg = encrypt(decoded_data.msg, param[1])
            elif param[0] == "d":
                decoded_data.msg = decrypt(decoded_data.msg, param[1])
            else:
                decoded_data.msg = "Unknown parameter"
    print("done")
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







