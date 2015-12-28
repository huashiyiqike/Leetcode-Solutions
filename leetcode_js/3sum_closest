var threeSumClosest = function(nums, target) {
	nums.sort(function(a, b){
		return a - b;
	});
	var res = nums[0] + nums[1] + nums[2];
	for(var i = 0; i < nums.length-2; i++){ 
		var start = i+1, end = nums.length-1;
		while(start < end){
			var tmpsum = nums[start] + nums[end] + nums[i];
			if(Math.abs(res - target) > Math.abs(tmpsum - target)) res = tmpsum;
			if(tmpsum < target) start++;
			else if(tmpsum > target) end--;
			else return target;
		}
	}
	return res;
}
console.log(threeSumClosest([-1, 2, 1, -4], 1), 2);
console.log(threeSumClosest([0,2,1,-3], 1), 0);
