$(function () {
  $("#tabs").tabs();
});



// creation of select Shape
let select_Shape = {
  "Rectangle / Parallelogram Area": "Arectangle",
  "Triangle Area": "Atraingle",
  "Trapezoid Area": "Atrapexoid",
  "Circle Area": "Acircle",
  "Sector Area": "Asector",
  "Ellipse Area": "Aellipse",
  "Square Area": "Asquare",
  "Ball Surface Area": "SAcircle",
  "Cone Surface Area": "SAcone",
  "Cube Surface Area": "SAcube",
  "Cylinder Surface Area": "SAcylinder",
  "Rectangle Surface Area": "SArectangle",
  "Capsule Surface Area": "SAcapsule",
  " Conical Frustum Surface Area": "SAconicfrustum",
  "Ellipsoid Surface Area": "SAellipsoid",
  "Square Pyramid Surface Area": "SAsqpyramid",
};

const dropShape = document.querySelectorAll("#SurfaceContainer select");

// let getButton = document.getElementById("get_Lenght");
for (let i = 0; i < dropShape.length; i++) {
  for (shape_Code in select_Shape) {
    x = select_Shape[shape_Code];
    //console.log(mass_Code);
    let selected;
    if (i == 0) {
      selected = shape_Code == "Rectangle Area" ? "selected" : "";
    }
    let optionSelect = `<option value="${x}" ${selected}>${shape_Code}</option>`;
    dropShape[i].insertAdjacentHTML("beforeend", optionSelect);
  }
}
//--------------------------//

// ------constructor for unit conversion
class unitConverter {
  constructor(unit, angle, value) {
    this.unit = unit;
    this.angle = angle;
    this.value = value;
  }
  convertUnit(unit, value) {
    switch (true) {
      case this.unit == "cm":
        return this.value;
        break;

      case this.unit == "m":
        return this.value * 100;
        break;

      case this.unit == "inch":
        return this.value * 2.54;
        break;

      case this.unit == "km":
        return this.value * 100000;
        break;

      case this.unit == "mm":
        return this.value / 10;
        break;

      case this.unit == "feet":
        return this.value * 30.48;
        break;

      case this.unit == "yard":
        return this.value * 91.4;
        break;

      case this.unit == "mile":
        return this.value * 160934;
        break;

      default:
        console.log("invalid");
        break;
    }
  }

  convertAngle(angle, value) {
    switch (true) {
      case this.angle == "deg":
        return this.value;
        break;

      case this.angle == "radian":
        return this.value * (180 / 3.14159265359);

        break;

      default:
        //console.log("invalid");
        break;
    }
  }
}
// ------constructor for result conversion
class resultConverter {
  constructor(convert, result) {
    this.convert = convert;
    this.result = result;
  }
  ConvertResult(convert, result) {
    switch (true) {
      case this.convert == "cm":
        return this.result;
        break;

      case this.convert == "m":
        return this.result / 10000;
        break;

      case this.convert == "inch":
        return this.result / 6.452;
        break;

      case this.convert == "km":
        return this.result / 1e10;
        break;

      case this.convert == "mm":
        return this.result / 100;
        break;

      case this.convert == "feet":
        return this.result / 929;
        break;

      case this.convert == "yard":
        return this.result / 8361;
        break;

      case this.convert == "mile":
        return this.result / 2.59e10;
        break;

      default:
        console.log("invalid");
        break;
    }
  }
}

// -----------switch Statements for Selectes Shapes-----

// let y = document.querySelector("#selectShape").value;
// console.log(y)
function selShape() {
  let select = document.getElementById("selectShape");
  let option = select.options[select.selectedIndex];

  //console.log(option.text);
  switch (true) {
    case option.value == "Arectangle":
      //console.log("sucess")
      $("#containerCalc").load("SAContainer.html #AreaRectangle");
      document.getElementById("SAImg").src = "../image/arearect.png";

      break;

    case option.value == "Atraingle":
      $("#containerCalc").load("SAContainer.html #AreaTriangle");
      document.getElementById("SAImg").src = "../image/areatriag.png";
      break;

    case option.value == "Atrapexoid":
      $("#containerCalc").load("SAContainer.html #AreaTrapozoid");
      document.getElementById("SAImg").src = "../image/area-trapezoid.png";
      break;

    case option.value == "Acircle":
      $("#containerCalc").load("SAContainer.html #AreaCircle");
      document.getElementById("SAImg").src = "../image/Acircle.png";
      break;

    case option.value == "Asector":
      $("#containerCalc").load("SAContainer.html #AreaSector");
      document.getElementById("SAImg").src = "../image/areaSector.jpg";
      break;

    case option.value == "Aellipse":
      $("#containerCalc").load("SAContainer.html #AreaEllipse");
      document.getElementById("SAImg").src = "../image/areaellpise.png";
      break;

    case option.value == "Asquare":
      $("#containerCalc").load("SAContainer.html #AreaSquare");
      document.getElementById("SAImg").src = "../image/areaSqua.jpg";
      break;

    case option.value == "SAcircle":
      $("#containerCalc").load("SAContainer.html #SurfaceAreaCircle");
      document.getElementById("SAImg").src = "../image/ballSA.jpg";
      break;

    case option.value == "SAcone":
      $("#containerCalc").load("SAContainer.html #SAreaCone");
      document.getElementById("SAImg").src = "../image/SACone.png";
      break;

    case option.value == "SAcube":
      $("#containerCalc").load("SAContainer.html #SAreaCube");
      document.getElementById("SAImg").src = "../image/cubesarea.png";
      break;

    case option.value == "SAcylinder":
      $("#containerCalc").load("SAContainer.html #SACylinder");
      document.getElementById("SAImg").src = "../image/SAcylinder.png";
      break;

    case option.value == "SArectangle":
      $("#containerCalc").load("SAContainer.html #SAreaRectangle");
      document.getElementById("SAImg").src = "../image/SArectangle.png";
      break;

    case option.value == "SAcapsule":
      $("#containerCalc").load("SAContainer.html #SAreaCapsule");
      document.getElementById("SAImg").src = "../image/SAcapsu.png";
      break;

    case option.value == "SAconicfrustum":
      $("#containerCalc").load("SAContainer.html #SAreaConicFrus");
      document.getElementById("SAImg").src = "../image/cone_frustum.png";
      break;

    case option.value == "SAellipsoid":
      $("#containerCalc").load("SAContainer.html #SAreaEllipse");
      document.getElementById("SAImg").src = "../image/Ellipsoid.png";
      break;

    case option.value == "SAsqpyramid":
      $("#containerCalc").load("SAContainer.html #SAreaSqPyramid");
      document.getElementById("SAImg").src = "../image/sqpyramid.png";
      break;
    default:
      alert("invalid");
      break;
  }
}

//---------------- shapes area calculator ---------//

// --------Area OF RECTANGLE
function getAreaRect() {
  let select_Arect_height = document.getElementById("Arect_height_Sel").value;
  let select_Arect_width = document.getElementById("Arect_width_Sel").value;

  // inputs value

  let ARectheight = document.getElementById("Arect_height").value;
  ARectheight = parseFloat(ARectheight);
  let ARectwidth = document.getElementById("Arect_width").value;
  SARectwidth = parseFloat(ARectwidth);
  //console.log(SRectheight);

  let height = new unitConverter(select_Arect_height, "", ARectheight);
  let height_value = height.convertUnit();
  let width = new unitConverter(select_Arect_width, "", ARectwidth);
  let width_value = width.convertUnit();

  let result = height_value * width_value;
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Arect_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_ARectangle")
    .addEventListener("click", ConvertAreaRect);

  function ConvertAreaRect() {
    //console.log("clicked")
    let Convert_to = document.getElementById("Arect_convert").value;
    let fromConvert = document.getElementById("Calc_Arect_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Arect_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Area OF Triangle--------
function getAreaTraig() {
  //console.log("clicked")
  //---select tag
  let select_triag_base = document.getElementById("Atriag_base_Sel").value;
  let select_triag_height = document.getElementById("Atriag_height_Sel").value;
  // ----input values
  let input_base = document.getElementById("Atriag_base").value;
  input_base = parseFloat(input_base);
  let input_height = document.getElementById("Atriag_height").value;
  input_height = parseFloat(input_height);
  //console.log(SRectheight);

  let base = new unitConverter(select_triag_base, "", input_base);
  let base_value = base.convertUnit();
  let height = new unitConverter(select_triag_height, "", input_height);
  let height_value = height.convertUnit();

  let result = (1 / 2) * height_value * base_value;
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Atriag_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_Atriag")
    .addEventListener("click", ConvertAreaRect);

  function ConvertAreaRect() {
    //console.log("clicked")
    let Convert_to = document.getElementById("Atriag_convert").value;
    let fromConvert = document.getElementById("Calc_Atriag_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Atriag_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Area OF Trapezoid--------
function getAreaTrapozeid() {
  //console.log("clicked")
  //---select tag
  let select_trape_base1 = document.getElementById("Atrapo_base1_Sel").value;
  let select_trape_base2 = document.getElementById("Atrapo_base2_Sel").value;
  let select_trape_height = document.getElementById("Atrapo_height_Sel").value;
  // ----input values
  let input_base1 = document.getElementById("Atrapo_base1").value;
  input_base1 = parseFloat(input_base1);
  let input_base2 = document.getElementById("Atrapo_base2").value;
  input_base2 = parseFloat(input_base2);
  let input_height = document.getElementById("Atrapo_height").value;
  input_height = parseFloat(input_height);
  //console.log(SRectheight);

  let base1 = new unitConverter(select_trape_base1, "", input_base1);
  let base1_value = base1.convertUnit();
  let base2 = new unitConverter(select_trape_base2, "", input_base2);
  let base2_value = base2.convertUnit();
  let height = new unitConverter(select_trape_height, "", input_height);
  let height_value = height.convertUnit();

  let result = (1 / 2) * (base1_value + base2_value) * height_value;
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Atrapo_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_Atrapo")
    .addEventListener("click", ConvertAreaTrapezoid);

  function ConvertAreaTrapezoid() {
    //console.log("clicked")
    let Convert_to = document.getElementById("Atrapo_convert").value;
    let fromConvert = document.getElementById("Calc_Atrapo_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Atrapo_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Area OF Circle--------
function getAreaCircle() {
  //console.log("clicked")
  //---select tag
  let select_circ_rad = document.getElementById("Acirc_radius_Sel").value;

  // ----input values
  let input_radius = document.getElementById("Acirc_radius").value;
  input_radius = parseFloat(input_radius);

  // console.log(input_radius);

  let radius = new unitConverter(select_circ_rad, input_radius);
  let radius_value = radius.convertUnit();
  let pi = 3.14159265359;
  pi = parseFloat(pi);
  //console.log(pi)
  let result = pi * (radius_value * radius_value);
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Acirc_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_Acircule")
    .addEventListener("click", ConvertAreacirc);

  function ConvertAreacirc() {
    console.log("clicked");
    let Convert_to = document.getElementById("Acircule_convert").value;
    let fromConvert = document.getElementById("Calc_Acirc_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, "", result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Acircule_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Area OF Sector--------
function getAreaSect() {
  //console.log("clicked")
  //---select tag
  let select_sect_radi = document.getElementById("Asect_radi_Sel").value;
  let select_sect_angle = document.getElementById("Atsect_angle_Sel").value;
  //console.log(select_sect_angle);
  // ----input values
  let input_radi = document.getElementById("Asect_radi").value;
  input_radi = parseInt(input_radi);
  let input_angle = document.getElementById("Asect_angle").value;
  input_angle = parseFloat(input_angle);
  let pi = 3.14159265359;
  pi = parseFloat(pi);
  //console.log(SRectheight);

  let radius = new unitConverter(select_sect_radi, "", input_radi);
  let radius_value = radius.convertUnit();
  let angle = new unitConverter("", select_sect_angle, input_angle);
  let angle_value = angle.convertAngle();

  let result = (angle_value / 360) * pi * (radius_value * radius_value);
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Asect_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_Asect")
    .addEventListener("click", ConvertAreaSect);

  function ConvertAreaSect() {
    //console.log("clicked")
    let Convert_to = document.getElementById("Asect_convert").value;
    let fromConvert = document.getElementById("Calc_Asect_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Asect_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Area OF Ellipse--------
function getAreaEllip() {
  //console.log("clicked")
  //---select tag
  let select_ellip_maj = document.getElementById("Aelli_smaj_Sel").value;
  let select_ellip_min = document.getElementById("Aelle_smin_Sel").value;
  // ----input values
  let input_maj = document.getElementById("Aelli_smaj").value;
  input_maj = parseFloat(input_maj);
  let input_min = document.getElementById("Aelli_smin").value;
  input_min = parseFloat(input_min);
  //console.log(SRectheight);

  let major = new unitConverter(select_ellip_maj, "", input_maj);
  let major_value = major.convertUnit();
  let miner = new unitConverter(select_ellip_min, "", input_min);
  let miner_value = miner.convertUnit();
  let pi = 3.14159265359;
  pi = parseFloat(pi);
  let result = pi * major_value * miner_value;
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Aellipse_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_Aellip")
    .addEventListener("click", ConvertAreaEllipse);

  function ConvertAreaEllipse() {
    //console.log("clicked")
    let Convert_to = document.getElementById("Aellip_convert").value;
    let fromConvert = document.getElementById("Calc_Aellipse_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Aellipg_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Area OF Square
function getAreaSqua() {
  let select_Asqua_edge = document.getElementById("Asqua_edge_Sel").value;

  let Asquaedge = document.getElementById("Asqua_side").value;
  Asquaedge = parseFloat(Asquaedge);

  //console.log(SRectheight);

  let side = new unitConverter(select_Asqua_edge, "", Asquaedge);
  let side_value = side.convertUnit();

  let result = side_value * side_value;
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_Squa_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_ASquare")
    .addEventListener("click", ConvertAreaSqua);

  function ConvertAreaSqua() {
    //console.log("clicked")
    let Convert_to = document.getElementById("ASqua_convert").value;
    let fromConvert = document.getElementById("Calc_Squa_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_Asqua_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}
// --------Surface Area OF Circle--------
function getSAreaCircle() {
  //---select tag
  let select_circ_rad = document.getElementById("SAcirc_radius_Sel").value;
  //console.log(select_circ_rad)

  // ----input values
  let input_SACirc_radius = document.getElementById("SAcircle_radius").value;
  input__SACirc_radius = parseFloat(input_SACirc_radius);

  //console.log(input_SACirc_radius);

  let radius = new unitConverter(select_circ_rad, "", input__SACirc_radius);
  let radius_value = radius.convertUnit();
  let pi = 3.14159265359;
  pi = parseFloat(pi);
  //console.log(pi)
  let result = 4 * pi * (radius_value * radius_value);
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_SAcirc_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SAcircule")
    .addEventListener("click", ConvertSAreacirc);

  function ConvertSAreacirc() {
    //console.log("clicked");
    let Convert_to = document.getElementById("SAcircule_convert").value;
    let fromConvert = document.getElementById("Calc_SAcirc_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAcircule_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}
// --------SurfaceArea OF Cone--------
function getSAreaCone() {
  //console.log("clicked")
  //---select tag
  let select_SAcone_baseRadi = document.getElementById(
    "SAcone_baseradi_Sel"
  ).value;
  let select_SAcone_height = document.getElementById("SAcone_height_Sel").value;
  // ----input values
  let input_baseradi = document.getElementById("SAcone_baseradi").value;
  input_baseradi = parseFloat(input_baseradi);
  let input_SAcone_height = document.getElementById("SAcone_height").value;
  input_SAcone_height = parseFloat(input_SAcone_height);

  let SAconebaseradi = new unitConverter(
    select_SAcone_baseRadi,
    "",
    input_baseradi
  );
  let SAconebaseradi_value = SAconebaseradi.convertUnit();
  let SAConeheight = new unitConverter(
    select_SAcone_height,
    "",
    input_SAcone_height
  );
  //console.log(input_SAcone_height);
  let SAConeheight_value = SAConeheight.convertUnit();

  let pi = 3.14159265359;
  pi = parseFloat(pi);
  let result =
    pi *
    SAconebaseradi_value *
    (SAconebaseradi_value +
      Math.sqrt(
        SAConeheight_value * SAConeheight_value +
          SAconebaseradi_value * SAconebaseradi_value
      ));
  result = result.toFixed(5);
  //console.log(result);
  document.getElementById("Calc_SAcone_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SAcone")
    .addEventListener("click", ConvertSAreaCone);

  function ConvertSAreaCone() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SAcone_convert").value;
    let fromConvert = document.getElementById("Calc_SAcone_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAcone_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}
// --------SurfaceArea OF Square
function getSAreaSqua() {
  let select_SAsqua_edge = document.getElementById("SAsqua_edge_Sel").value;

  let SAsquaedge = document.getElementById("SAsqua_side").value;
  SAsquaedge = parseFloat(SAsquaedge);

  let side = new unitConverter(select_SAsqua_edge, "", SAsquaedge);
  let side_value = side.convertUnit();
  //console.log(side_value);

  let result = 6 * (side_value * side_value);
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_SASqua_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SASquare")
    .addEventListener("click", ConvertAreaSqua);

  function ConvertAreaSqua() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SASqua_convert").value;
    let fromConvert = document.getElementById("Calc_SASqua_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAsqua_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}
// --------SurfaceArea OF Cylinder--------
function getSAreaCylinder() {
  //console.log("clicked")
  //---select tag
  let select_SAcylin_baseRadi = document.getElementById(
    "SAcylin_baseradi_Sel"
  ).value;
  let select_SAcylin_height =
    document.getElementById("SAcylin_height_Sel").value;
  // ----input values
  let input_baseradi = document.getElementById("SAcylin_baseradi").value;
  input_baseradi = parseFloat(input_baseradi);
  let input_SAcylin_height = document.getElementById("SAcylin_height").value;
  input_SAcylin_height = parseFloat(input_SAcylin_height);

  let SAcylinbaseradi = new unitConverter(
    select_SAcylin_baseRadi,
    "",
    input_baseradi
  );
  let SAcylinbaseradi_value = SAcylinbaseradi.convertUnit();
  let SACylinheight = new unitConverter(
    select_SAcylin_height,
    "",
    input_SAcylin_height
  );
  //console.log(input_SAcone_height);
  let SACylinheight_value = SACylinheight.convertUnit();

  let pi = 3.14159265359;
  pi = parseFloat(pi);
  let result =
    2 * pi * SAcylinbaseradi_value * SACylinheight_value +
    2 * pi * (SAcylinbaseradi_value * SAcylinbaseradi_value);
  result = result.toFixed(5);
  //console.log(result);
  document.getElementById("Calc_SAcylin_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SAcylin")
    .addEventListener("click", ConvertSAreaCylin);

  function ConvertSAreaCylin() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SAcylin_convert").value;
    let fromConvert = document.getElementById("Calc_SAcylin_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAcylin_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
  //---Surface Area of rectangle----
}
function getSAreaRect() {
  let select_SArect_length = document.getElementById("SArect_length_Sel").value;
  let select_SArect_height = document.getElementById("SArect_height_Sel").value;
  let select_SArect_width = document.getElementById("SArect_width_Sel").value;

  // inputs value
  let SARectlength = document.getElementById("SArect_length").value;
  SARectlength = parseFloat(SARectlength);
  let SARectheight = document.getElementById("SArect_height").value;
  SARectheight = parseFloat(SARectheight);
  let SARectwidth = document.getElementById("SArect_width").value;
  SARectwidth = parseFloat(SARectwidth);
  //console.log(SRectheight);
  let SArectlenght = new unitConverter(select_SArect_length, "", SARectlength);
  let length_value = SArectlenght.convertUnit();
  let height = new unitConverter(select_SArect_height, "", SARectheight);
  let height_value = height.convertUnit();
  let width = new unitConverter(select_SArect_width, "", SARectwidth);
  let width_value = width.convertUnit();

  let result =
    2 *
    (length_value * width_value +
      height_value * length_value +
      height_value * width_value);
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_SArect_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SARectangle")
    .addEventListener("click", ConvertSAreaRect);

  function ConvertSAreaRect() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SArect_convert").value;
    let fromConvert = document.getElementById("Calc_SArect_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SArect_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------SurfaceArea OF Capsule--------
function getSAreaCapsule() {
  //console.log("clicked")
  //---select tag
  let select_SAcapsu_baseRadi = document.getElementById(
    "SAcapsu_baseradi_Sel"
  ).value;
  let select_SAcapsu_height =
    document.getElementById("SAcapsu_height_Sel").value;
  // ----input values
  let input_baseradi = document.getElementById("SAcapsu_baseradi").value;
  input_baseradi = parseFloat(input_baseradi);
  let input_SAcapsu_height = document.getElementById("SAcapsu_height").value;
  input_SAcapsu_height = parseFloat(input_SAcapsu_height);

  let SAcapsubaseradi = new unitConverter(
    select_SAcapsu_baseRadi,
    "",
    input_baseradi
  );
  let SAcapsubaseradi_value = SAcapsubaseradi.convertUnit();
  let SACapsuheight = new unitConverter(
    select_SAcapsu_height,
    "",
    input_SAcapsu_height
  );
  //console.log(input_SAcone_height);
  let SACapsuheight_value = SACapsuheight.convertUnit();

  let pi = 3.14159265359;
  pi = parseFloat(pi);
  let result =
    2 *
    pi *
    SAcapsubaseradi_value *
    (2 * SAcapsubaseradi_value + SACapsuheight_value);
  result = result.toFixed(5);
  //console.log(result);
  document.getElementById("Calc_SAcapsu_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SAcapsu")
    .addEventListener("click", ConvertSAreaCapsu);

  function ConvertSAreaCapsu() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SAcapsu_convert").value;
    let fromConvert = document.getElementById("Calc_SAcapsu_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAcapsu_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------SurfaceArea OF ConicFrustum--------
function getSAreaConicFrustum() {
  //console.log("clicked")
  //---select tag
  let select_SAconfrus_baseRadi = document.getElementById(
    "SAcapsu_baseradi_Sel"
  ).value;
  let select_SAconfrus_bottRadi = document.getElementById(
    "SAconfrus_bottradi_Sel"
  ).value;
  let select_SAconfrus_height = document.getElementById(
    "SAconfrus_height_Sel"
  ).value;
  // ----input values
  let input_baseradi = document.getElementById("SAconfrus_baseradi").value;
  input_baseradi = parseFloat(input_baseradi);
  let input_bottradi = document.getElementById("SAconfrus_bottradi").value;
  input_bottradi = parseFloat(input_bottradi);
  let input_SAconfrus_height =
    document.getElementById("SAconfrus_height").value;
  input_SAconfrus_height = parseFloat(input_SAconfrus_height);

  let SAconfrusbaseradi = new unitConverter(
    select_SAconfrus_baseRadi,
    "",
    input_baseradi
  );
  let SAconfrusbaseradi_value = SAconfrusbaseradi.convertUnit();
  let SAconfrusbottradi = new unitConverter(
    select_SAconfrus_bottRadi,
    "",
    input_bottradi
  );
  let SAconfrusbottradi_value = SAconfrusbottradi.convertUnit();
  let SAConfrusheight = new unitConverter(
    select_SAconfrus_height,
    "",
    input_SAconfrus_height
  );
  //console.log(input_SAcone_height);
  let SAConfrusheight_value = SAConfrusheight.convertUnit();

  let pi = 3.14159265359;
  pi = parseFloat(pi);
  // let L = Math.sqrt((SAConfrusheight_value*SAConfrusheight_value)+((SAconfrusbottradi_value-SAconfrusbaseradi_value)*(SAconfrusbottradi_value-SAconfrusbaseradi_value)));
  // let result = (pi * L*(SAconfrusbottradi_value+SAconfrusbaseradi_value ))+((SAconfrusbottradi_value*SAconfrusbottradi_value)+(SAconfrusbaseradi_value *SAconfrusbaseradi_value ));
  let LSA =
    pi *
    (SAconfrusbottradi_value + SAconfrusbaseradi_value) *
    Math.sqrt(
      Math.pow(SAconfrusbottradi_value - SAconfrusbaseradi_value, 2) +
        SAConfrusheight_value * SAConfrusheight_value
    );

  let BSA = pi * Math.pow(SAconfrusbottradi_value, 2);
  let TSA = pi * Math.pow(SAconfrusbaseradi_value, 2);
  let result = LSA + TSA + BSA;
  result = result.toFixed(5);
  //console.log(result);
  document.getElementById("Calc_SAconfrus_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SAconfrus")
    .addEventListener("click", ConvertSAreaConFrus);

  function ConvertSAreaConFrus() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SAconfrus_convert").value;
    let fromConvert = document.getElementById("Calc_SAconfrus_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAconfrus_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

// --------Surface Area OF Ellips0id--------
function getSAreaEllip() {
  //console.log("clicked")
  //---select tag
  let select_ellip_a1 = document.getElementById("SAelli_a1_Sel").value;
  let select_ellip_a2 = document.getElementById("SAelli_a2_Sel").value;
  let select_ellip_a3 = document.getElementById("SAelle_a3_Sel").value;
  // ----input values
  let input_a1 = document.getElementById("SAelli_a1").value;
  input_a1 = parseFloat(input_a1);
  let input_a2 = document.getElementById("SAelli_a2").value;
  input_a2 = parseFloat(input_a2);
  let input_a3 = document.getElementById("SAelli_a3").value;
  input_a3 = parseFloat(input_a3);
  //console.log(SRectheight);

  let a1 = new unitConverter(select_ellip_a1, "", input_a1);
  let a1_value = a1.convertUnit();
  let a2 = new unitConverter(select_ellip_a2, "", input_a2);
  let a2_value = a2.convertUnit();
  let a3 = new unitConverter(select_ellip_a3, "", input_a3);
  let a3_value = a3.convertUnit();
  let pi = 3.14159265359;
  pi = parseFloat(pi);
  let result =
    4 *
    pi *
    Math.pow(
      (Math.pow(a1_value * a2_value, 1.6) +
        Math.pow(a1_value * a3_value, 1.6) +
        Math.pow(a3_value * a2_value, 1.6)) /
        3,
      1 / 1.6
    );
  result = result.toFixed(5);
  //console.log(width_value);
  document.getElementById("Calc_SAellipse_Result").innerHTML =
    "= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document
    .getElementById("Conv_SAellip")
    .addEventListener("click", ConvertSAreaEllipse);

  function ConvertSAreaEllipse() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SAellip_convert").value;
    let fromConvert = document.getElementById("Calc_SAellipse_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAellipg_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}

//---Surface Area of Square Pyramid----

function getSASqpyramid() {
 
  let select_SAsqpy_height = document.getElementById("SAsqpy_height_Sel").value;
  let select_SAsqpy_edge = document.getElementById("SAsqpy_edge_Sel").value;

  // inputs value
  
  let SAsqpyheight = document.getElementById("SAsqpy_height").value;
  SAsqpyheight = parseFloat(SAsqpyheight);
  let SAsqpyedge = document.getElementById("SAsqpy_edge").value;
  SAsqpyedge = parseFloat(SAsqpyedge);
  
  let height = new unitConverter(select_SAsqpy_height, "", SAsqpyheight);
  let height_value = height.convertUnit();
  let edge = new unitConverter(select_SAsqpy_edge, "", SAsqpyedge);
  let edge_value = edge.convertUnit();

  let BSA = Math.pow(edge_value, 2)
  let LSA = 2 * edge_value * (Math.sqrt( Math.pow((edge_value/2 ),2) + Math.pow(height_value, 2))) ;
  result = BSA + LSA;
  result = result.toFixed(5);
  console.log(result);
  //console.log(width_value);
  document.getElementById("Calc_SAsqpy_Result").innerHTML ="= " + result + "cm<sup>2</sup>";
  // convert result in other unit
  document.getElementById("Conv_SAsqpyramid").addEventListener("click", ConvertSASqPy);

  function ConvertSASqPy() {
    //console.log("clicked")
    let Convert_to = document.getElementById("SAsqpy_convert").value;
    let fromConvert = document.getElementById("Calc_SAsqpy_Result").value;
    fromConvert = parseFloat(fromConvert);
    //console.log(Convert_to)

    let convertUnit = new resultConverter(Convert_to, result);
    let resultConv = convertUnit.ConvertResult();
    document.getElementById("Conv_SAsqpy_Result").innerHTML =
      "= " + resultConv.toFixed(5) + Convert_to + "<sup>2</sup>";
  }
}
selShape();
