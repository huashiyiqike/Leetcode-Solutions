
var largestNumber = function(nums) {
    nums.sort(function(a, b){
        var x = a + '' + b, y = b + '' + a;
        return Number(y) - Number(x);
    })
    var res = '';
    nums = nums.map(String).reduce(function(a,b){return a+b;});
    if(nums[0] === '0') return '0';
    return nums;
}
document.writeln(largestNumber([3,55,9]));
document.writeln(largestNumber([3,55,9,0]));
document.writeln(largestNumber([3,55,9,0, 9]));