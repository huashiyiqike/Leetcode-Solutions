/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
 */
var minPatches = function(nums, n) {
    var reach = count = idx = 0;
    while(reach < n){
    	if(idx < nums.length && nums[idx] <= reach + 1){
    		reach += nums[idx++];
    	}else{
    		reach += reach + 1;
    		count++;
    	}
    }
    return count;
};