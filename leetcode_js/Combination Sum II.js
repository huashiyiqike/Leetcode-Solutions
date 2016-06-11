var combinationSum2 = function(candidates, target){
	res = [];
	helper(candidates.sort(function(a, b){
		return a - b;
	}), target, 0, [], res);
	return res;
}
function helper(candidates, target, start, path, res){
	if(target == 0){
		res.push(path);
		return;
	}
	for(var i = start; i < candidates.length; i++){
		if(target - candidates[start] >= 0){
			if(i != start && candidates[i] == candidates[i-1]){
				continue;
			} 
			helper(candidates, target - candidates[i], i + 1,
				path.concat(candidates[i]) , res);
		}else{
			return;
		}
	}
}
