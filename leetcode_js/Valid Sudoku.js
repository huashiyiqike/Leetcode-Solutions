/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var row = [], col = [], x = [];
    for(var i = 0; i < 9; i++){
    	row[i] = Array(board[0].length);
    	col[i] = Array(board[0].length);
    	x[i] = Array(board[0].length);
    	for(var j = 0; j < 9; j++){
    		row[i][j] = false;
    		col[i][j] = false;
    		x[i][j] = false;
    	}
    }
    for(var i = 0; i < 9; i++){
    	for(var j = 0; j < 9; j++){
    		var num = board[i][j];
    		if(num != '.'){
    			var k = Math.floor(i/3)*3 + Math.floor(j/3);
    			if(row[i][num] || col[j][num] 
    				|| x[k][num]){
    				return false;
    			}
    			row[i][num] = col[j][num] = x[k][num];
    		}
    	}
    }
    return true;
};