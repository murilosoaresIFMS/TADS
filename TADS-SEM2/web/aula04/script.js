let h2 = document.getElementById('h2')
let img = document.querySelector('img')
let article = document.querySelector('article')

function showMore() {
    article.classList.toggle('open')
}

img.addEventListener('click', showMore)
h2.addEventListener('click', showMore)