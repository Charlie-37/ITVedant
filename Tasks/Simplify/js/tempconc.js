// creating object for select tab
let convert_Temp = {
  Celsius: "C",
  Faherenheit: "F",
  Kelvin: "K",
};

const dropTemp = document.querySelectorAll("#tableTemp select");

fromTemp = document.querySelector("#fromTemp select");
toTemp = document.querySelector("#toTemp select");
// let get_Mass_Button = document.querySelector("#get_Mass");

// let conv_mass = document.getElementById("result_mass");

//console.log(input_mass)
// let getButton = document.getElementById("get_Lenght");

for (let i = 0; i < dropTemp.length; i++) {
  let x = "";
  for (let temp_Code in convert_Temp) {
    x = convert_Temp[temp_Code]; // to assign value in potion tag
    // to assign default selected value in droplist
    let selected;
    if (i == 0) {
      selected = temp_Code == " Celsius" ? "selected" : "";
    } else if (i == 1) {
      selected = temp_Code == "Faherenheit" ? "selected" : "";
    }
    // adding the object in the option tag with value and text
    let optionTemp = `<option value="${x}" ${selected}>${temp_Code}</option>`;
    dropTemp[i].insertAdjacentHTML("beforeend", optionTemp);
  }
}

// Creating Calculate button listner and adding the convert function
let tempConversion = document
  .getElementById("get_temp")
  .addEventListener("click", convertTemp);

function convertTemp() {
  let from_temp = document.getElementById("from_Temp").value;
  console.log(from_temp);
  let to_temp = document.getElementById("to_Temp").value;
  let input_temp = document.getElementById("temp_input").value;
  input_temp = parseInt(input_temp);
  let result_Temp = "";
  //console.log(input_Speed)

  switch (true) {
      // converting Celsius to ......
    case from_temp == "C" && to_temp == "F":
      // console.log("sucess");
      result_Temp = (input_temp * (9 / 5)) + 32;
      break;

    case from_temp == "C" && to_temp == "K":
      // console.log("sucess");
      result_Temp = input_temp + 273.15;
      break;

    case from_temp == "C" && to_temp == "C":
      // console.log("sucess");
      result_Temp = input_temp ;
      break;


       // converting Fahrenheit to ......
    case from_temp == "F" && to_temp == "F":
        result_Temp = input_temp ;
        break;
  
      case from_temp == "F" && to_temp == "K":
        result_Temp = (input_temp - 32) * (5/9) + 273.15 ;
        break;
  
      case from_temp == "F" && to_temp == "C":
        result_Temp = (input_temp - 32) * (5/9) ;
        break;

        
         // converting Kelvin to ......
    case from_temp == "K" && to_temp == "F":
        result_Temp = (input_temp - 273.15) * (9/5) + 32;
        break;
  
      case from_temp == "K" && to_temp == "K":
        result_Temp = input_temp;
        break;
  
      case from_temp == "K" && to_temp == "C":
        result_Temp = input_temp - 273.15;
        break;
  
    default:
      console.log("invalid");
      break;
  }

  let result_Temp_Num = result_Temp.toFixed(3);

  document.getElementById("result_temp").innerText =
    input_temp + " " + from_temp + " = " + result_Temp_Num + "  " + to_temp;
}
