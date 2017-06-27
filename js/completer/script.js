/**
 * Created by tanktankette on 6/26/17.
 */
function Completer() {
    this.list = {};
    this.highest = 0;

    this.complete = function(word){
        var results = [];
        Object.keys(this.list).forEach(function(item) {
        if (item.toString().includes(word)){
            results.push(item);
        }});
        return results;
    };

    this.add = function(word){
        this.list[word] = 0;
    };

    this.select = function(word){
      this.list[word] += 1;
      if(this.list[word] > this.highest){
          this.highest = this.list[word];
      }
    };

    this.collectWeight = function(w){
        var results = [];
        for(var key in this.list){
            if (this.list[key] === w){
                results.push(key);
            }
        }
        return results;
    };

    this.sort = function(){
        var i = this.highest;
        var newSort = [];
        while (i >= 0) {
            var temp = this.collectWeight(i);
            if (temp !== []) {
                temp.sort();
                newSort = newSort.concat(temp);
            }
            i--;
        }
        var newList = {};
        for(var key in newSort){
            key = newSort[key];
            newList[key] = this.list[key];
        }
        this.list = newList;
    };
}

var t = new Completer();
t.add("baa");
t.add("banana");
t.add("apple");
t.select("banana");
t.sort();