/**
 * @param {string} s
 * @return {boolean}
 */
var checkdigit = function(s){
    for(var i = 0; i < s.length; i++){
        if(s[i] > "9" || s[i] < "0") return false;
    }
    return true;
}
var check = function(s){
    if(s === "." || s.length === 0) return false;
    s = s.split(".");
    if(s.length > 2) return false;
    if(s.length === 2){
        return checkdigit(s[0]) && checkdigit(s[1]);
    }
    return checkdigit(s[0]);
}
var isNumber = function(s) {
    s = s.trim();
    if(s.length === 0) return false;
    if(s[0] === "+" || s[0] === "-") s = s.substr(1, s.length);
    s = s.split("e");
    if(s.length > 2) return false;
    if(s.length === 1) return check(s[0]);
    if(s[1][0] === "+" || s[1][0] === "-") s[1] = s[1].substr(1, s[1].length);
    if(s[1].length === 0) return false;
    return checkdigit(s[1]) && check(s[0]);
};
document.writeln(isNumber("6e6.5"));
document.writeln(isNumber("-1."));