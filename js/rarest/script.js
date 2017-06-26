/**
 * Created by tanktankette on 6/26/17.
 */
var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

function findRarestValue(obj){
    var freq = new Object();
    Object.values(obj).forEach(function(item) {
        if (freq[item] !== undefined) {
            freq[item] = freq[item] + 1;
        } else {
            freq[item] = 1;
        }
    });

    var least = -1;
    Object.keys(freq).forEach(function(item) {
        if(freq[item] < freq[least] || least === -1){
            least = item
        }
    });
    return least;
}

function getKeysByValue(v, obj) {
    var results = [];
    Object.keys(obj).forEach(function(item) {
        if (obj[item].toString() === v.toString()){
            results.push(item);
        }
    });
    return results;
}

function findRarestKeys(obj) {
    return getKeysByValue(findRarestValue(obj), obj);
}

console.log(findRarestValue(namesToAges));
console.log(findRarestKeys(namesToAges));