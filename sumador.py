from pyscript import document, window

primer_dato = float(window.prompt("primer dato:"))
segundo_dato = float(window.prompt("segundo dato:"))
resultado = primer_dato + segundo_dato

document.querySelector("#primer-dato").value = primer_dato
document.querySelector("#segundo-dato").value = segundo_dato
document.querySelector("#resultado").innerHTML = resultado