class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        list=[1,2]
        for i in range(2,n+1):
            list.append(list[i-1]+list[i-2])
        return list[n-1]