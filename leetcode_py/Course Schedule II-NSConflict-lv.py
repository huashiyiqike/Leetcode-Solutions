from collections import defaultdict


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        course = defaultdict(set)
        neighbor = defaultdict(set)
        for i, pre in prerequisites:
            course[i].add(pre)
            neighbor[pre].add(i)
        stack = [n for n in range(numCourses) if not course[n]]
        res = []
        while stack:
            pre = stack.pop()
            res.append(pre)
            for i in neighbor[pre]:
                course[i].remove(pre)
                if not course[i]:
                    stack.append(i)
        return res if len(res) == numCourses else []



class course:
    def __init__(self, num):
        self.num = num
        self.lists = []
        self.indim = 0


class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        courses = [course(i) for i in range(numCourses)]
        for i in prerequisites:
            for j in i[1:]:
                courses[j].lists.append(i[0])
                courses[i[0]].indim += 1

        res, queue = [], []
        for i in courses:
            if i.indim == 0:
                queue.append(i)

        while len(queue) > 0:
            for i in queue[0].lists:
                courses[i].indim -= 1
                if courses[i].indim == 0:
                    queue.append(courses[i])

            res.append(queue[0].num)
            del queue[0]

        return res if len(res) == numCourses else []


if __name__ == "__main__":
    a = Solution()
    print a.findOrder(4, [[0, 1], [3, 1], [1, 3], [3, 2]])
