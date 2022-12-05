from websocket_server import WebsocketServer

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
            self.server.send_message(client, "Mensaje recibido")
    
    def run(self):
        print("Starting...")
        self.server.set_fn_new_client(self.connected)
        self.server.set_fn_message_received(self.reciveMessage)
        self.server.run_forever()
