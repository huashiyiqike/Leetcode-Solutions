/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var helper = function (nums, res, path, vis) {
    if (path.length == nums.length) {
        res.push(path.slice());
        return;
    }
    for (var i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] == nums[i - 1] && vis[i - 1]) {
            continue;
        }
        if (!vis[i]) {
            vis[i] = true;
            path.push(nums[i]);
            helper(nums, res, path, vis);
            path.pop();
            vis[i] = false;
        }
    }
};
var permuteUnique = function (nums) {
    nums = nums.sort(function (a, b) { return a - b; });
    var res = [];
    var vis = [];
    for (var i = 0; i < nums.length; i++) {
        vis[i] = false;
    }
    helper(nums, res, [], vis);
    return res;
};
