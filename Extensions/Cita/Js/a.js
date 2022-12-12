console.log("iniciado")

var bucle = setInterval(function(){
    console.log("started")
    selectTextId("provincia", "Murcia")
    clearInterval(bucle);
},5000);
