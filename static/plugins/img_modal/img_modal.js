
var img_to_modal = document.getElementsByClassName('img-to-modal')
for(img of img_to_modal){
    img.addEventListener("click",imgToModal)
}

function imgToModal(){
    var src = this.src
    var alt = this.alt
    var modal = document.createElement("DIV")
    modal.className = "img-modal"
    modal.innerHTML = '<span class="img-modal--close">&times;</span>\
        <img class="img-modal--img" src='+src+'>\
        <div class="img-modal--caption">'+alt+'</div>'
    document.body.appendChild(modal)
    document.getElementsByClassName("img-modal--close")[0].addEventListener("click", closeModal)
    document.body.style.overflow = "hidden"
}

function closeModal(){
    document.body.style.overflow = "auto"
    document.getElementsByClassName("img-modal")[0].remove()
}


