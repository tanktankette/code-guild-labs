/**
 * Created by tanktankette on 6/27/17.
 */
String.prototype.capitalize = function() {
    return this.replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase(); });
};

back = {"Clear": "url(clear.jpeg)",
        "Clouds" : "url(cloudy.jpeg)",
        "Snow" : "url(snow.jpeg)",
        "Rain" : "url(rain.jpeg)"};

icons = {"Clear": "http://openweathermap.org/img/w/01d.png",
        "Clouds": "http://openweathermap.org/img/w/03d.png",
        "Snow": "http://openweathermap.org/img/w/13d.png",
        "Rain": "http://openweathermap.org/img/w/10d.png"};

$("#button").click(function(e){
    e.preventDefault();

    var pkg = {APPID: "9c862df5681526994f6c14a975122599"};
    var location = $("#location").val();
    if(isNaN(location)){
        pkg.q = location;
    } else {
        pkg.zip = location;
    }

    $.ajax({
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: pkg,
        dataType: "jsonp",
        success: function(data){
            tempc = data.main.temp - 272.15;
            tempf = tempc * 9 / 5 + 32;
            var w = data.weather[0].main;
            var ico = $("<img src =" + icons[w] + ">");
            $("#temp").text("Temp (C/F): " + tempc.toFixed(1) + "°/" + tempf.toFixed(0) + "°");
            $("#city").text("City: " + data.name);
            $("#condition").html("Condition: " + data.weather[0].description.capitalize() + ico[0].outerHTML);
            console.log(ico[0].outerHTML);
            $("#weatherwrapper").css("background", back[w]);
        }
    })


});