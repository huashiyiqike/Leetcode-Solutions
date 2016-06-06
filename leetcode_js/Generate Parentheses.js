/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var res = [];
    recursive(n, n, res, '');
    return res;
};
function recursive(left, right, res, path){
	if(left == 0 && right == 0){
		res.push(path);
		return;
	}
	if(left > right){return;}
	if(left > 0){ 
		recursive(left - 1, right, res, path + '(');
	}
	if(left < right){
		recursive(left, right - 1, res, path + ')');
	}
	
}