let arr = [];
var product_number;
var product_name = "pr_bs";
var product_fullname;

function alarma(x) {
    product_number = x;
    product_fullname = product_name + product_number;
    arr.push(product_fullname);
    alert(arr);
    alert(arr.length);
}

window.onload = function forbasket() {
    var x;
    arr.length
    for (let i = 0; i < arr.length; i++) {
        x = document.getElementById("fin");
        x.innerHTML = document.getElementsById(this.product_fullname);
    }
}


