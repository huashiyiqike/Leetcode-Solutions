/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var cur = 0;
    for(var i = 0; i < nums.length; i++){
    	if(nums[i] != val){
    		nums[cur++] = nums[i];
    	}
    }
    return cur;
};