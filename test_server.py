import sys
import cPickle
import math

from SocketServer import BaseRequestHandler, UDPServer


class UDPHandler(BaseRequestHandler):

    def handle(self):
        data = self.request[0]
        socket = self.request[1]

        socket.sendto("server: " + data, self.client_address)
        print data 
        return


class GameServer(UDPServer):
    def __init__(self, server_address, handler_class=UDPHandler):
        UDPServer.__init__(self, server_address, handler_class)
        return


if __name__ == "__main__":
    # host, port = "localhost", 9999
    host, port = "10.12.185.71", 9999
    if len(sys.argv) > 1:
        index = int(sys.argv[1])
        port = port + index
    print port
    server = GameServer((host, port), UDPHandler)
    server.serve_forever()
