// var el = document.getElementById("form")
// console.log("sin", el)
// console.log("con", elementoId("form"))
// console.log("start")
// var el = document.getElementById('form')
// el.value = "/icpco/citar?p=3&locale=es";
function firstPage(){
    seleccionarIdValue('form', "/icpco/citar?p=3&locale=es");
    waitRandom(3000);
    pulsarBotonId("btnAceptar");
}

function secondPage(){
    seleccionarIdValue("tramiteGrupo[1]", "4301");
    waitRandom(3000);
    pulsarBotonId("btnAceptar");
}

function thirdPage(){
    pulsarBotonId("btnEntrar");
}

function fourthPage(cliente){
    escribir_id("txtIdCitado", cliente.pasaporte)
    escribir_id("txtDesCitado", cliente.nombre)
    escribir_id("txtAnnoCitado", cliente.anyo)
    seleccionar_id("txtPaisNac", cliente.pais)
    pulsarBotonId("btnEnviar");
}

function fifthPage(){
    pulsarBotonId("btnEnviar")
}
// sleep(1000)
// document.getElementById('form').value = "/icpco/citar?p=3&locale=es";
// sleep(3000)
// document.getElementById("btnAceptar").click();