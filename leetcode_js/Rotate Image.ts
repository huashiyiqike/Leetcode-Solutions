/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

let rotate :(matrix:number[][])=>any
 = function(matrix:number[][]) {
 	for(let i:number = 0; i < matrix.length/2; i++){
 		for(let j:number = 0; j < matrix[0].length; j++){
 			let op:number = matrix.length - 1 - i;
 			let tmp: number = matrix[op][j];
 			matrix[op][j] = matrix[i][j];
 			matrix[i][j] = tmp;
 		}
 	}
 	for(let i: number = 0; i < matrix.length; i++){
 		for(let j: number = i + 1; j < matrix[0].length; j++){
 			let tmp: number = matrix[i][j];
 			matrix[i][j] = matrix[j][i];
 			matrix[j][i] = tmp;
 		}
 	}
 }
    