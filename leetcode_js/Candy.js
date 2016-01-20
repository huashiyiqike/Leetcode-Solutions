/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    var left = new Array(), right = new Array();
    for(var i = 0; i < ratings.length; i++){
        left[i] = 1;
        right[i] = 1;
    }
    for(i = 1; i < ratings.length; i++){
        if(ratings[i] > ratings[i-1]) left[i] = left[i-1] + 1;
        var tmp = ratings.length - i;
        if(ratings[tmp-1] > ratings[tmp]){ 
            right[tmp-1] = right[tmp]+1;
        }
    }
    for( i = 0 ; i < ratings.length; i++){
        left[i] = Math.max(left[i], right[i]);
    }
    return left.reduce(function(a,b){return a+b;});
};
document.writeln(candy([1,2,3]))