/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @constructor
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    this.cur = 0;
    this.list = []; 
    this.nestedList = nestedList;
};


/**
 * @this NestedIterator
 * @returns {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    return !(this.list.length == 0 && this.cur == this.nestedList.length);
};

/**
 * @this NestedIterator
 * @returns {integer}
 */

NestedIterator.prototype.next = function() { 
    if(this.list.length != 0){
        var iter = new NestedIterator(this.list);
        return iter.next();
    }else{
        if(this.cur  < this.nestedList.length){
             var tmp = this.nestedList[this.cur++]; 
             this.nestedList.shift();
             if(tmp.isInteger()){
                 return tmp.getInteger();
             }else{
                 this.list = tmp.getList();
                 return this.list.shift();
             }
        } 
    }
};

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/