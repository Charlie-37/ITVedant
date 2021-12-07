let v = document.getElementById("container1");
//document.write(v.innerHTML);

//console.log(v.innerHTML);

//console.log("--------------------------------")

//console.log(v.innerText);



document.getElementById("container2").innerHTML = v.innerHTML

var div1 = document.getElementsByTagName('div');

console.log(div1);
//console.log(div1[0].innerText)   
//console.log(div1[2].innerText)   
//console.log(div1[1].innerText)  

console.log("---------*******-------------")

for(let i = 0; i< div1.length; i++){
    //console.log(div1[i].innerText)
}


// ---------------Get Multiple Elements By Classes

let div2 = document.getElementsByClassName("abc");

for(let i = 0; i<div2.length; i++){

    //console.log(div2[i].innerText);
}

function submitForm(){
    
    let name = document.getElementById('fname');
    console.log(name)
    let number = document.getElementById('fnumber');
    document.getElementById("valueform").innerHTML = name.value + " " + number.value;
    return false

}

//-------*******image change function

function img1(){
    document.getElementById("imageCont").innerHTML = `<img src="../image/Uchiha-Clan.jpg" alt="">`
}
function img2() {
    document.getElementById("imageCont").innerHTML = ` <img src="../image/wallpapersden.com_akatsuki-naruto_2560x1440.jpg" alt="">`
}
function img3() {
    document.getElementById("imageCont").innerHTML = ` <img src="../image/wallpapersden.com_naruto-naruto-shippuden-sasuke-uchiha_3840x2160.jpg" alt="">`
}
function img4() {
    document.getElementById("imageCont").innerHTML = `<img src="../image/wp2551484.jpg" alt="">`
}