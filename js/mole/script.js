/**
 * Created by tanktankette on 6/29/17.
 */
let score = 0;
let t;
let delay = 4100;
let timeout = [];
let len = 16;
let strikes = 0;

function pad(num, size) {
    let s = num+"";
    while (s.length < size) s = "0" + s;
    return s;
}

for(let i = 1; i<=len; i++) {
    let div = $('<div></div>');
    let holeimg = $('<img src="top.png" class="top">');
    let moleimg = $('<img src="mole.png" class="mole">');
    div.attr("id", "mole" + i);
    div.append(moleimg);
    div.append(holeimg);

    $("#molewrapper").append(div);
}

function hit(){
    console.log("huh");
    $(this).removeClass("out");
}

function mole(){
    clearInterval(t);
    for(let i in timeout){
        if(timeout[i] > 0) {
            timeout[i]--;
        }else{
            if ($(`#mole${i} .mole`).hasClass("out")) {
                $(`#mole${i} .mole`).removeClass("out");
                $(`#mole${i} .mole`).attr("src","win.png");
                strikes ++;
                $("#messages").text(`Strikes: ${strikes}`);
            }else{
                timeout[i] = 0;
            }
        }
    }

    let choice = Math.floor(Math.random()*16) + 1;
    if ($(`#mole${choice} .mole`).hasClass("out") === false) {
        $(`#mole${choice} .mole`).attr("src", "mole.png");
        $(`#mole${choice} .mole`).addClass("out");
        timeout[choice] = 5;
    }
    if( delay > 100) {
        delay -= 50;
    }
    if(strikes < 3) {
        t = setInterval(mole, delay);
    } else {
        $("#messages").text("Game Over!!!");
        allup();
    }
}

function allup(){
    "use strict";
    for(let i = 1; i <= len; i++) {
        timeout[i - 1] = 0;
        $(`#mole${i} .mole`).addClass("out");
        $(`#mole${i} .mole`).attr("src", "win.png");
    }
}

function alldown(){
    "use strict";
    for(let i = 1; i <= len; i++) {
        timeout[i - 1] = 0;
        $(`#mole${i} .mole`).removeClass("out");
        $(`#mole${i} .mole`).attr("src", "hit.png");
    }
}

$("#start").click(function() {
    "use strict";
    strikes = 0;
    score = 0;
    delay = 4100;
    alldown();
    clearInterval(t);
    t = setInterval(mole, 1000);
    $("#messages").text(`Strikes: ${strikes}`);
    $("#score").text("Score: " + pad(score, 4));
});

$("img").click(function(){
    if($(this).siblings("img").hasClass("out") && strikes < 3) {
        score += 1;
        $("#score").text("Score: " + pad(score, 4));
        $(this).siblings("img").attr("src", "hit.png");
        $(this).siblings("img").removeClass("out");
    }
});