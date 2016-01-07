//Related to question Excel Sheet Column Title
//
//Given a column title as appear in an Excel sheet, return its corresponding column number.
//
//For example:
//
//    A -> 1
//    B -> 2
//    C -> 3
//    ...
//    Z -> 26
//    AA -> 27
//    AB -> 28 
// https://leetcode.com/problems/excel-sheet-column-number/
/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function(s) {
    var res = 0;
    for(i in s){
        res *= 26;
        res += s[i].charCodeAt() - 'A'.charCodeAt() + 1;
    }
    return res;
};
document.write(titleToNumber("A"));