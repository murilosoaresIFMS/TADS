const container = document.getElementById('container')

const url = "https://jsonplaceholder.typicode.com/posts"

async function getPost() {
    const resp = await fetch(url)
    const data = await resp.json()
    data.map((post) => {
        console.log(post.title)
    })
    console.log(data)
}

getPost()

