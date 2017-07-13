const holdbuttons = [$("#holdfirst"), $("#holdsecond")];

holdbuttons[0].click(function(e) {
    e.preventDefault();
    hold(0)
});
holdbuttons[1].click(function(e){
    e.preventDefault();
    hold(1)
});



$("#roll").click( function(e){
    e.preventDefault();
    if (dice[0].held === false){dice[0].roll()}
    if (dice[1].held === false){dice[1].roll()}
    update();
});

function hold(i){
    if (dice[i].held === false && dice[i].value !== 6) {
        dice[i].held = true;
        dice[1 - i].held = false;
            console.log("test");
        holdbuttons[i].val("Die held");
        holdbuttons[1 - i].val("Hold this die");
            console.log("test");
    } else if (dice[i].value !== 6){
        dice[i].held = false;
        holdbuttons[i].val("Hold this die");
    }
}

function update() {
    $("#die1").css("background", pictures[dice[0].value - 1]);
    $("#die2").css("background", pictures[dice[1].value - 1]);
    if(dice[0].value === 6){holdbuttons[0].css("background", "gray")}else{holdbuttons[0].css("background", "")}
    if(dice[1].value === 6){holdbuttons[1].css("background", "gray")}else{holdbuttons[1].css("background", "")}
    if(stage === 0 && dice[0].value + dice[1].value === 3){
        stage = 1;
        alert("Stage 1 complete, now go for 3 and 4");
    } else if(stage === 1 && ((dice[0].value === 3 && dice[1].value === 4) || (dice[0].value === 4 && dice[1].value === 3))){
        alert("Stage 2 complete, now go for 5 and 6");
        stage = 2;
    } else if(stage === 2 && dice[0].value + dice[1].value === 11){
        alert("You win! Resetting to first stage");
        stage = 0;
    } else if(dice[0].value === 3 && dice[1].value === 3){
        alert("Angry dice!!! Back to first stage, get a 1 and a 2");
        stage = 0;
    }
}

function Die() {
    this.value = 7;
    this.held = false;

    this.roll = function (c) {
        this.value = Math.floor(Math.random() * 6) + 1;
    };
}

let stage = 0;
let pictures = ["url(dice1.png)","url(dice2.png)","url(dice3.png)","url(dice4.png)","url(dice5.png)","url(dice6.png)","gray"];


alert("Let's play a game, try to roll a 1 and a 2 in either order\nThe jumping ferret is a three, if you roll two threes the game is reset");

dice = [new Die(), new Die()];

update();