#import sys;
from server import Server

server = Server("localhost", 8080)
server.run()
