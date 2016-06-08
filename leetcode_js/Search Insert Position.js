/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var l = 0, r = nums.length - 1;
    while(l <= r){
    	mid = l + Math.floor((r-l)/2);
    	if(nums[mid] > target){
    		r = mid - 1;
    	}else if(nums[mid] < target){
    		l = mid + 1;
    	}else{
    		return mid;
    	}
    }
    return l;
};