/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
	var s = s.split('');
    var vow = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1};
    var le = 0, ri = s.length - 1;
    while(le < ri){
    	while(le < s.length && !(s[le] in vow)){
    		le++;
    	}
    	while(ri >= 0 && !(s[ri] in vow)){
    		ri--;
    	}
    	if(le < ri){
    		var tmp = s[le];
    		s[le] = s[ri];
    		s[ri] = tmp;
    	}
    	le++;
    	ri--;
    }
    return s.join('');
};