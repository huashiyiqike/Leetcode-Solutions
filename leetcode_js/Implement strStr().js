/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
	if(haystack === needle) return 0;
	if(haystack.length === 0) return -1;
	var fCheck = function(i){
		for(var j = 0 ; j < needle.length ; j++){
			if(haystack[j+i] !== needle[j]) return false;
		}
		return true;
	}
	for(var i = 0 ; i < haystack.length - needle.length + 1 ; i++){
		if(fCheck(i)) return i;
	}    
	return -1;
};