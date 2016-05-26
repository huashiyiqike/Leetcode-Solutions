
function NestedInteger(num) {
    this.val = num;
    this.isInteger = function() {
        return this.val.length==1 && typeof(this.val[0]) == "number" ;
    };

    this.getInteger = function() {
        return this.val[0];
    };

    this.getList = function() {
        if(this.val.length > 1){
            return this.val;
        }else{
            return null;
        }
    };
};
 
/**
 * @constructor
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    this.queue = nestedList; 
    this.nexts = null;
};

/**
 * @this NestedIterator
 * @returns {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    if(this.nexts == null){
        var res;
        while(this.queue.length > 0){
            var cur = this.queue.shift();
            if(cur.isInteger()){
                res = cur.getInteger();
                break;
            }else{
                cur = cur.getList();
                if(!cur) break;
                for(var i = cur.length-1; i >= 0; i--){ 
                    this.queue.unshift(cur[i]);
                }
            }
        }
        this.nexts = res;
    }
       
    return !(this.nexts == undefined); 
};

/**
 * @this NestedIterator
 * @returns {integer}
 */
NestedIterator.prototype.next = function() { 
    var res = this.nexts;
    this.nexts = null;
    return res;
};

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/
var a = new NestedInteger([1]), b = new NestedInteger([1]);
var c = new NestedInteger([a,b]);
var d = new NestedInteger([2]);
var e = new NestedInteger([1]), f = new NestedInteger([1]);
var g = new NestedInteger([e,f]);
var x = new NestedInteger([c, d, g]);
var i = new NestedIterator(x), m = [];
while (i.hasNext())
 m.push(i.next());
console.log(m);
var i = new NestedIterator([new NestedInteger([])]);
while (i.hasNext())
 m.push(i.next());
console.log(m);
