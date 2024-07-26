/*
// formas de declarar variavel
const a = 1; // constante
let b = 2;  // variável
var c = 3; // legado
d = 10;

// condicional
if (a > 2) {
    // caso verdade
} else {
    // caso falso
}

// apresentacao dos resultados
console.log(a)
alert(a)
document.write(a)


// manipulacao de DOM

let c = document.getElementById('container');
let d = document.getElementsByClassName("menu");
let e = document.getElementsByTagName("input");
let f = document.querySelector('#container');

// estrutura de repetiçao

for (let i = 0; i < 10; i++) {
    console.log(i)
}

let j = 0;
while (j < 10) {
    console.log(j)
    j++;
}

let h = 0;
do {
    console.log(h);
    h++;
} while (h < 10);

function soma(a,b) {
    console.log(a+b)
}

soma(6,6);

let soma = new Function("b", "h", "return (a + b")

// objetos
*/

let pessoa = {
    nome: "João",
    idade: 20, 
    sexo: "M"
}

function dizerOi() {
    let nome = document.getElementById("nome").value;
    let error = document.getElementById('Error');
    if (nome.length != 0) {
        error.innerHTML = `Oi, ${nome}`
        error.classList.add('Sucess')
    }
    else {
        error.innerHTML = 'Insira um valor válido'
        error.classList.add("Error")
    }
}