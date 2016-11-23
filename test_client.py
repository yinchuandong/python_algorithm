import socket
import sys
import numpy as np
import cPickle
import time


# HOST, PORT = "10.100.228.240", 9999
HOST, PORT = "10.12.185.71", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def main():
    # data = " ".join(sys.argv[1:])
    # send action
    sock.sendto('fuck you', (HOST, PORT))

    data = sock.recv(1000) 
    print data


    return


if __name__ == '__main__':
    main()
    # for i in range(1000):
    #     main()
