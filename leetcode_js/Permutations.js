/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
   var res = [], flag = [], path = [];
   for(var i = 0; i < nums.length; i++){flag.push(false);}
   function dfs(){
   		if(path.length == nums.length){
   			res.push(path.slice());
   			return;
   		}
   		for(var i = 0; i < nums.length; i++){
   			if(!flag[i]){
   				flag[i] = true;
   				path.push(nums[i]);
   				dfs();
   				flag[i] = false;
   				path.pop();
   			}
   		}
   } 
   dfs();
   return res;
};


/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    nums = nums.sort(function(a, b){
    	return a - b;
    }); 
    var res = [];
    while(nums){
    	res.push(nums.slice(0));
    	nums = next(nums); 
    }
    return res;
};
function next(cur){
	for(var j = cur.length - 2; j > -1; j--){
		for(var i = cur.length - 1; i > j; i--){
			if(cur[i] > cur[j]){
				var tmp = cur[j];
				cur[j] = cur[i];
				cur[i] = tmp;
				var k = j + 1, m = cur.length - 1;
				while(k < m){
					var tmp = cur[k];
					cur[k++] = cur[m];
					cur[m--] = tmp;
				}  
				return cur;
			}
		}
	}
	return false;
}