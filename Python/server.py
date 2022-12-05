from websocket_server import WebsocketServer

class Server():

    def __init__(self, host, port):
        self.server = WebsocketServer(host, port)

    def connected(client, server):
        print("Conectado")
        self.listado_clientes.pull(client)

    def reciveMessage(client, server, message):
        print("mensaje: "+message)
        if message == "Recibido":
            print("Todo ha salido como se esperaba")
        else:
            server.send_message(client, "Mensaje recibido")
    
    def run(self):
        print("Starting...")
        server.set_fn_new_client(connected)
        server.set_fn_message_received(reciveMessage)
        server.run_forever()