/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
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
            console.log(vis);
            var tmp_path = path.slice();
            tmp_path.push(nums[i]);
            helper(nums, res, tmp_path, vis);
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

 

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/
//console.log(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]));

console.log(permuteUnique([1, 1, 2]));
