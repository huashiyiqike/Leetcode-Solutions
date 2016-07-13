/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    nums.sort(function(a, b){return a - b;});
    var len = nums.length, mid = Math.floor((len-1)/2);
    var index = 0;
    var arr = Array(len);
    for(var i = 0; i <= mid ;i++){
      arr[index] = nums[mid-i];
      if((index + 1) < len){
        arr[index+1] = nums[len-i-1];
      }
      index += 2;
    }
    for(var i = 0; i < len; i++){
      nums[i] = arr[i];
    }
};

 