/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
	if(digits.length == 0){return [];}
    var maps = ['', '', 'abc', 'def', 'ghi', 'jkl', 
    'mno', 'qprs', 'tuv', 'wxyz'];
    var res = [];
    bfs(res, '', 0);
    return res;

    function bfs(res, path, idx){
    	if(idx == digits.length){
    		res.push(path);
    		return;
    	}
    	var choices = maps[+digits[idx]];
    	for(var c in choices){
    		bfs(res, path+choices[c], idx+1);
    	}
	}
};

