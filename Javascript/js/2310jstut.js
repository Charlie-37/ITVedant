var x = [20, 50, 55, 77, 62, 45, 47, 85, 62, 99];
//console.log(x);

//console.log(x[6]);

var y = new Array();
y[0]= 58;
y[6]= 78;
y[3]= 36;
y[10]= 98;
//console.log(y);

var z = [2, 45, 66, 49, 36];
//console.log(z);
z[2]= 11;
//console.log(z);


let k = new Array();
k[0] = [10, 11, 12, 13, 14, 15, 16];
k[1] = ["Sunil", "Prasad", "Sahil", "Sujay", "Tushar"];
k[2] = ["Mumbai","Gujrat", "Patna", "Banglore", "Chennai", "Delhi"]

//console.log(k)

let l = [[10, 11, 12, 13, 14, 15, 16],
        ["Sunil", "Prasad", "Sahil", "Sujay", "Tushar"],
        ["Mumbai", "Gujrat", "Patna", "Banglore", "Chennai", "Delhi"] ]

//console.log(l)

for(let i = 0; i< l.length; i++){
    //console.log(l[i]);
    for(j = 0; j< l[i].length; j++){
       //console.log(l[i][j])
    }
}

document.write("<table border=1 cellspacing=2 width=400px>");
for(let i = 1; i<11; i++){
    //document.write("<tr>")
    for(j = 1; j<11; j++){
        document.write("<td>" + (i * j) + "</td>");
    }
    document.write("</tr>");
}
document.write("</table>")

for(i = 1; i<11; i++){
    for(j = 1; j<11; j++){
       // console.log(i*j);
    }
}

let m = [12, 25, 62, 5, 56, 98, 45, 77, 55];
//console.log(m.slice(3, 7));

//console.log(m.indexOf(98));
m.push(120);
m.unshift(11)

//console.log(m)

m.pop()
//console.log(m);


m.splice(1,3)
//console.log(m)
//console.log(m.slice(0,1))

var s = {
    name : "Sunil",
    address : "Badlapur",
    subject : ["Maths", "Science", "History"]
}

//console.log(s["name"]);

for(let i in s){
    console.log(i + ": "+ s[i])
}

function add(a,b){
    let z = a + b;
    console.log( z)
}
add(2,4);

function addition(a,b){
    return a+b;
}
y = addition(20, 30)

console.log(y)







function data(name, sname="Bhave"){
    document.write(name + " " + sname);
}
data("sunil")
data( " sunil", "Jadhav")

 r = {
    name : "Sunil",
    sname : "Bhave",
    address : "Badlapur",
    data : function(){
        a=20;
        b= 30;
        return a+b;
    }
}

console.log(r)

var z = 20;
console.log(z);

if(true){

    var z = 90;
    console.log(z);

}

console.log(z);

let b = 30;
console.log(b);

if(true){
    let b = 80;
    console.log(b)
}

 console.log(b)




 