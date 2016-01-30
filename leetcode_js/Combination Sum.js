/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var helper = function(candidates, target, start, res, path){
    if(target === 0){
        res.push(path);
        return;
    }
    for(var i = start; i < candidates.length; i++){
        if(candidates[i] > target) return;
        helper(candidates, target - candidates[i], i, res, path.concat(candidates[i]));
    }
}
var combinationSum = function(candidates, target) {
    var res = [];
    candidates.sort(function(a, b){return a - b;})
    helper(candidates, target, 0, res, []);
    return res;
};
document.writeln(combinationSum([3,12,9,11,6,7,8,5,4], 15));