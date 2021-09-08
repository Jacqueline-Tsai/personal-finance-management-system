
window.onload = function(){
    let viewButtons = document.getElementsByClassName("view-investment-entity-button")
    console.log(viewButtons)
    for (let viewButton of viewButtons){
        console.log(viewButton.id)
        viewButton.addEventListener("mouseover", event => {
            console.log(event);
        });
    }
}

function toggle(id, type) { 
    item = document.getElementById(id)
    if(type != undefined){
        item.style.display = type;
    }
    else if (item.style.display == "none") {
        item.style.display = "";
    } else {
        item.style.display = "none";
    }
}

function close(element){
    document.getElementById(id).style.display = "none";
}

window.onload = function() {
    let list = document.getElementsByClassName("green_pos_red_neg")
    for(let item of list){
        let value = parseInt(item.innerHTML)
        if(value > 0){
            item.innerHTML = "$ " + value.toString()
            item.style.color = "rgb(0, 205, 102)"
        }
        else{
            item.innerHTML = "$ " + (0-value).toString()
            item.style.color = "rgb(255, 80, 102)"
        }
    }
};
