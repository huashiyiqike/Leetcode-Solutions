/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var dict = {}, start = 0, res = 0;
    for(var i = 0; i < s.length; i++){
    	if(s[i] in dict && dict[s[i]] >= start){
    		start = dict[s[i]] + 1;
    	}
    	dict[s[i]] = i;
    	res = Math.max(res, i - start + 1);
    }
    return res;
};