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
        Object.keys(this.list).forEach(function(item) {
        if (this.list[item] === w){
            results.push(item);
        }});
        return results;
    };

    this.sort = function(){
        var i = 0;
        var newSort = [];
        while (i <= this.highest) {
            var temp = this.collectWeight(i);
            if (temp !== []) {
                newSort.push(temp.sort());
            }
            i++;
        }
        var newList = {};
        newSort.forEach(function(item){
            newList[item] = this.list[item];
        });
        this.list = newList;
    };
}

var t = new Completer();
t.add("baa");
t.add("banana");
t.add("apple");
t.sort();