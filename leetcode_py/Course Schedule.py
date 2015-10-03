class Node:
    def __init__(self):
        self.neighbor = []
        self.into = 0
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        courses = [Node() for i in range(numCourses)]
        for i in prerequisites:
            for j in i[1:]:
                courses[j].neighbor.append(i[0])
                courses[i[0]].into += 1
        res = []
        queue = []
        for i in courses:
            if i.into == 0:
                queue.append(i)

        while queue:
            tmp = queue.pop(0)
            for i in tmp.neighbor:
                courses[i].into -= 1
                if courses[i].into == 0:
                    queue.append(courses[i])
            res.append(tmp)
        return len(res) == numCourses

class course:
    def __init__(self):
        self.lists=[]
        self.indim=0
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        courses=[course() for i in range(numCourses)]
        for i in prerequisites:
            for j in i[1:]:
                courses[j].lists.append(i[0])
                courses[i[0]].indim+=1
                
        res=[]
        queue=[]
        for i in courses:
            if  i.indim==0:
                queue.append(i)
                
        while len(queue)>0:
            for i in queue[0].lists:
                courses[i].indim-=1
                if courses[i].indim==0:
                    queue.append(courses[i])
                    
            res.append(queue[0])
            del queue[0]
        return len(res)==numCourses
                
if __name__=="__main__":
    a=Solution()
    print a.canFinish(    4, [[0,1],[3,1],[1,3],[3,2]] )              