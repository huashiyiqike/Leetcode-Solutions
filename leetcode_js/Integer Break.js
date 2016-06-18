/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
	if(n == 2){
		return 1;
	}else if(n == 3){
		return 2;
	}
	var res = 1;
    while(n > 4){
    	res *= 3;
    	n -= 3;
    }
    return res * n;
};