document.getElementById("submit").addEventListener("click", function(e){
    e.preventDefault();
    var c = document.getElementById("color").value;
    document.body.style.backgroundColor = c;
});

function Color(red, green, blue) // Constructor
{
    this.r = red;
    this.g = green;
    this.b = blue;

    this.blend = function(c){
        var red = this.r + c.r;
        var green = this.g + c.g;
        var blue = this.b + c.b;

        if (red > 255){red = 255}
        if (green > 255){green = 255}
        if (blue > 255){blue = 255}

        return new Color(red, green, blue);
    };

    this.toHex = function() {
        var red = Number(this.r).toString(16);
        var green = Number(this.g).toString(16);
        var blue = Number(this.b).toString(16);
        return red+green+blue;
    };
}
var clr1 = new Color(25,55,255);
var clr2 = new Color(10,25,3);
var clr3 = clr1.blend(clr2);

console.log(clr3.toHex());