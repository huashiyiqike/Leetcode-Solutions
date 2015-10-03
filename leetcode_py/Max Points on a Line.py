# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
from collections import defaultdict
class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if not points:
            return 0

        res = 1
        for i in range(len(points)-1):
            vertical = 1
            same = 0
            dict = defaultdict(int)
            for j in range(i+1, len(points)):
                if points[j].x == points[i].x:
                    vertical += 1
                    if points[j].y == points[i].y:
                        same += 1
                else:
                    lope = (points[j].y - points[i].y) / float(points[j].x - points[i].x)
                    cross = points[i].y - points[i].x*(points[j].y - points[i].y)\
                        / float(points[j].x - points[i].x)
                    dict[(lope, cross)] += 1

            res = max(res, (vertical if vertical > 1 else 0),\
                      same + 1 + (max(dict.values()) if dict.values() else 0))

        return res

if __name__=="__main__":
    a=Solution()
    #  print a.maxPoints([Point(0,0),Point(1,0)])
    print a.maxPoints([Point(0,0),Point(1,1),Point(0,0)])
    print a.maxPoints([Point(0,0),Point(0,0)])
    print a.maxPoints([Point(1,1),Point(2,2), Point(1,0), Point(2,1)])
    print a.maxPoints([Point(-1, -1), Point(0,0), Point(2,2)])

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution():
    def maxPoints(self, points):
        res=0
        for i in range(len(points)):
            tmpres,dicts,same,inf=0,{},1,0
            for j in range(i+1,len(points)):
                if points[i].x==points[j].x and points[i].y==points[j].y:
                    same+=1
                elif points[i].x==points[j].x:
                    inf+=1
                else:
                    slop=1.0*(points[j].y-points[i].y)/(points[j].x-points[i].x)
                    if slop not in dicts:
                        dicts[slop]=1
                    else:
                        dicts[slop]+=1
                for slop in dicts:
                    tmpres=max(tmpres,same+dicts[slop]) 
            res=max(res,tmpres,same+inf)
        return res            
            

# 
# class Solution:
#     # @param {Point[]} points
#     # @return {integer}
#     def maxPoints(self, points):
#         if len(points)==0:
#             return 0
#         res=1
#         dicts={}
#         i=0
#         while i <len(points):
#             if (points[i].x,points[i].y) not in dicts:
#                 dicts[(points[i].x,points[i].y)]=1
#                 i+=1
#             else:
#                 dicts[(points[i].x,points[i].y)]+=1
#                 del points[i]
#                 
#                 
#         for i in range(len(points)):
#             tmpres=dicts[(points[i].x,points[i].y)]
#             res=max(res,tmpres)
#             for j in range(i+1,len(points)):
#                 tmpres=dicts[(points[i].x,points[i].y)]+ dicts[(points[j].x,points[j].y)]
#                 for k in range(j+1,len(points)):
#                     if (points[j].y-points[i].y)*(points[k].x-points[i].x)==(points[j].x-points[i].x)*(points[k].y-points[i].y):
#                         tmpres+=dicts[(points[k].x,points[k].y)]
#                  
#                 res=max(res,tmpres)
#                 
#         return res
    

if __name__=="__main__":
    a=Solution()
  #  print a.maxPoints([Point(0,0),Point(1,0)])
    print a.maxPoints([Point(0,0),Point(1,1),Point(0,0)])
    print a.maxPoints([Point(0,0),Point(0,0)])
    print a.maxPoints([Point(1,1),Point(2,2), Point(1,0), Point(2,1)])