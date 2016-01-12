/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    var dp = [];
    for(var i = 0; i < triangle.length; i++){
        dp[i] = triangle[triangle.length - 1][i];
    }
    for(i = triangle.length-1; i >= 0; i--){
        for(var j = 0; j < i; j++){
            dp[j] = triangle[i][j] + Math.min(dp[j], dp[j+1]);
        }
    }
    return dp[0];
};