document.getElementById("holdfirst").addEventListener("click", function(e) {
    e.preventDefault();
    hold(0)
});

document.getElementById("holdsecond").addEventListener("click", function(e){
    e.preventDefault();
    hold(1)
});

document.getElementById("roll").addEventListener("click", function(e){
    e.preventDefault();
    if (dice[0].held === false){dice[0].roll()}
    if (dice[1].held === false){dice[1].roll()}
    update();
});

function hold(i){
    if (dice[i].held === false && dice[i].value !== 6) {
        dice[i].held = true;
        dice[1 - i].held = false;
        holdbuttons[i].value = "Die held";
        holdbuttons[1 - i].value = "Hold this die";
    } else if (dice[i].value !== 6){
        dice[i].held = false;
        holdbuttons[i].value = "Hold this die";
    }
}

alert("Let's play a game, try to roll a 1 and a 2 in either order")

function update() {
    document.getElementById("die1").style.backgroundImage = "url(" + pictures[dice[0].value - 1] + ")";
    document.getElementById("die2").style.backgroundImage = "url(" + pictures[dice[1].value - 1] + ")";
    if(dice[0].value === 6){holdbuttons[0].style.background = "gray"}else{holdbuttons[0].style.background = ""}
    if(dice[1].value === 6){holdbuttons[1].style.background = "gray"}else{holdbuttons[1].style.background = ""}
    if(stage === 0 && dice[0].value + dice[1].value === 3){
        stage = 1;
        alert("Stage 1 complete, now go for 3 and 4");
    } else if(stage === 1 && ((dice[0].value === 3 && dice[1].value === 4) || (dice[0].value === 4 && dice[1].value === 3))){
        alert("Stage 2 complete, now go for 5 and 6");
        stage = 2
    } else if(stage === 2 && dice[0].value + dice[1].value === 11){
        alert("You win! Resetting to first stage");
        stage = 0;
    } else if(dice[0].value === 3 && dice[1].value === 3){
        alert("Angry dice!!! Back to first stage, get a 1 and a 2")
        stage = 0;
    }
}

var stage = 0;
var pictures = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png",""];
var holdbuttons = [document.getElementById("holdfirst"), document.getElementById("holdsecond")]

function Die() // Constructor
{
    this.value = 7;
    this.held = false;

    this.roll = function (c) {
        this.value = Math.floor(Math.random() * 6) + 1;
    };
}

dice = [new Die(), new Die()];

update();