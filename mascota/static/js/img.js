var pos=0;
var to_show = document.getElementById('carlo-base');
var imagenes = [
    './img/slays/Sprite-0001.png',
    './img/slays/Sprite-0002.png',
    './img/slays/Sprite-0003.png'
];

function dibujar(pos){
    to_show.src = imagenes[pos-1];
}

var to = setInterval(function(){
    pos++;
    dibujar(pos);
    if(pos == imagenes.length){
        clearInterval(to);
    }
},1000);