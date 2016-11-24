import socket
import sys
import numpy as np
import cPickle
import time


HOST, PORT = "localhost", 9999
# HOST, PORT = "10.12.185.71", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def main():
    # data = " ".join(sys.argv[1:])
    # send action
    data = "hello___"
    sock.connect((HOST, PORT))
    sock.send('10')
    for i in range(10):
        time.sleep(3)
        sock.sendall(data + str(i))
    # sock.sendall(data)
    received = sock.recv(1000)
    sock.close()
    print("Sent:     {}".format(data))
    print("Received: {}".format(received))

    return


# def send_msg(sock, msg):
#     # Prefix each message with a 4-byte length (network byte order)
#     msg = struct.pack('>I', len(msg)) + msg
#     sock.sendall(msg)


# def recv_msg(sock):
#     # Read message length and unpack it into an integer
#     raw_msglen = recvall(sock, 4)
#     if not raw_msglen:
#         return None
#     msglen = struct.unpack('>I', raw_msglen)[0]
#     # Read the message data
#     return recvall(sock, msglen)


# def recvall(sock, n):
#     # Helper function to recv n bytes or return None if EOF is hit
#     data = ''
#     while len(data) < n:
#         packet = sock.recv(n - len(data))
#         if not packet:
#             return None
#         data += packet
#     return data

if __name__ == '__main__':
    main()
    # for i in range(1000):
    #     main()
