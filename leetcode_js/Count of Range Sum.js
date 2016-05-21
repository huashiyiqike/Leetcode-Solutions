/**
 * @param {number[]} nums
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
// 滑动窗口不行 二分查找
var countRangeSum = function(nums, lower, upper) {
	var sums = [];
	for(var i = 0; i < nums.length; i++){
		var pre = 0;
		if(sums.length > 0) pre = sums[sums.length-1];
		sums[sums.length] = pre + nums[i]; 
	}
	
};

function heappush(arr, obj){
    arr.push(obj);
    var i = arr.length-1;
    while(i>0){
        var p = Math.floor((i-1)/2);
        if(arr[i][0] > arr[p][0]){ 
            var tmp = arr[i];
            arr[i] = arr[p];
            arr[p] = tmp;
            i = p;
        }else{
            break;
        }
    }
}
 
function heappop(arr){ 
    if(arr.length == 1){
        arr.pop();
        return;
    }
    arr[0] = arr.pop();
    var i = 0;
    while(2*i+1 < arr.length){
        if(2*i+2 >= arr.length){
            if(arr[i][0] < arr[2*i+1][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+1];
                arr[2*i+1] = tmp; 
                i = 2*i + 1;
            }
            return;
        }

        if(arr[2*i+1][0]>arr[2*i+2][0]){
            if(arr[i][0] < arr[2*i+1][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+1];
                arr[2*i+1] = tmp; 
                i = 2*i + 1;
            }
            else if(arr[i][0] < arr[2*i+2][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+2];
                arr[2*i+2] = tmp;
                i = 2*i +2;
            } else{break;}
        }else{
            if(arr[i][0] < arr[2*i+2][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+2];
                arr[2*i+2] = tmp; 
                i = 2*i + 2;
            }
            else if(arr[i][0] < arr[2*i+1][0]){
                var tmp = arr[i];
                arr[i] = arr[2*i+1];
                arr[2*i+1] = tmp;
                i = 2*i +1;
            } else{break;}
        }
    }
}