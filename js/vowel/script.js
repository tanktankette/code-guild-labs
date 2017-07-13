/**
 * Created by tanktankette on 6/23/17.
 */
alert("It's time to play...");
alert("IS IT A VOWEL?!?!?!");

let c = prompt('Enter a character');

while(c !== ""){
    c.toLowerCase();
    if(c === "a" || c === "e" || c === "i" || c === "o" || c === "u"){
        alert("IT'S A VOWEL! YOU WIN THE GAME!")
    } else if (c === "y") {
        alert("It's a... a 'Y'. Don't know what to do with that... Congrats anyway?")
    } else if (c.length > 1){
        alert("It's not a valid input!")
    } else {
        alert("It's not a vowel!")
    }
    c = prompt('Enter a character');
}

