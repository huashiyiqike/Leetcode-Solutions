<blockquote>
<pre>Given an integer matrix, find the length of the longest increasing path.

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
</pre>
</blockquote>

Simply loop through the matrix, DFS and maintain two matrix: one for visited and another for memorization of current longest increasing path(we can combine this two as one of course). In each place we go four directions, if visited we used the previous value and plus 1, else we DFS and return the value. Do not forget to set these two matrix in the end of the DFS. 
Simply loop through the matrix, DFS and maintain one matrix name max for the max size of  current longest increasing path . In each place we go four directions, if max[NewX][NewY]==0 we use DFS count the max[NewX][NewY], max[i][j]=max(max[i][j],max[NewX][NewY]+1),finally we find the max element of max matrix.