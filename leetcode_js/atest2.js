/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
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

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/
var m  = longestPalindrome("a");
console.log(m);
