// creating object for select tab
let convert_Mass = {
  Milligram: "mgram",
  Gram: "gram",
  Kilogram: "kgram",
  Tonne: "tone",
  Pound: "pound",
  Ounce: "ounce",
  Stone: "stone",
  USTon: "uston",
  ImperialTon: "impton",
};

const dropMass = document.querySelectorAll("#tableMass select");

fromMass = document.querySelector("fromMass select");
toMass = document.querySelector("toMass select");
// let get_Mass_Button = document.querySelector("#get_Mass");

// let conv_mass = document.getElementById("result_mass");

//console.log(input_mass)
// let getButton = document.getElementById("get_Lenght");
for (let i = 0; i < dropMass.length; i++) {
  for (mass_Code in convert_Mass) {
    //console.log(mass_Code);
    let selected;
    if (i == 0) {
      selected = mass_Code == "Gram" ? "selected" : "";
    } else if (i == 1) {
      selected = mass_Code == "Pound" ? "selected" : "";
    }
    let optionMass = `<option value="${mass_Code}" ${selected}>${mass_Code}</option>`;
    dropMass[i].insertAdjacentHTML("beforeend", optionMass);
  }
}

// Creating Calculate button listner and adding the convert function
let massConversion = document
  .getElementById("get_mass")
  .addEventListener("click", convertMass);






function convertMass() {
    let from_Mass = document.getElementById("from_mass").value;
     let to_Mass = document.getElementById("to_mass").value;
     let input_Mass = document.getElementById("mass_input").value;
  input_Mass = parseInt(input_Mass);
     let result_mass = "";
  //console.log(to_Mass)


  switch (true) {

    //----- converting Gram to.....
    case from_Mass == "Gram" && to_Mass == "Pound":
      result_mass = input_Mass / 454;
      break;

    case from_Mass == "Gram" && to_Mass == "Milligram":
      result_mass = input_Mass *1000;
      break;

    case from_Mass == "Gram" && to_Mass == "Gram":
      result_mass = input_Mass ;
      break;

    case from_Mass == "Gram" && to_Mass == "Kilogram":
      result_mass = input_Mass / 1000;
      break;

    case from_Mass == "Gram" && to_Mass == "Tonne":
      result_mass = input_Mass / 1000000;
      break;

    case from_Mass == "Gram" && to_Mass == "Ounce":
      result_mass = input_Mass / 28.35;
      break;

    case from_Mass == "Gram" && to_Mass == "Stone":
      result_mass = input_Mass / 6350;
      break;

    case from_Mass == "Gram" && to_Mass == "USTon":
      result_mass = input_Mass / 907185;
      break;

    case from_Mass == "Gram" && to_Mass == "ImperialTon":
      result_mass = input_Mass / 1.016e+6;
      break;

    //----- converting Pound to.....
    case from_Mass == "Pound" && to_Mass == "Pound":
      result_mass = input_Mass;
      break;

    case from_Mass == "Pound" && to_Mass == "Milligram":
      result_mass = input_Mass * 453592;
      break;

    case from_Mass == "Pound" && to_Mass == "Gram":
      result_mass = input_Mass * 454 ;
      break;

    case from_Mass == "Pound" && to_Mass == "Kilogram":
      result_mass = input_Mass / 2.205;
      break;

    case from_Mass == "Pound" && to_Mass == "Tonne":
      result_mass = input_Mass / 2205;
      break;

    case from_Mass == "Pound" && to_Mass == "Ounce":
      result_mass = input_Mass * 16;
      break;

    case from_Mass == "Pound" && to_Mass == "Stone":
      result_mass = input_Mass / 14;
      break;

    case from_Mass == "Pound" && to_Mass == "USTon":
      result_mass = input_Mass / 2000;
      break;

    case from_Mass == "Pound" && to_Mass == "ImperialTon":
      result_mass = input_Mass / 2240;
      break;

    //----- converting Kilogram to.....
    case from_Mass == "Kilogram" && to_Mass == "Pound":
      result_mass = input_Mass * 2.205;
      break;

    case from_Mass == "Kilogram" && to_Mass == "Milligram":
      result_mass = input_Mass * 1e+6;
      break;

    case from_Mass == "Kilogram" && to_Mass == "Gram":
      result_mass = input_Mass * 1000 ;
      break;

    case from_Mass == "Kilogram" && to_Mass == "Kilogram":
      result_mass = input_Mass;
      break;

    case from_Mass == "Kilogram" && to_Mass == "Tonne":
      result_mass = input_Mass / 1000;
      break;

    case from_Mass == "Kilogram" && to_Mass == "Ounce":
      result_mass = input_Mass * 35.274;
      break;

    case from_Mass == "Kilogram" && to_Mass == "Stone":
      result_mass = input_Mass / 6.35;
      break;

    case from_Mass == "Kilogram" && to_Mass == "USTon":
      result_mass = input_Mass / 2000;
      break;

    case from_Mass == "Kilogram" && to_Mass == "ImperialTon":
      result_mass = input_Mass / 1016;
      break;

    //----- converting Milligram to.....
    case from_Mass == "Milligram" && to_Mass == "Pound":
      result_mass = input_Mass / 453592;
      break;

    case from_Mass == "Milligram" && to_Mass == "Milligram":
      result_mass = input_Mass;
      break;

    case from_Mass == "Milligram" && to_Mass == "Gram":
      result_mass = input_Mass * 1000 ;
      break;

    case from_Mass == "Milligram" && to_Mass == "Kilogram":
      result_mass = input_Mass * 1e+6;
      break;

    case from_Mass == "Milligram" && to_Mass == "Tonne":
      result_mass = input_Mass / 1e+9;
      break;

    case from_Mass == "Milligram" && to_Mass == "Ounce":
      result_mass = input_Mass / 28350;
      break;

    case from_Mass == "Milligram" && to_Mass == "Stone":
      result_mass = input_Mass / 6.35e+6;
      break;

    case from_Mass == "Milligram" && to_Mass == "USTon":
      result_mass = input_Mass / 9.072e+8;
      break;

    case from_Mass == "Milligram" && to_Mass == "ImperialTon":
      result_mass = input_Mass / 1.016e+9;
      break;

    //----- converting Ounce to.....
    case from_Mass == "Ounce" && to_Mass == "Pound":
      result_mass = input_Mass / 16;
      break;

    case from_Mass == "Ounce" && to_Mass == "Milligram":
      result_mass = input_Mass * 28350;
      break;

    case from_Mass == "Ounce" && to_Mass == "Gram":
      result_mass = input_Mass * 28.35 ;
      break;

    case from_Mass == "Ounce" && to_Mass == "Kilogram":
      result_mass = input_Mass / 35.274;
      break;

    case from_Mass == "Ounce" && to_Mass == "Tonne":
      result_mass = input_Mass / 35274;
      break;

    case from_Mass == "Ounce" && to_Mass == "Ounce":
      result_mass = input_Mass;
      break;

    case from_Mass == "Ounce" && to_Mass == "Stone":
      result_mass = input_Mass / 224;
      break;

    case from_Mass == "Ounce" && to_Mass == "USTon":
      result_mass = input_Mass / 32000;
      break;

    case from_Mass == "Ounce" && to_Mass == "ImperialTon":
      result_mass = input_Mass / 35840;
      break;

     //----- converting Stone to.....
     case from_Mass == "Stone" && to_Mass == "Pound":
        result_mass = input_Mass * 14;
        break;
  
      case from_Mass == "Stone" && to_Mass == "Milligram":
        result_mass = input_Mass * 6.35e+6;
        break;
  
      case from_Mass == "Stone" && to_Mass == "Gram":
        result_mass = input_Mass * 6350;
        break;
  
      case from_Mass == "Stone" && to_Mass == "Kilogram":
        result_mass = input_Mass * 6.35;
        break;
  
      case from_Mass == "Stone" && to_Mass == "Tonne":
        result_mass = input_Mass / 157;
        break;
  
      case from_Mass == "Stone" && to_Mass == "Ounce":
        result_mass = input_Mass * 224;
        break;
  
      case from_Mass == "Stone" && to_Mass == "Stone":
        result_mass = input_Mass ;
        break;
  
      case from_Mass == "Stone" && to_Mass == "USTon":
        result_mass = input_Mass / 143;
        break;
  
      case from_Mass == "Stone" && to_Mass == "ImperialTon":
        result_mass = input_Mass / 160;
        break;
    
       //----- converting Tonne to.....
     case from_Mass == "Tonne" && to_Mass == "Pound":
        result_mass = input_Mass * 2205;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "Milligram":
        result_mass = input_Mass * 1e+9;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "Gram":
        result_mass = input_Mass * 1e+6;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "Kilogram":
        result_mass = input_Mass * 1000;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "Tonne":
        result_mass = input_Mass ;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "Ounce":
        result_mass = input_Mass * 35274;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "Stone":
        result_mass = input_Mass * 157;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "USTon":
        result_mass = input_Mass * 1.102;
        break;
  
      case from_Mass == "Tonne" && to_Mass == "ImperialTon":
        result_mass = input_Mass / 1.016;
        break;  

         //----- converting USTonne to.....
     case from_Mass == "USTon" && to_Mass == "Pound":
        result_mass = input_Mass * 2000;
        break;
  
      case from_Mass == "USTon" && to_Mass == "Milligram":
        result_mass = input_Mass * 9.072e+8;
        break;
  
      case from_Mass == "USTon" && to_Mass == "Gram":
        result_mass = input_Mass * 907185;
        break;
  
      case from_Mass == "USTon" && to_Mass == "Kilogram":
        result_mass = input_Mass * 907.185;
        break;
  
      case from_Mass == "USTon" && to_Mass == "Tonne":
        result_mass = input_Mass / 1.102;
        break;
  
      case from_Mass == "USTon" && to_Mass == "Ounce":
        result_mass = input_Mass * 32000;
        break;
  
      case from_Mass == "USTon" && to_Mass == "Stone":
        result_mass = input_Mass * 143;
        break;
  
      case from_Mass == "USTon" && to_Mass == "USTon":
        result_mass = input_Mass ;
        break;
  
      case from_Mass == "USTon" && to_Mass == "ImperialTon":
        result_mass = input_Mass / 1.12;
        break;

     //----- converting ImperialTon to.....
     case from_Mass == "ImperialTon" && to_Mass == "Pound":
        result_mass = input_Mass * 2240;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "Milligram":
        result_mass = input_Mass * 1.016e+9;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "Gram":
        result_mass = input_Mass * 1.016e+6;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "Kilogram":
        result_mass = input_Mass * 1016;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "Tonne":
        result_mass = input_Mass * 1.016;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "Ounce":
        result_mass = input_Mass * 35840;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "Stone":
        result_mass = input_Mass * 160;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "USTon":
        result_mass = input_Mass * 1.12 ;
        break;
  
      case from_Mass == "ImperialTon" && to_Mass == "ImperialTon":
        result_mass = input_Mass;
        break;


    default:
      console.log("invalid number");
      break;
  }

 // creating a function to get big long result in exponential form 
 // eg = 9.84 * (1/100000000) = 9.84e-8
  function expo(x, f){
      return Number.parseFloat(x).toExponential(f);
  }
  let result_Mass_Num = expo(result_mass, 5)

  document.getElementById("result_mass").innerText =
    input_Mass + " " + from_Mass + " = " + result_Mass_Num + "  " + to_Mass;
}
