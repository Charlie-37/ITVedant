// for Change Image according to tabs change
document.getElementById("imgLeng").addEventListener("click" ,  ()=>{
  //console.log("clicked")
  document.getElementById("imgB").src = "../image/length.png"
  
});
document.getElementById("imgMass").addEventListener("click" ,  ()=>{
  //console.log("clicked")
  document.getElementById("imgB").src = "../image/mass.png"
  
});
document.getElementById("imgSpeed").addEventListener("click" ,  ()=>{
  //console.log("clicked")
  document.getElementById("imgB").src = "../image/speed1.png"
  
});
document.getElementById("imgTemp").addEventListener("click" ,  ()=>{
  //console.log("clicked")
  document.getElementById("imgB").src = "../image/temp1.png"
  
});


// for Tabs Jquery UI
$(function () {
  $("#tabs").tabs();
});

// --------creation of Select tag for length-------
let convert_Len = {
  Kilometre: "kmeter",
  Meter: "meter",
  Centimeter: "cmeter",
  Mile: "mile",
  Yard: "yard",
  Foot: "foot",
  Inch: "inch",
  NauticalMile: "nmile",
};
const dropLength = document.querySelectorAll("#tableLen select");

fromLength = document.querySelector("fromLen select");
toLength = document.querySelector("toLen select");
let getButton = document.querySelector("#get_Lenght");
// let getButton = document.getElementById("get_Lenght");
for (let i = 0; i < dropLength.length; i++) {
  for (len_Code in convert_Len) {
    
    // console.log(len_Code);
    let selected;
    if (i == 0) {
      selected = len_Code == "Centimeter" ? "selected" : "";
    } else if (i == 1) {
      selected = len_Code == "Meter" ? "selected" : "";
    }
    let optionLen = `<option value="${len_Code}" ${selected}>${len_Code}</option>`;
    dropLength[i].insertAdjacentHTML("beforeend", optionLen);
  }
}
// getButton.addEventListener("click", e=> {
//     getLengthConvert()
//     e.preventDefault();
// })


function get_Length() {
 
  let getConvertOne = document.getElementById("element1").value;
  getConvertOne = parseInt(getConvertOne);

  let conv_One = document.getElementById("from_len").value;
  let conv_Two = document.getElementById("to_len").value;

  let con_result = "";
   
  
  switch (true) {
    // ------switch for Centimeter to ...
    case conv_One == "Centimeter" && conv_Two == "Centimeter":
      con_result = getConvertOne;
      break;

    case conv_One == "Centimeter" && conv_Two == "Meter":
      con_result = getConvertOne / 100;

      break;

    case conv_One == "Centimeter" && conv_Two == "Kilometre":
      con_result = getConvertOne / 100000;

      break;

    case conv_One == "Centimeter" && conv_Two == "Mile":
      con_result = getConvertOne / 160934;

      break;

    case conv_One == "Centimeter" && conv_Two == "Yard":
      con_result = getConvertOne / 91.4;

      break;

    case conv_One == "Centimeter" && conv_Two == "Foot":
      con_result = getConvertOne / 30.48;

      break;

    case conv_One == "Centimeter" && conv_Two == "Inch":
      con_result = getConvertOne / 2.54;

      break;

    case conv_One == "Centimeter" && conv_Two == "NauticalMile":
      con_result = getConvertOne / 185200;

      break;

    // ------switch for Meter to ...
    case conv_One == "Meter" && conv_Two == "Centimeter":
      con_result = getConvertOne * 100;

      break;

    case conv_One == "Meter" && conv_Two == "Meter":
      con_result = getConvertOne;

      break;

    case conv_One == "Meter" && conv_Two == "Kilometre":
      con_result = getConvertOne / 1000;

      break;

    case conv_One == "Meter" && conv_Two == "Mile":
      con_result = getConvertOne / 1609;

      break;

    case conv_One == "Meter" && conv_Two == "Yard":
      break;

    case conv_One == "Meter" && conv_Two == "Foot":
      con_result = getConvertOne * 3.281;

      break;

    case conv_One == "Meter" && conv_Two == "Inch":
      con_result = getConvertOne * 39.37;

      break;

    case conv_One == "Meter" && conv_Two == "NauticalMile":
      con_result = getConvertOne / 1852;

      break;

    // ------switch for Kilometer to ...
    case conv_One == "Kilometre" && conv_Two == "Centimeter":
      con_result = getConvertOne * 10000;

      break;

    case conv_One == "Kilometre" && conv_Two == "Meter":
      con_result = getConvertOne * 100;

      break;

    case conv_One == "Kilometre" && conv_Two == "Kilometre":
      con_result = getConvertOne;

      break;

    case conv_One == "Kilometre" && conv_Two == "Mile":
      con_result = getConvertOne / 1.609;

      break;

    case conv_One == "Kilometre" && conv_Two == "Yard":
      con_result = getConvertOne * 1094;

      break;

    case conv_One == "Kilometre" && conv_Two == "Foot":
      con_result = getConvertOne * 3281;

      break;

    case conv_One == "Kilometre" && conv_Two == "Inch":
      con_result = getConvertOne * 3937;

      break;

    case conv_One == "Kilometre" && conv_Two == "NauticalMile":
      con_result = getConvertOne / 1.852;

      break;
     // ------switch for Inch to ...
     case conv_One == "Inch" && conv_Two == "Centimeter":
      con_result = getConvertOne * 2.54;

      break;

    case conv_One == "Inch" && conv_Two == "Meter":
      con_result = getConvertOne * 39.37;

      break;

    case conv_One == "Inch" && conv_Two == "Kilometre":
      con_result = getConvertOne / 39370;

      break;

    case conv_One == "Inch" && conv_Two == "Mile":
      con_result = getConvertOne / 63360;

      break;

    case conv_One == "Inch" && conv_Two == "Yard":
      con_result = getConvertOne / 36;

      break;

    case conv_One == "Inch" && conv_Two == "Foot":
      con_result = getConvertOne /12;

      break;

    case conv_One == "Inch" && conv_Two == "Inch":
      con_result = getConvertOne ;

      break;

    case conv_One == "Inch" && conv_Two == "NauticalMile":
      con_result = getConvertOne / 72913;

      break;

      // ------switch for Foot to ...
     case conv_One == "Foot" && conv_Two == "Centimeter":
      con_result = getConvertOne * 30.48;

      break;

    case conv_One == "Foot" && conv_Two == "Meter":
      con_result = getConvertOne / 3.281;

      break;

    case conv_One == "Foot" && conv_Two == "Kilometre":
      con_result = getConvertOne / 3281;

      break;

    case conv_One == "Foot" && conv_Two == "Mile":
      con_result = getConvertOne / 5280;

      break;

    case conv_One == "Foot" && conv_Two == "Yard":
      con_result = getConvertOne / 3;

      break;

    case conv_One == "Foot" && conv_Two == "Foot":
      con_result = getConvertOne;

      break;

    case conv_One == "Foot" && conv_Two == "Inch":
      con_result = getConvertOne * 12;

      break;

    case conv_One == "Foot" && conv_Two == "NauticalMile":
      con_result = getConvertOne / 72913;

      break;

      // ------switch for Mile to ...
     case conv_One == "Mile" && conv_Two == "Centimeter":
      con_result = getConvertOne * 160934;

      break;

    case conv_One == "Mile" && conv_Two == "Meter":
      con_result = getConvertOne * 1609;

      break;

    case conv_One == "Mile" && conv_Two == "Kilometre":
      con_result = getConvertOne * 1.609;

      break;

    case conv_One == "Mile" && conv_Two == "Mile":
      con_result = getConvertOne;

      break;

    case conv_One == "Mile" && conv_Two == "Yard":
      con_result = getConvertOne *1760;

      break;

    case conv_One == "Mile" && conv_Two == "Foot":
      con_result = getConvertOne * 5280;

      break;

    case conv_One == "Mile" && conv_Two == "Inch":
      con_result = getConvertOne * 63360;

      break;

    case conv_One == "Mile" && conv_Two == "NauticalMile":
      con_result = getConvertOne / 1.151;

      break;

      // ------switch for Mile to ...
      case conv_One == "NauticalMile" && conv_Two == "Centimeter":
        con_result = getConvertOne * 185200;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "Meter":
        con_result = getConvertOne * 1852;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "Kilometre":
        con_result = getConvertOne * 1.852;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "Mile":
        con_result = getConvertOne * 1.151;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "Yard":
        con_result = getConvertOne * 2025;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "Foot":
        con_result = getConvertOne * 6076;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "Inch":
        con_result = getConvertOne * 72913;
  
        break;
  
      case conv_One == "NauticalMile" && conv_Two == "NauticalMile":
        con_result = getConvertOne;
  
        break;
    default:
      console.log("invalid");
      break;
  }
  let resultNum = con_result.toFixed(4);
  document.getElementById("result_length").innerText =
    getConvertOne + " " + conv_One + " = " + resultNum + "  " + conv_Two;
    
}



