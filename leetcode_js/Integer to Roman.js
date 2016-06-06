/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    var value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    var res = '';
    while(num > 0){
    	for(var i = 0; i < value.length; i++){
    		while(num >= value[i]){
    			res += symbol[i];
    			num -= value[i];
    		}
    		// more geek
    		// var n = Math.floor(num/value[i]); 
    		// if(n != 0){
    		// 	res += new Array(n + 1).join(symbol[i]);
    		// 	num %= value[i];
    		// }
    	}
    }
    return res;
};