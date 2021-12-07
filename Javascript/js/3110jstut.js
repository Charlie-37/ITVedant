class college{
  show(){
      console.log("hello")
  }
}
 /* extends is use to inherit the property of parent college
  i.e you can access the property of other class*/
class student extends college{ 
    display(){
        console.log("world")
    }

}

let a = new student();
a.display()
a.show()

console.log("--------class heirarchy-----")


class first{
    numone(){
        this.a = 20
        console.log("first called")
    }
}

class second extends first{
    numtwo(){
        this.b = 40
        console.log("second called")
        this.numone() // syntax to called a method in other method
    }

    result(){
        this.c = 90
        console.log("result called")
        console.log(this.a + this.b + this.c)
        this.numtwo()
    }
}
 var add = new second()
 add.numone()
 add.numtwo()
 add.result()

 // --- ****  Polymorphisim*****---////

 class one{
     show(){
         console.log("hello")
     }
 }

 class two extends one{
     show(){
         console.log("hii")
     }
 }

 let x = new two();
 x.show()



 class hello{
     show(){
         console.log("hello world")
     }
 }

 class world extends hello{
     show(){
         console.log("hii world")
         this.show() // this is a recursion as function calling itself
     }
 }

 let y = new world()

 // table without loop

 
 class table{

    mult( a, i = 1){
        console.log(a*i)
        i++

        if(i<11){
            this.mult(a , i)
        }
    }
 }
 
 let multtab = new table()

 multtab.mult(2)

 class A {
     static show(){
         console.log("hii")
     }
 }

 A.show();

 
//  var o = alert("hello");
//  console.log(o)
  

//  var p = prompt("enter yor name");
//  console.log(p)

const num = 12123;
const placeValue = (num, res = [], factor = 1) => {
   if(num){
      const val = (num % 10) * factor;
      res.unshift(val);
      return placeValue(Math.floor(num / 10), res, factor * 10);

   };
   return res;
};

