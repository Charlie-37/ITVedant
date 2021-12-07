


class Emp{
    show(){
        console.log("developer");
    }
    }

var x = new Emp();
x.show();

//----Calculator using Class

class arthmatic{

    constructor(a,b){
        this.a = a
        this.b = b
    }

    add(a,b){
        return this.a+this.b;
    }
    sub(a, b) {
        return this.a - this.b;
    }
    mult(a, b) {
        return this.a * this.b;
    }
    div(a, b) {
        return this.a / this.b;
    }
    
}

let y = new arthmatic(2,3);
let z = y.add();
console.log(z);



class abc{
    constructor(x,y){
        console.log(x+y)
    }
}

x = new abc(5,5);


// employee constructor

class employee{
    constructor(name, accnum, contact, email){
        this.name = name
        this.accnum = accnum
        this.contact = contact
        this.email = email
    }
    display(){
        console.log(this.name + " " + this.accnum + " "+ this.contact + " " + this.email)
    }
}

let empdet1 = new employee("sunil", "SBI3264", "991750", "sunilb@37");
empdet1.display()


let empdet2 = new employee("prasad", "TJSB6566", "24356", "prasad@1234");
empdet2.display()