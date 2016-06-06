/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
	if(nums.length == 0){return 0;}
    var cur = 0;
    for(var i = 0; i < nums.length - 1; i++){
    	if(nums[i+1] !== nums[cur]){
    		nums[++cur] = nums[i+1];
    	}
    }
    nums = nums.slice(0, cur+1);
    return cur + 1;
};