<backquote><pre>
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
</backquote></pre>

There are at least two ways to solve it.
1. DFS
We use a flag array to tag the numbers that have been traversed, so we can iterate the array with dfs.
2. find the pattern.
Use the idea similar to the next permutation.