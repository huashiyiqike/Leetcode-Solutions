/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    if(s.length == 0 || p.length == 0){
    	return true;
    }else if(p.length == 0){
    	return false;
    }
    if(s != '' && s[0] == p[0]){
    	if(p.length > 1 && p[1] == '*'){
    		return isMatch(s, p.slice(2)) ||
    		isMatch(s.slice(1), p);
    	}else{
    		return isMatch(s.slice(1), p.slice(1));
    	}
    }else if(s != '' && p[0] == '.'){
    	if(p.length > 1 && p[1] == '*'){
    		return isMatch(s, p.slice(2)) ||
    		isMatch(s.slice(1), p);
    	}else{
    		return isMatch(s.slice(1), p.slice(1));
    	}
    }else if(p.length > 1 && p[1] == '*'){
    	return isMatch(s, p.slice(2));
    }
    return false;
};