/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    if(s.length < p.split("*").join("").length){
        return false;
    }
    var dp = new Array(s.length + 1);
    
    for(var i = 0; i < s.length + 1; i++){
        dp[i] = new Array(p.length + 1);
        for(var j = 0; j < p.length+1; j++){ 
            dp[i][j] = false;
        }
        dp[0][0] = true;
    }
    for(i = 1; i < p.length+1; i++){
        if(dp[0][i-1] && p[i-1] == '*'){
            dp[0][i] = true;
        }
    }

    for(var i = 1; i < s.length+1; i++){
        for(var j = 1; j < p.length+1; j++){
            if((p[j - 1] === '?' || s[i-1] == p[j - 1] )
                && dp[i - 1][j - 1]){
                dp[i][j] = true;
            }else if(p[j-1] == '*' && (dp[i - 1][j - 1] ||
                dp[i][j - 1] || dp[i - 1][j])){
                dp[i][j] = true;
            }
        }
    }
    return dp[dp.length - 1][dp[0].length - 1];
};