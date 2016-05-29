/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if(numRows == 1){return s;}
    else if(numRows <= 0 || s == ""){return "";}
    var step = 2 * numRows - 2, res = '';
    for(var i = 0 ; i < numRows; i++){
        for(var j = i; j < s.length; j += step){
            res += s[j];
            if(0 < i && i < numRows - 1 && j + step - 2 * i < s.length){
                res += s[j + step - 2 * i];
            } 
        }
    }
    return res;
};