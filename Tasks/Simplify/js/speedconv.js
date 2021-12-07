// creating object for select tab
let convert_Speed = {
  "Miles per hour": "miles/hr",
  "Foot per second": "foot/sec",
  "Meter per second": "meter/sec",
  "Kilometer per hour": "km/hr",
  Knot: "knot",
};

const dropSpeed = document.querySelectorAll("#tableSpeed select");

fromSpeed = document.querySelector("#fromSpeed select");
toSpeed = document.querySelector("#toSpeed select");
// let get_Mass_Button = document.querySelector("#get_Mass");

// let conv_mass = document.getElementById("result_mass");

//console.log(input_mass)
// let getButton = document.getElementById("get_Lenght");

for (let i = 0; i < dropSpeed.length; i++) {
  let x = "";
  for (let speed_Code in convert_Speed) {
    x = convert_Speed[speed_Code];

    let selected;
    if (i == 0) {
      selected = speed_Code == "Kilometer per hour" ? "selected" : "";
    } else if (i == 1) {
      selected = speed_Code == "Meter per second" ? "selected" : "";
    }
    let optionSpeed = `<option value="${x}" ${selected}>${speed_Code}</option>`;
    dropSpeed[i].insertAdjacentHTML("beforeend", optionSpeed);
  }
}

// Creating Calculate button listner and adding the convert function
let speedConversion = document
  .getElementById("get_speed")
  .addEventListener("click", convertSpeed);

function convertSpeed() {
  let from_Speed = document.getElementById("from_speed").value;
  let to_Speed = document.getElementById("to_speed").value;
  let input_Speed = document.getElementById("speed_input").value;
  input_Speed = parseInt(input_Speed);
  let result_Speed = "";
  //console.log(input_Speed)

  switch (true) {
    //------ converting KM/Hr toooo
    case from_Speed == "km/hr" && to_Speed == "meter/sec":
      result_Speed = input_Speed / 3.6;
      //console.log(result_Speed)
      break;

    case from_Speed == "km/hr" && to_Speed == "foot/sec":
      result_Speed = input_Speed / 1.097;

    case from_Speed == "km/hr" && to_Speed == "miles/hr":
      result_Speed = input_Speed / 1.609;

      break;

    case from_Speed == "km/hr" && to_Speed == "knot":
      result_Speed = input_Speed / 1.852;
      break;

    case from_Speed == "km/hr" && to_Speed == "km/hr":
      result_Speed = input_Speed;
      break;

    //------ converting meter/sec toooo
    case from_Speed == "meter/sec" && to_Speed == "meter/sec":
      result_Speed = input_Speed;
      break;

    case from_Speed == "meter/sec" && to_Speed == "foot/sec":
      result_Speed = input_Speed * 3.281;
      break;

    case from_Speed == "meter/sec" && to_Speed == "miles/hr":
      result_Speed = input_Speed * 2.237;
      break;

    case from_Speed == "meter/sec" && to_Speed == "knot":
      result_Speed = input_Speed * 1.944;

    case from_Speed == "meter/sec" && to_Speed == "km/hr":
      result_Speed = input_Speed * 3.6;

    //------ converting miles/hr toooo
    case from_Speed == "miles/hr" && to_Speed == "meter/sec":
      result_Speed = input_Speed / 2.237;
      break;

    case from_Speed == "miles/hr" && to_Speed == "foot/sec":
      result_Speed = input_Speed * 1.467;
      break;

    case from_Speed == "miles/hr" && to_Speed == "miles/hr":
      result_Speed = input_Speed;

      break;

    case from_Speed == "miles/hr" && to_Speed == "knot":
      result_Speed = input_Speed / 1.151;
      break;

    case from_Speed == "miles/hr" && to_Speed == "km/hr":
      result_Speed = input_Speed * 1.609;
      break;

    //------ converting foot/sec toooo
    case from_Speed == "foot/sec" && to_Speed == "meter/sec":
      result_Speed = input_Speed / 3.281;
      break;

    case from_Speed == "foot/sec" && to_Speed == "foot/sec":
      result_Speed = input_Speed;

    case from_Speed == "foot/sec" && to_Speed == "miles/hr":
      result_Speed = input_Speed / 1.467;
      break;

    case from_Speed == "foot/sec" && to_Speed == "knot":
      result_Speed = input_Speed / 1.688;
      break;

    case from_Speed == "foot/sec" && to_Speed == "km/hr":
      result_Speed = input_Speed * 1.097;
      break;

    //------ converting knot toooo
    case from_Speed == "knot" && to_Speed == "meter/sec":
      result_Speed = input_Speed / 1.944;
      break;

    case from_Speed == "knot" && to_Speed == "foot/sec":
      result_Speed = input_Speed * 1.688;
      break;

    case from_Speed == "knot" && to_Speed == "miles/hr":
      result_Speed = input_Speed * 1.151;

      break;

    case from_Speed == "knot" && to_Speed == "knot":
      result_Speed = input_Speed;
      break;

    case from_Speed == "knot" && to_Speed == "km/hr":
      result_Speed = input_Speed * 1.852;
      break;

      default :
      console.log("invalid");
      break;
  }

  let result_Speed_Num = result_Speed.toFixed(5);

  document.getElementById("result_speed").innerText =
    input_Speed + " " + from_Speed + " = " + result_Speed_Num + "  " + to_Speed;
}
