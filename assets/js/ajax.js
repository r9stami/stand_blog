function like_post(slug,pk) {
    $.get(`/blog/like/${slug}/${pk}`).then(response =>{
        var element = document.getElementById('like')
        var count = document.getElementById('count')
        if(response['response'] === 'like'){
            element.className = 'fa fa-heart'
            count.innerText = Number(count.innerText) + 1
        }else{
            element.className = "fa fa-heart-o"
            count.innerText = Number(count.innerText ) - 1
        }
    })
}


