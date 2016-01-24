/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    if(str.length === 0) return 0;
    var res = 0, sign = 1;
    str = str.trim(' ')
    if(str[0] === "-"){
        sign = -1;
        str = str.substr(1, str.length);
    }else if(str[0] === "+"){
        str = str.substr(1, str.length);
    }
    while(str.length > 0 && str[0] === "0"){
        str = str.substr(1, str.length);
    }
    for(var i = 0; i < str.length; i++){
        if(str[i] > "9" || str[i] < "0" ){ 
            break;
        }
        res *= 10;
        res += new Number(str[i]);
    }
    if(sign === 1 && res > 2147483647){ //Math.pow(2, 31) - 1)
            res = 2147483647;
    }
    if(res > 2147483648){
            res = 2147483648;
    }

    return res * sign;   
};