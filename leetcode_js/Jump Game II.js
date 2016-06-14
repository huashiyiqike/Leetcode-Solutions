/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
  	var dp = Array(nums.length), maxs = 0;
  	dp[0] = 0;
  	for(var i = 0; i < nums.length; i++){
  		if(i + nums[i] > maxs){
  			for(var j = maxs + 1; j < i + nums[i] + 1; j++){
  				if(j < dp.length){
  					dp[j] = dp[i] + 1;
  				}
  			}
  			maxs = i + nums[i];
  		}
  	}  
  	return dp[dp.length - 1];
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    var cur = maxl = last = step = 0;
    while(cur < nums.length - 1){
    	maxl = Math.max(maxl, cur + nums[cur]);
    	for(var i = last; i < cur; i++){
    		maxl = Math.max(maxl, i + nums[i]);
    	}
    	last = cur;
    	cur = maxl;
    	step += 1;
    }
    return step;
};

