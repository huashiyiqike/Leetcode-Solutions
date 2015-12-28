var threeSum = function(nums){
	nums.sort(function(a,b){
		return a-b;
	});
	var res = [], len = nums.length;
	for(var i = 0 ; i < len - 2; i++){
		if (i !== 0 && nums[i] === nums[i - 1]) continue;
		var target = - nums[i], start = i+1, end = len-1;
		while(start < end){
			var tmpsum = nums[start] + nums[end];
			if(tmpsum < target){
				start++;
			}else if(tmpsum > target){
				end--;
			}else{
				res.push([nums[i], nums[start++], nums[end]]);
				while(start <= end){
					if(nums[start] > nums[start-1]) break;
					 start++;
				}
			}
		}
	}
	return res;
}
console.log(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]);
