/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var helper = function(nums, start, path, res){
    res.push(path);
    for(var i = start; i < nums.length; i++){
        helper(nums, i+1, path.concat(nums[i]), res);
    }
//    if(path.length > 0) res.push(path);
//    for(var i = start; i < nums.length; i++){
//        helper(nums, i+1, path, res);
//        helper(nums, i+1, path.concat(nums[i]), res);
//    }
}
var subsets = function(nums) {
    nums.sort(function(a,b){return a-b;})
    var res = [];
    helper(nums, 0, [], res);
    return res;
};