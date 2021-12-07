

$("h1").css("color", "red")
$("#h1").css({ "color": "lime", "background-color": "green" })
$("#h1").click(function () {
    $("#h1").css({ "color": "aqua", "background-color": "blue" })
})
$("#h2").click(function () {
    $("#h2").css({ "color": "red", "background-color": "yellow" })
})

$(document).ready(function () {
    $("#h2").dblclick(function () {
        $("#h2").css({ "font-family": "san-serif", "color": "black", "background-color": "lightgrey" })
    })
})

/*--------------hide show---------------*/

$(document).ready(function(){
    $("#hide").click(function(){
        $("div").hide()
    });

    $("#show").click(function () {
        $("div").show()
    })
})