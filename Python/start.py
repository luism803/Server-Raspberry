#import sys;
from server.py import Server

server = Server("localhost", 8080)
server.run()