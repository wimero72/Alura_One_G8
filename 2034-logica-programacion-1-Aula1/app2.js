//Variables
let maximoRangoNsecreto=0;
let maximoIntentos=0;
let numeroUsuario=0;
let intentos=1;
let numeroSecreto=0;
console.log(numeroSecreto);
maximoRangoNsecreto = parseInt(prompt('Bienvenido al juego del número secreto, por favor introduce el maximo del rango:'));
console.log(maximoRangoNsecreto);
maximoIntentos = parseInt(prompt('Por favor Introduce el maximo de intentos:'));
console.log(maximoIntentos);
numeroSecreto=(Math.floor(Math.random()*maximoRangoNsecreto)+1);
console.log(numeroSecreto);
while (numeroUsuario != numeroSecreto) {
    numeroUsuario = parseInt(prompt(`Elige un número entre 1 y ${maximoRangoNsecreto}`));
    console.log(numeroUsuario  == numeroSecreto);
    if (numeroUsuario  == numeroSecreto) {
        alert(`Acertaste, el número secreto es : ${numeroSecreto}. Lo has logrado en ${intentos} ${intentos > 1 ? 'Intentos' : 'Intento' }`);
    } else {
        if (intentos==maximoIntentos){
            alert('Agotaste el numero maximo de intentos, El número secreto era ' + numeroSecreto);
            break;
        } else {
            if (numeroSecreto > numeroUsuario){
                alert('El número secreto es mayor');
            } else {
                alert('El numero secreto es menor');
            }    
            intentos++;
        }
    }

}
