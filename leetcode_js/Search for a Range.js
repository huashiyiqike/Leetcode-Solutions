/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    var mid, left = 0, right = nums.length - 1;
    while(left <= right){
    	mid = left + Math.floor((right - left)/2);
    	if(nums[mid] < target){
    		left = mid + 1;
    	}else{
    		right = mid - 1;
    	}
    }
    var resleft = left;
    left = 0/*or right, saves time*/, right = nums.length - 1;
    while(left <= right){
    	mid = left + Math.floor((right - left)/2);
    	if(target < nums[mid]){
    		right = mid - 1;
    	}else{
    		left = mid + 1;
    	}
    }
    var resright = right;
    return resleft <= resright ? [resleft, resright]:[-1, -1];
};