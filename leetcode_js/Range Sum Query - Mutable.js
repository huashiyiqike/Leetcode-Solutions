/**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    var res = [], sum = 0;
    for(var i = 0; i < nums.length; i++){
    	sum += nums[i];
    	res.push(sum);
    }
    this.origin = nums;
    this.accum = res;
};

/**
 * @param {number} i
 * @param {number} val
 * @return {void}
 */
NumArray.prototype.update = function(i, val) {
	var before = this.origin[i];
	var diff = val - this.origin[i];
    this.origin[i] = val;
    for(var m = i; m < this.accum.length; m++){
    	this.accum[m] += diff;
    }
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.accum[j] - this.accum[i] + this.origin[i];
};



/**
 * Your NumArray object will be instantiated and called as such:
 * var numArray = new NumArray(nums);
 * numArray.sumRange(0, 1);
 * numArray.update(1, 10);
 * numArray.sumRange(0, 2);
 */