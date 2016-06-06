/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length == 0){return "";}
    var longest = strs[0];
    for(var i = 1; i < strs.length; i++){
    	var maxlen = 0;
    	while(maxlen < strs[i].length && maxlen < longest.length 
    		&& strs[i][maxlen] == longest[maxlen]){
    		maxlen++;
    	}
    	longest = longest.slice(0, maxlen);
    }
    return longest;
};