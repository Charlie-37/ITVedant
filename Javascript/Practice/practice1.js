// js counter 
let data = 0;

let CounterDispley = document.querySelector(".counter");
function decCount(){
    if(data <= 1){
        data = 0;
    }
    else{
        data--;
    }
    updateDispay()
    
} 
function resCount(){
    data  = 0;
    updateDispay()
    
} 
function incCount(){
    data++;
    updateDispay()
    
} 

function updateDispay(){
    CounterDispley.innerHTML = data;
}