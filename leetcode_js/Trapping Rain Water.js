/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    if(height.length == 0){return 0;}
    var maxs = Math.max(height), maxs_idx = height.indexOf(maxs); 
    var left = height[0], right = height[1], res = 0;
    for(var i = 1; i < maxs_idx; i++){
    	if(height[i] > left){
    		left = height[i];
    	}else{
    		res += left - height[i];
    	}
    }
    for(var i = maxs_idx - 1; i > maxs_idx; i--){
    	if(height[i] > right){
    		right = height[i];
    	}else{
    		res += right - height[i];
    	}
    }
    return res;
};