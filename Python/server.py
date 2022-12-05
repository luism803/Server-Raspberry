from websocket_server import WebsocketServer

print("starting...")

server = WebsocketServer("localhost", 8080)

def connected(client, server):
    print("Conectado")

def reciveMessage(client, server, message):
    print(message)
    if message == "Recibido":
        print("Todo ha salido como se esperaba")
    else:
        server.send_message(client, "Mensaje recibido")
        
server.set_fn_new_client(connected)
server.set_fn_message_received(reciveMessage)
server.run_forever()
