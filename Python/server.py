from websocket_server import WebsocketServer
import json

class Server():

    def __init__(self, host, port):
        self.server = WebsocketServer(host, port)

    def connected(self, client, server):
        print("Conectado")

    def reciveMessage(self, client, server, message):
        print("mensaje: "+message)
        if message == "Recibido":
            print("Todo ha salido como se esperaba")
        else:
            # a Python object (dict):
            x = {
            "name": "John",
            "age": 30,
            "city": "New York"
            }
            # convert into JSON:
            y = json.dumps(x)
            self.server.send_message(client, y)
    
    def run(self):
        print("Starting...")
        self.server.set_fn_new_client(self.connected)
        self.server.set_fn_message_received(self.reciveMessage)
        self.server.run_forever()
