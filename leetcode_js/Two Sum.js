/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var map = {};
    for(var i = 0; i < nums.length; i++){
        if(!(nums[i] in map)){
            map[target - nums[i]] = i;
        }else{
            return [map[nums[i]]+1,i+1];
        }
    }
};
document.write(twoSum([1,2,3],4))