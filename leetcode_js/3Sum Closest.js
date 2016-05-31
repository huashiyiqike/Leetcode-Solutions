/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort(function(a,b){return a - b;})
    var res = nums[0] + nums[1] + nums[2];
    for(var i = 0; i < nums.length -2; i++){
    	var le = i + 1, ri = nums.length - 1;
    	while(le < ri){
    		var tmp = nums[i] + nums[le] + nums[ri];
    		if(tmp < target){
    			le++;
    		}else if(tmp > target){
    			ri--;
    		}else{
    			return target;
    		}
    		if(Math.abs(target - tmp) <
    		 Math.abs(res - target)){
    			res = tmp;
    		}
    	}
    }
    return res;
};