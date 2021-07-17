function toggle(id) {
    item = document.getElementById(id)
    if (item.style.display == "none") {
        item.style.display = "";
    } else {
        item.style.display = "none";
    }
}

function close(element){
    console.log(element)
    document.getElementById(id).style.display = "none";
}