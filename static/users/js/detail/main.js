var edit = false
function toggleEdit(){ 
    /*
    makes inputs visible, editable and outlines them
    */
    const hidden_divs = document.getElementsByClassName("hidden-input")
    const readonly_inputs = document.querySelectorAll("#right-info input")
    const bio = document.getElementById("bio")

    for(var div of hidden_divs){
        div.classList.toggle("d-none")
    }

    for(var input of readonly_inputs){
        input.readOnly = edit
        input.classList.toggle("underline")
    }
    
    bio.readOnly = edit
    bio.classList.toggle("border-line")
    edit = !edit
}