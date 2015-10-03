class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left,right=0,len(height)-1
        res=0
        while left<right:
            res=max(res,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res





class Solution:
    # @param height, an integer[]
    # @return an integer
    def maxArea(self, height):
        maxs=0
        left=0
        right=len(height)-1
        while left<right:
            maxs=max(maxs,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxs