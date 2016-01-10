/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort(function(a,b){return a-b;})
    var res = [];
    helper(nums, 0, [], res);
    return res;
};
var helper = function(nums, start, path, res){
    res.push(path);
    for(var i = start; i < nums.length; i++){
        if(i > start && nums[i] == nums[i-1]) continue;
        helper(nums, i+1, path.concat(nums[i]), res);
    }
}