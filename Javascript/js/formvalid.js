
function formSubmit(){
    console.log("clicked")

    let fname = document.getElementById("fname").value;
    if(fname == ''){
        document.getElementById("nameError").innerHTML= "* Name is Empty * ";
        return false
    }
    
    if( !isNaN(fname))
    {
        document.getElementById("nameError").innerHTML = "* Name has to be in a Character * ";
        return false
    }


    //----------- contact validate
    let fnumber = document.getElementById("fnumber").value;
    if (fnumber == '') {
        document.getElementById("contactError").innerHTML = "* Contact is Empty * ";
        
        return false
    }
    if (!isNaN(fname)) {
        document.getElementById("contactError").innerHTML = "* Name has to be in a Number * ";
        return false
    }

    return true
}