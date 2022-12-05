const ws = new WebSocket("ws://localhost:8080/");

ws.addEventListener("open", e => {
    console.log("Conexión establecida.");
    ws.send("Conectado");
});

ws.addEventListener("message", message => {
    var data = message.data;
    console.log(data);
    ws.send("Recibido");
});
