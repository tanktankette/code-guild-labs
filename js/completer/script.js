/**
 * Created by tanktankette on 6/26/17.
 */
function Completer() {
    this.list = {};
    this.highest = 0;

    this.complete = function (word) {
        let results = this.check(word);
        if(results.length > 0) {
            return results;
        }

        let e1 = this.edits(word);
        for(e in e1) {
            results = results.concat(this.check(e1[e]));
        }

        if (results.length > 0) {
            return this.prune(results);
        }

        let e2 = this.secondedits(e1);
        for(e in e2) {
            results = results.concat(this.check(e2[e]));
        }

        if (results.length > 0) {
            return this.prune(results);
        } else {return "Nothing found"}

    };

    this.check = function(word){
        "use strict";
        let results = [];
        Object.keys(this.list).forEach(function (item) {
            if (item.toString().includes(word)) {
                results.push(item);
            }
        });
        return results;
    };

    this.prune = function(results){
        "use strict";
        for (let w1 in results){
            let w2 = parseInt(w1) + 1;
            while (w2 < results.length){
                if(results[w1] === results[w2]){
                    results.splice(w2, 1);
                } else {w2++}
            }
        }
        return results
    };

    this.add = function (word) {
        this.list[word] = 0;
    };

    this.select = function (word) {
        this.list[word] += 1;
        if (this.list[word] > this.highest) {
            this.highest = this.list[word];
        }
        this.sort();
    };

    this.collectWeight = function (w) {
        let results = [];
        for (let key in this.list) {
            if (this.list[key] === w) {
                results.push(key);
            }
        }
        return results;
    };

    this.sort = function () {
        let i = this.highest;
        let newSort = [];
        while (i >= 0) {
            let temp = this.collectWeight(i);
            if (temp !== []) {
                temp.sort();
                newSort = newSort.concat(temp);
            }
            i--;
        }
        let newList = {};
        for (let key in newSort) {
            key = newSort[key];
            newList[key] = this.list[key];
        }
        this.list = newList;
    };


    this.edits = function (word) {
        "use strict";
        let letters = "abcdefghijklmnopqrstuvwxyz";
        let flips = [];
        let deletes = [];
        let inserts = [];
        let replaces = [];
        for(let i = 0; i < word.length; i++){
            let start = word.slice(0,i);
            let end = word.slice(i);
            deletes.push(start + end.slice(1));
            if(end.length >=2){
                flips.push(start + end[1] + end[0] + end.slice(2));
            }
            for(let l in letters) {
                inserts.push(start + letters[l] + end);
                replaces.push(start + letters[l] + end.slice(1))
            }
        }
        return flips.concat(deletes, inserts, replaces);
    };

    this.secondedits = function (words) {
        "use strict";
        let results = [];
        for(let w in words){
            results = results.concat(this.edits(words[w]));
        }
        return results;
    }

}

let t = new Completer();
t.add("baa");
t.add("banana");
t.add("apple");
t.select("banana");
t.sort();