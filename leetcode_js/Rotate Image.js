/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
    for (var i = 0; i < matrix.length / 2; i++) {
        for (var j = 0; j < matrix[0].length; j++) {
            var op = matrix.length - 1 - i;
            var tmp = matrix[op][j];
            matrix[op][j] = matrix[i][j];
            matrix[i][j] = tmp;
        }
    }
    for (var i = 0; i < matrix.length; i++) {
        for (var j = i + 1; j < matrix[0].length; j++) {
            var tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }
};
