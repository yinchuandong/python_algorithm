import socket
import sys
import threading
import signal
from PIL import Image
from io import BytesIO
import base64
import random
import json


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 9999)
sock.bind(server_address)
sock.listen(1)

client_threads = []
stop_requested = False


def signal_handler(signal_, frame_):
    print 'You pressed Ctrl+C !'
    global stop_requested
    stop_requested = True
    return


def handler(connection, client_address):
    try:
        print 'client connected:', client_address
        while not stop_requested:
            data = recv_msg(connection)
            if data:
                print 'received:', len(data)
                data = json.loads(data)
                image = Image.open(BytesIO(base64.b64decode(data['img']))).convert('RGB')
                imgname = 'test_%d.png' % random.randint(0, 10000)
                image.save(imgname)
                # print 'received "%s"' % data
                action = json.dumps({'left': True}).zfill(100)
                connection.sendall(action)
            else:
                break
    finally:
        connection.close()
    return


def main():
    while True:
        print 'waiting for a connection'
        connection, client_address = sock.accept()
        client = threading.Thread(target=handler, args=(connection, client_address))
        client_threads.append(client)
        if len(client_threads) == 1:
            break

    signal.signal(signal.SIGINT, signal_handler)

    for thread in client_threads:
        thread.start()

    print 'Press Ctrl+C to stop'
    signal.pause()

    print 'Now saving data....'
    for t in client_threads:
        t.join()
    return


def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 20)
    if not raw_msglen:
        return None
    msglen = int(raw_msglen)
    return recvall(sock, msglen)


def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = ''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


if __name__ == '__main__':
    main()
