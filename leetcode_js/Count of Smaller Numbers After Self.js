/**
 * @param {number[]} nums
 * @return {number[]}
 */

var bi_insert = function(num, arr){
	if(arr.length == 0){
		arr.push(num);
		return 0;
	}
	var left = 0, right = arr.length - 1;
	while(left <= right){
		var mid = left+Math.floor((right-left)/2);
		if(arr[mid] >= num){
			right = mid - 1;
		}else{
			left = mid + 1;
		}
	}
	arr.splice(left, 0, num); 
	return left;
};
var countSmaller = function(nums) {
    var sorted = [], res = [];
    for(var i = nums.length - 1; i >= 0; i--){
    	res.unshift(bi_insert(nums.pop(), sorted))
    }
    return res;
};
