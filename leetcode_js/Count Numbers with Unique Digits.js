/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if(n == 0){return 1;}
    var res = 9, k = 9, total = res + 1;
    n = Math.min(n, 10);
    for(var i = 1; i < n; i++){
    	res *= k--;
    	total += res;
    }
    return total;
};