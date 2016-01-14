/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    var res = new Array(n);
    for(var i = 2; i < n; i++) res[i] = 1;
    for(var i = 2; i < Math.floor(Math.sqrt(n))+1; i++){
        for(var j = i*2; j < n; j += i){
            res[j] = 0;
        }
    }
    var re = 0;
    for(i = 0; i < n; i++){
        if(res[i] === 1) re += 1;
    }
    return re;
};