/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var left = 0, right = nums.length - 1, mid;
    while(left <= right){
    	mid = left + Math.floor((right - left) / 2);
    	if(nums[mid] == target) return mid;
    	if(nums[mid] < nums[right]){
    		if(nums[mid] < target && target <= nums[right]){
	    		left = mid + 1;
	    	}else{
	    		right = mid - 1;
	    	}
    	}else{
    		if(nums[left] <= target && target < nums[mid]){
    			right = mid - 1;
    		}else{
    			left = mid + 1;
    		}
    	}
    }
    return -1;
};