var containsNearbyAlmostDuplicate = function(nums, k, t) { 
	var idx_arr = [];
	for(var i = 0; i < nums.length; i++){
		idx_arr.push(i);
	}
	idx_arr.sort(function(a, b){
		return nums[a] - nums[b];
	});
	for(var i = 0; i < nums.length; i++){
		var j = i+1; 
		while(j < nums.length && nums[idx_arr[j]] - nums[idx_arr[i]] <= t){
			if(Math.abs(idx_arr[i] - idx_arr[j]) <= k){
				return true;
			}
			j++;
		}
	}
    return false;
};