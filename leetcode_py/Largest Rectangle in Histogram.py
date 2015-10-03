class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                size = max(size, h*w)
            stack.append(i)
        return size

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        stack = [0]
        res = 0
        for idx, item in enumerate(height[1:], start=1):
            if not stack or height[stack[-1]] < item:
                stack.append(idx)
            else:
                while stack and height[stack[-1]] > item:
                    left = stack.pop()
                    if stack:
                        res = max(res, (idx - 1 - stack[-1]) * height[left])
                    else:
                        res = max(res, idx * height[left])
                stack.append(idx)
        while stack:
            left = stack.pop()
            if stack:
                res = max(res, (len(height) - 1 - stack[-1]) * height[left])
            else:
                res = max(res, len(height) * height[left])
        return res

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if len(height)==0:
            return 0
        stack=[0]
        res=0
        i=1
        while i<len(height):
            # print i, stack
            if len(stack)==0 or (len(stack)>0  and height[stack[-1]]<height[i]) :
                stack.append(i)
                i+=1
            else:
                left=stack.pop()
                val=height[left]
                if len(stack)>0:
                    res=max(res,val*(i-stack[-1]-1))
                else:
                    res=max(res,val*i)

        while len(stack)>0:
            left=stack.pop()
            val=height[left]
            if len(stack)>0:
                res=max(res,val*(len(height)-stack[-1]-1))
            else:
                res=max(res,val*(len(height)))
        return res
