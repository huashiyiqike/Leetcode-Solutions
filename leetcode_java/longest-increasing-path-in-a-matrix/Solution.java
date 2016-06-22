public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
         if(matrix == null || matrix.length == 0){
			 return 0;
		 }
		 int xLen = matrix.length;
		 int yLen = matrix[0].length;
		 int i,j;
		 int[][] lenArr = new int[xLen][yLen];
		 int max=0;
		
		 for(i = 0;i < xLen;i++){
			 for(j = 0;j < yLen;j++){
					dfs(matrix,i,j,xLen-1,yLen-1,lenArr); 
					max = Math.max(max,lenArr[i][j]);
				}
				
		
		 }
		// System.out.println(result.size());
		return max;
		
    }
    private  void  dfs(int[][] matrix, int i, int j,int xLen,int yLen,int[][] lenArr) {
		// TODO Auto-generated method stub
		if(i < 0 || j < 0 || i > xLen || j > yLen){
			return ;
		}
	      lenArr[i][j] = 1;
		if(j > 0 && matrix[i][j] < matrix[i][j-1]){
		     if(lenArr[i][j-1] == 0){
				dfs(matrix,i,j-1,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j] = Math.max(lenArr[i][j],lenArr[i][j-1] + 1);
		}
		if(i > 0 && matrix[i][j] < matrix[i-1][j]){
			
			if(lenArr[i-1][j] == 0){
				dfs(matrix,i-1,j,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j] = Math.max(lenArr[i][j],lenArr[i-1][j]+1);
		}
		if(j < yLen && matrix[i][j] < matrix[i][j+1]){
		
				if(lenArr[i][j+1] == 0){
				dfs(matrix,i,j+1,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j] = Math.max(lenArr[i][j],lenArr[i][j+1]+1);
		}
		if(i < xLen && matrix[i][j] < matrix[i+1][j]){
		
			if(lenArr[i+1][j] == 0){
				dfs(matrix,i+1,j,xLen,yLen,lenArr); 
		     }
		     lenArr[i][j] = Math.max(lenArr[i][j],lenArr[i+1][j]+1);
			
			
	
	   }
	
	}
}