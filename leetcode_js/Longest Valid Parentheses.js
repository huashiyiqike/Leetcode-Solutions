/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    var stack = [], left = maxlen = 0;
    for(var i = 0; i < s.length; i++){
    	if(s[i] == '('){
    		stack.push(i);
    	}else{
    		if(stack.length == 0){
    			left = i+1;
    		}else{
    			stack.pop();
    			if(stack.length == 0){
    				maxlen = Math.max(maxlen, i - left + 1);
    			}else{
    				maxlen = Math.max(maxlen, 
    					i - stack[stack.length - 1] + 1);
    			}
    		}
    	}
    }
    return maxlen;
};