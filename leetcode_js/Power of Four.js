/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
    return Math.log2(num)%2 == 0;
};