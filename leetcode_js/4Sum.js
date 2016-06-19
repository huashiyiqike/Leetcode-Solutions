/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    var res = [];
    nums.sort(function(a,b){return a-b;})
    for(var i = 0; i < nums.length-3; i++){
        if(i > 0 && nums[i] === nums[i-1]) continue;
        var res1 = nums[i];
        for(var j = i+1; j < nums.length-2; j++){
            if(j>i+1 && nums[j] === nums[j-1]) continue;
            var res2 = nums[j];
            var left = j+1, right = nums.length-1;
            while(left < right){
                sum = res1+res2+nums[left]+nums[right];
                if(sum < target){
                    left++;
                }else if(sum > target){
                    right--;
                }else{
                    var res3 = nums[left], res4 = nums[right];
                    res.push([res1, res2, res3, res4]); 
                    while(left < nums.length && nums[left] === res3) left++;
                    while(right >= 0 && nums[right] === res4) right--; 
                }
                
            }
            
        }
    }
    return res;
};
 
// WA
var twoSum = function(nums, start, res, target, tmpres){
    var map = {};
    for(var i = start; i < nums.length; i++){
        if(nums[i] in map){
            res.push( [ nums[tmpres[0]], nums[tmpres[1]], nums[map[nums[i]]], nums[i] ] );
        }else{
            map[target-nums[i]] = i;
        }
    }
}
var fourSum = function(nums, target) {
    nums.sort(function(a,b){
        return a-b;
    });
    var res = [];
    for(var i = 0 ; i < nums.length-3; i++){
        for(var j = i+1; j < nums.length-2; j++){
            if(j > 0 && j> i+1 && nums[j] == nums[j-1]) 
                continue;
            twoSum(nums, j+1, res, target-nums[i]-nums[j], [i, j]);
        }
    }
    return res;
}; 