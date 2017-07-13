document.getElementById("submit").addEventListener("click", function(e){
    e.preventDefault();
    const c = document.getElementById("color").value;
    document.body.style.backgroundColor = c;
});

function Color(red, green, blue) // Constructor
{
    this.r = red;
    this.g = green;
    this.b = blue;

    this.blend = function(c){
        let red = this.r + c.r;
        let green = this.g + c.g;
        let blue = this.b + c.b;

        if (red > 255){red = 255}
        if (green > 255){green = 255}
        if (blue > 255){blue = 255}

        return new Color(red, green, blue);
    };

    this.toHex = function() {
        const red = Number(this.r).toString(16);
        const green = Number(this.g).toString(16);
        const blue = Number(this.b).toString(16);
        return red+green+blue;
    };
}
const clr1 = new Color(25, 55, 255);
const clr2 = new Color(10, 25, 3);
const clr3 = clr1.blend(clr2);

console.log(clr3.toHex());