/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    var row = [], col = [], x = [];
    for(var i = 0; i < 9; i++){
        row[i] = Array(board[0].length);
        col[i] = Array(board[0].length);
        x[i] = Array(board[0].length); 
    }

    for(var i = 0; i < 9; i++){ 
        for(var j = 0; j < 9; j++){
            var chr = board[i][j];
            if(chr != '.'){  
                row[i][chr - 1] = true;
                col[j][chr - 1] = true;
                x[Math.floor(i/3)*3+Math.floor(j/3)][chr - 1] = true;
            } 
        }
    }
    helper(board, 0, 0); 

    function helper(board, idx, idy){
        if(idy > 8){
            return helper(board, idx + 1, 0);
        }
        if(idx > 8){return true;}
        if(board[idx][idy] != '.'){
            return helper(board, idx, idy + 1);
        }
        for(var i = 0; i < 9; i++){
            if(row[idx][i] || col[idy][i] 
                || x[Math.floor(idx/3)*3+Math.floor(idy/3)][i]){
                continue;
            }
            row[idx][i] = true;
            col[idy][i] = true;
            x[Math.floor(idx/3)*3+Math.floor(idy/3)][i] = true;
            if(helper(board, idx, idy + 1)){
                board[idx][idy] = i + 1 + '';
                return true;
            }
            row[idx][i] = false;
            col[idy][i] = false;
            x[Math.floor(idx/3)*3+Math.floor(idy/3)][i] = false;
        }
        return false;
    }
};