var datos = [];
datos[0] = ["Calcetines Rotos", 16, "img/libro1.jpg"];
datos[1] = ["Patria", 15.9, "img/libro2.jpg"];
datos[2] = ["Los Ritos Del Agua", 21.8, "img/libro3.jpg"];
datos[3] = ["El Extraño Verano de Tom Harvey", 20, "img/libro4.jpg"];
datos[4] = ["La Habitación en Llamas", 21.5, "img/libro5.jpg"];
datos[5] = ["El secreto de Ile-de-sein", 16.5, "img/libro6.jpg"];
datos[6] = ["Ocho días de Marzo", 15.9, "img/libro7.jpg"];
datos[7] = ["Cinco dias de Octubre", 15.9, "img/libro8.jpg"];
var salida = "";
var compra = [];

function carrito() {
    for (i = 0; i < datos.length; i++) {
        if (i == 0) {
            salida += '<div class="row">';
        }
        else if ((i % 4) == 0) {
            salida += '</div> <div class="row">';
        };
        salida += '<div style="height:300px" class="col-md-3 producto"> <img style="width:20%" src=' + datos[i][2] + ' class="img-rounded"><h3 class="text-primary text-center">' + datos[i][0] + '</h3>' + datos[i][1] + ' € <br> <button onclick = "addCart(this,'+i+')"  onchange = "devolver(this,'+i+')" type="button" style="margin-top:15px" class= "btn btn-primary active btn-default">Comprar</button></div>';
        document.getElementById("hello").innerHTML = salida;
    };
    if (i != 0) {
        salida += "</div>";
    };
};

function addCart(boton, libro) {
    console.log(boton);
    compra.push([libro, 1]);
    boton.disabled = true;
//    if(borrarCart()){
//        boton.disabled=false;
//    };
    refreshCarrito();
};

function cantidad(posicion, incremento) {
    compra[posicion][1] += incremento;
    if (compra[posicion][1] < 1) {
        compra[posicion][1] = 1;
    };
    refreshCarrito();
};

function refreshCarrito() {
    tablaCompra();
};

function tablaCompra() {
    var imprimir = "";
    for (i = 0; i < compra.length; i++) {
        var x = compra[i][0];
        imprimir += "<tr><td>" + (i + 1) + "</td><td>" + datos[x][0] + "</td><td><button onclick = 'cantidad("+i+", -1 )'>-</button>" + compra[i][1] + "<button onclick = 'cantidad("+i+", 1 )'>+</button></td><td>" + datos[x][1] + " €</td><td><button onclick= 'borrarCart(" + i + ")' >Eliminar</button></td></tr>"
    };
    document.getElementById("tabla-compra").innerHTML = imprimir;
};

function borrarCart(k) {
    compra.splice(k, 1);
//    if(boton.disabled=true){
//        boton.disabled=false;
//    }
    refreshCarrito();
}
carrito();


function devolver(boton,libros){
    console.log(boton);
    if(compra.length=datos[libros]){
    boton.disabled =false;
}
};
