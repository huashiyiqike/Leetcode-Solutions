/*
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
*/

public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
         if(matrix==null||matrix.length==0){
			 return 0;
		 }
		 int xLen=matrix.length;
		 int yLen=matrix[0].length;
		 int i,j;
		 int[][] lenArr=new int[xLen][yLen];
		 int max=0;
		
		 for(i=0;i<xLen;i++){
			 for(j=0;j<yLen;j++){
					dfs(matrix,i,j,xLen-1,yLen-1,lenArr); 
					max=Math.max(max,lenArr[i][j]);
				}
				
		
		 }
		// System.out.println(result.size());
		return max;
		
    }
    private  void  dfs(int[][] matrix, int i, int j,int xLen,int yLen,int[][] lenArr) {
		// TODO Auto-generated method stub
		if(i<0||j<0||i>xLen||j>yLen){
			return ;
		}
	      lenArr[i][j]=1;
		if(j>0&&matrix[i][j]<matrix[i][j-1]){
		     if(lenArr[i][j-1]==0){
				dfs(matrix,i,j-1,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j]=Math.max(lenArr[i][j],lenArr[i][j-1]+1);
		}
		if(i>0&&matrix[i][j]<matrix[i-1][j]){
			
			if(lenArr[i-1][j]==0){
				dfs(matrix,i-1,j,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j]=Math.max(lenArr[i][j],lenArr[i-1][j]+1);
		}
		if(j<yLen&&matrix[i][j]<matrix[i][j+1]){
		
				if(lenArr[i][j+1]==0){
				dfs(matrix,i,j+1,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j]=Math.max(lenArr[i][j],lenArr[i][j+1]+1);
		}
		if(i<xLen&&matrix[i][j]<matrix[i+1][j]){
		
			if(lenArr[i+1][j]==0){
				dfs(matrix,i+1,j,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j]=Math.max(lenArr[i][j],lenArr[i+1][j]+1);
			
			
	
	   }
	
	}
}