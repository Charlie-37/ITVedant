
function calc(){
let num1 = document.getElementById("input_1").value
num1 = parseInt(num1)
let num2 = document.getElementById("input_2").value
num2 = parseInt(num2)
let select_1 = document.getElementById("select_1").value
let select_2 = document.getElementById("select_2").value
console.log(select_2)

// if(select_1 == "cm" && select_2 =="meter"){
//  console.log("sucess")
//     document.getElementById("result").innerHTML = num1/100;
// }
// else if(select_1 =="meter" && select_2 == "cm" ){
    
    //     document.getElementById("result").innerHTML = num1*100;
    // }
    
    switch(true){
        case (select_1 == "cm" && select_2 == "meter"):
            document.getElementById("result").innerHTML = num1/100 + " meter";
            break ;
            
            case (select_1 =="meter" && select_2 == "cm"):
               document.getElementById("result").innerHTML = num1*100 + " cm";
               break;

            default:
                console.log("invalid");
                break;

}
    
}

