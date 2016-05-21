/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var hash = [], heap = [], res = [];
    for(var i in nums){
    	hash[nums[i]] = hash[nums[i]] !== undefined? hash[nums[i]]+1 : 1;
    }
    for(i = 0; i < hash.length; i++){
    	heappush(heap, hash[i]);
    }
    for(i = 0; i < k; i++){
    	res.push(heap[0][1]);
    	heappop(heap);
    }
    return res;
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