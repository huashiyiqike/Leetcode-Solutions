/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    var idx = 0;
    while(idx < nums.length){
    	if(nums[idx] > 0 && nums[idx] <= nums.length && 
    		nums[idx] !== nums[nums[idx]-1]){
    		var tmp = nums[nums[idx] - 1];
    		nums[nums[idx] - 1] = nums[idx];
    		nums[idx] = tmp;
    	}else{
    		idx++;
    	}
    }
    for(var i = 0; i< nums.length; i++){
    	if(i+1 != nums[i]){
    		return i+1;
    	}
    }
    return nums.length + 1;
};