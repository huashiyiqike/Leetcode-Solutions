/**
 * @param {number[][]} matrix
 * @return {number}
 */
var check = function(matrix, i, j){
    return !(i < 0 || i > matrix.length-1 || j < 0 || j > matrix[0].length-1);
}
var dfs = function(matrix, i, j, vis){
    var res = 1, dir = [[0,1], [0, -1], [-1, 0], [1, 0]];
    for(var m = 0; m < 4; m++){
        var tmpi =  i+dir[m][0], tmpj = j+dir[m][1];
        if(check(matrix, tmpi, tmpj) && matrix[tmpi][tmpj] > matrix[i][j]){ 
            if(vis[tmpi][tmpj] === 0) vis[tmpi][tmpj] = dfs(matrix, tmpi, tmpj, vis);
            res = Math.max(1+vis[tmpi][tmpj], res);
        }
    }
    return res;
}
var longestIncreasingPath = function(matrix) {
    var res = 0, vis = [];
    for(var i = 0; i < matrix.length; i++){
        vis[i] = [];
        for(var j = 0; j < matrix[0].length; j++){
            vis[i][j] = 0;
        }
    }
    if(matrix === null || matrix[0] === null) return res;
    for(var i = 0; i < matrix.length; i++){
        for(var j = 0; j < matrix[0].length; j++){
            res = Math.max(res, dfs(matrix, i, j, vis));
        }
    }
    return res;
};
document.writeln(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]));