function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

sleep(1000)
document.getElementById('form').value = "/icpco/citar?p=3&locale=es";
sleep(3000)
document.getElementById("btnAceptar").click();