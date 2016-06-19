/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    var dict = {};
    for(var i = 0; i < tickets.length; i++){
        if(tickets[i][0] in dict){
            dict[tickets[i][0]].push(tickets[i][1]);
        }else{
            dict[tickets[i][0]] = [tickets[i][1]];
        }
    }
    for(var i in dict){
        dict[i].sort();
    }
    var res = ["JFK"];
    for(var i = 0; i < tickets.length; i++){
        var key = res[res.length - 1];
        res.push(dict[key][0]);
        dict[key].shift();
    }
    return res;
};

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/
//console.log(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]));

console.log(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]));
