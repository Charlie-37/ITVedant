function seprtAmount(){
    let x = document.getElementById('amount').value;
    x = parseInt(x)
    // console.log(x)

    if( (x/10)%10 != 0){
        console.log("invalid");
        alert("Please Enter Amount Multiple of Hundreds or Thousand Only")
        location.reload();
    }
    else{

        let cashOfTowTh = Math.trunc(x / 2000);

        if( cashOfTowTh <= 0){
            document.getElementById("noteTwoTh").innerHTML = " ";
        }
        else{
            document.getElementById('noteTwoTh').innerHTML = " Cash of 2000 note : " + Math.trunc(cashOfTowTh);
        }


        let reOfTwoTh = x % 2000;
        //console.log(reOfTwoTh)

        let cashOfFivHun = Math.trunc(reOfTwoTh / 500);

        if (cashOfFivHun <= 0) {
            document.getElementById("noteFiveHun").innerHTML = " ";
        }
        else {
            document.getElementById('noteFiveHun').innerHTML = " Cash of 500 note : " + cashOfFivHun;
        }


        let reOfFivHun = reOfTwoTh % 500;
        console.log(reOfFivHun)
        let cashOfTwoHun = Math.trunc(reOfFivHun / 200);
        //console.log(cashOfTwoHun)
         if(cashOfTwoHun <= 0){
             document.getElementById("noteTwoHun").innerHTML = " ";
         }
         else{
             document.getElementById('noteTwoHun').innerHTML = " Cash of 200 note : " + cashOfTwoHun;
         }

         let reOfTwoHun = reOfFivHun % 200;
         let cashOfOneHun = Math.trunc(reOfTwoHun / 100);

        if (cashOfOneHun <= 0) {
            document.getElementById("noteOneHun").innerHTML = " ";
        }
        else {
            document.getElementById('noteOneHun').innerHTML = " Cash of 100 note : " + cashOfOneHun;
        }

        
    }

    
    
}

function resetAmount(){
location.reload();
}