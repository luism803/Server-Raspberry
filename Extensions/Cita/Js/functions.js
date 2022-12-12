function iniciar(){
    tTrabajo = 5000;
    tActual = 0;
    work = false;
}

function newValueId(id,valor){
    document.getElementById(id).value = valor;
}

function newPulsarId(id){
    document.getElementById(id).click();
}

function loop(fun){
    if(tActual>tTrabajo && !work){
        try {
            fun();
            work = true;
        } catch (error) {
            console.log("ha ocurrido un error");
            tTrabajo = tActual + 5000;
        }
    }
    tActual += 500;
}

function newFirstPage(){
    loop(function(){
        newValueId('form', "/icpco/citar?p=3&locale=es");
        newPulsarId("btnAceptar");
    });
}

function newSecondPage(){
    loop(function(){
        newValueId("tramiteGrupo[1]", "4031");
        newPulsarId("btnAceptar");
    });
}

function newThirdPage(){
    loop(function(){
        newPulsarId("btnEntrar");
    });
}

function newFourthPage(){
    loop(function(){
        newValueId("txtIdCitado", "51358156F")
        newValueId("txtDesCitado", "WALTER WAIT")
        newValueId("txtAnnoCitado", "1985")
        selectTextId("txtPaisNac", "FRANCIA")
        newPulsarId("btnEnviar");
    });
}

function newFifthPage(){
    loop(function(){
        newPulsarId("btnEnviar")
    });
}

function getArrText(element){
    var arrText = [];
    for(var i=0; i<element.options.length; i++){
        arrText.push(element.options[i].text)
    }
    return arrText;
}

function selectTextId(id, text){
    var element = document.getElementById(id);
    var arrText = getArrText(element);
    var pos = arrText.indexOf(text);
    if(pos != -1)
        element.value = element.options[pos].value;
    else
        alert("No exite el texto buscado")
}