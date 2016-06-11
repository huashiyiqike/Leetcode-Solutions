var countAndSay = function(n){
	strs = '1';
	for(var i = 0 ; i < n - 1; i++){
		strs = nexts(strs);
	}
	return strs;
}
function nexts(strs){
	var left = right = 0, res = '';
	while(left < strs.length){
		while(right < strs.length && strs[right] === strs[left]){
			right++;
		}
		res += (right - left) + strs[left];
		left = right;
	}
	return res;
}