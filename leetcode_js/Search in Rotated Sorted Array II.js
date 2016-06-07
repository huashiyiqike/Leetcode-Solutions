/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    var left = 0, right = nums.length - 1, mid;
    while(left <= right){
    	mid = left + Math.floor((right - left) / 2);
    	if(nums[mid] == target){return true;}
    	if(nums[mid] <= nums[right]){
    		if(nums[mid] < target && target <= nums[right]){
    			left = mid + 1;
    		}else{
    			right -= 1;
    		}
    	}else{
    		if(nums[left] <= target && target < nums[mid]){
    			right = mid - 1;
    		}else{
    			left += 1;
    		}
    	}
    }
    return false;
};