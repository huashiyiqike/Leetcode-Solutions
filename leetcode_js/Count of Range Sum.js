/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
// 滑动窗口不行 二分查找
var countRangeSum = function(nums, lower, upper) {
	var sums=[];
	for(var i = 0; i < nums.length; i++){
		var pre = 0;
		if(sums.length > 0) pre = sums[sums.length-1];
		sums[sums.length] = pre + nums[i]; 
	}
	

};