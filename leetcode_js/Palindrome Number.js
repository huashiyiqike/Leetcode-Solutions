/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0){return false;}
    var num = x, digits = -1;
    while(num > 0){
    	digits += 1;
    	num /= 10;
    }
    while(x > 0){
    	if(Math.floor(x / Math.pow(10, digits)) != x % 10){
    		return false;
    	}
    	x %= Math.pow(10, digits);
    	x = Math.floor(x/10);
    	digits -= 2;
    }
    return true;
};