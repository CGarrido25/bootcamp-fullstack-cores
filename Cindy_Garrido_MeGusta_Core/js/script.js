let publication_score_one=0
let publication_score_two=0
let publication_score_three=0

let btn_like_one = document.getElementById("btn_like_one")
let btn_like_two = document.getElementById("btn_like_two")
let btn_like_three = document.getElementById("btn_like_three")

let span_like_one = document.getElementById("span_like_one")
let span_like_two = document.getElementById("span_like_two")
let span_like_three = document.getElementById("span_like_three")


btn_like_one.addEventListener('click',function(){
    publication_score_one++
    span_like_one.innerText= `${publication_score_one} likes(s)`
})

btn_like_two.addEventListener('click',function(){
    publication_score_two++
    span_like_two.innerText= `${publication_score_two} likes(s)`
})

btn_like_three.addEventListener('click',function(){
    publication_score_three++
    span_like_three.innerText= `${publication_score_three} likes(s)`
})





