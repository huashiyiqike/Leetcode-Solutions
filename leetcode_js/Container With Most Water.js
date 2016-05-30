/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var left = 0, right = height.length - 1, max = 0;
    while(left < right){
    	max = Math.max(max, (right - left)*Math.min(height[left], height[right]));
    	if(height[left] < height[right]){
    		left++;
    	}else{
    		right--;
    	}
    }
    return max;
};