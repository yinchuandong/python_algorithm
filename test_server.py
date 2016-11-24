import socket
import sys
import threading
import signal


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
        header = connection.recv(1)
        print header, '-------header-----'
        while not stop_requested:
            data = connection.recv(16)
            print 'received "%s"' % data
            if data:
                connection.sendall(data)
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
        if len(client_threads) == 2:
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


if __name__ == '__main__':
    main()
