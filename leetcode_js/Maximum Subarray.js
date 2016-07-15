/**
 * @param {number[]} nums
 * @return {number}
 */
// var maxSubArray = function(nums) {
// };
function maxSubArray(nums) {
    if (nums.length == 0) {
        return 0;
    }
    //let localMax:number = Number.MIN_VALUE, globalMax:number = localMax; 
    // Number.MIN_VALUE plus a negative number get 0
    var localMax = 1 << 31 /*negative*/, globalMax = localMax;
    for (var i = 0; i < nums.length; i++) {
        localMax = Math.max(localMax + nums[i], nums[i]);
        globalMax = Math.max(globalMax, localMax);
    }
    return globalMax;
}
