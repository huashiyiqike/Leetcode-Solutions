/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    var T = '^#'+s.split("").join("#")+'#$';
    var n = T.length, C = R = 0, P = new Array(n), maxlen = 0, centerIndex = 0;
    for(var i = 0; i < n; i++){
        P[i] = 0;
    }
    for(var i = 1; i < n - 1; i++){
        P[i] = R > i ? Math.min(R - i, P[2 * C - i]):0;
        while(T[i + 1 + P[i]] == T[i - 1 - P[i]]){
            P[i] += 1;
        }
        if(i + P[i] > R){
            C = i;
            R = i + P[i];
        }
    }
    for(var i = 0 ; i < P.length; i++){
        if(P[i] > maxlen){
            maxlen = P[i];
            centerIndex = i;
        }
    }
    return s.slice(Math.floor((centerIndex - maxlen)/2),Math.floor((centerIndex + maxlen)/2));
}



//TLE
var longestPalindrome = function(s) {
	var sets = {}, begin = 0, maxlen = 0;
	for(var i = s.length-1; i >= 0; i--){
		for(var j = i; j < s.length; j++){
			if((j <= i + 1 || [i+1, j-1] in sets) && s[i] == s[j]){
				sets[[i+1, j-1]] = true;
				if(j - i + 1 > maxlen){
					maxlen = j - i + 1;
					begin = i;
				}
			}
		}
	}
	return s.slice(begin, begin + maxlen);
}


 // TLE, java AC
var longestPalindrome = function(s) {
    if(s.length == 0){return s;}
    var dp = new Array(s.length);
    for(var i = 0; i < s.length; i++){
    	dp[i] = new Array(s.length);
    }
    var maxlen = 0, start = 0, end = 0;
    for(var i = 0 ; i < s.length; i++){
    	for(var j = i;  j >= 0; j--){
    		if(i == j){ dp[i][j] = true;}
    		else if(j+1 == i && s[j] == s[i]) {dp[i][j] = true;}
    		else if(dp[i-1][j+1] && s[i] == s[j]) {dp[i][j] = true;}
    		if(dp[i][j]){
    			if(i - j + 1 > maxlen){
    				maxlen = i - j + 1;
    				start = j;
    				end = i;
    			}
    		}
    	}
    }
    return s.slice(start, end + 1);
};