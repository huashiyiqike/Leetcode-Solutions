/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    while(num >= 10){
        var res = 0;
        while(num > 0){
            res += num % 10;
            num = Math.floor(num/10);
        }
        num = res;
    }
    return num;
};