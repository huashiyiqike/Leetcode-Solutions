/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    var l = 0, r = nums.length - 1;
    while(l <= r){
    	var mid = left + Math.floor((r - l)/2);
    	if(nums[mid] >= nums[0]){
    		l = mid + 1;
    	}else{
    		r = mid - 1;
    	}
    }
    return l < nums.length? nums[l]:nums[0];
};