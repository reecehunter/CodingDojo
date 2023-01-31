function removeElement(e) {
    e.remove();
}

function loadReport() {
    alert("Loading weather report...");
}

function setTemperature(e) {
    const temps = document.getElementsByClassName("temp");
    if(e.value == "f") {
        for(var i = 0; i < temps.length; i++) {
            temps[i].textContent = Math.round((Number(temps[i].textContent) * 1.8) + 32);
        }
    } else {
        for(var i = 0; i < temps.length; i++) {
            temps[i].textContent = Math.round((Number(temps[i].textContent)- 32) / 1.8);
        }
    }
}