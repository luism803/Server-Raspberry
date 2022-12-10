/*PRUEBA*/

function saludar(){
    console.log("hola!");
}

// function saludar(){
//     window.location.href = 'https://rarbg.to/';
// }

/*UTILIDADES*/

function sleep(milliseconds){
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

function waitRandom(t=5000){
    console.log("esperando")
    let time = Math.floor(Math.random() * 2000) + t;
    console.log("esperado", time)
    sleep(time);
}

/*INTERACCION*/

function seleccionarIdValue(id, valor){
    let elemento = elementoIdWait(id);
    console.log(elemento)
    elemento.value = valor;
}

function elementoIdWait(id){
    let elemento = undefined;
    let contador = 0;
    while(!elemento){
        elemento = elementoId(id);
        if(!elemento)
            waitRandom();
        if(contador>5)
            return undefined;
        contador++;
    }
    return elemento
}

function pulsarBotonId(id){
    let elemento = elementoIdWait(id);
    elemento.click();
}

function elementoId(id){
    return document.getElementById(id);
}