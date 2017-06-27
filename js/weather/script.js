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
            $("#temp").text("Temp (C/F): " + tempc.toFixed(1) + "°/" + tempf.toFixed(0) + "°");
            $("#city").text("City: " + data.name);
            $("#condition").text("Condition: " + data.weather[0].description.capitalize());
            var w = data.weather[0].main;
            $("#weatherwrapper").css("background", back[w]);
        }
    })


});