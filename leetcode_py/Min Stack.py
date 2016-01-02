class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stacks = []

    def push(self, x):
        if len(self.stacks) == 0:
            self.stacks.append(x)
            self.stacks.append(x)
        else:
            self.stacks.append(min(self.stacks[-2], x))
            self.stacks.append(x)

    # @return nothing
    def pop(self):
        self.stacks.pop()
        self.stacks.pop()

    # @return an integer
    def top(self):
        if len(self.stacks) > 0:
            return self.stacks[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        if len(self.stacks) > 0:
            return self.stacks[-2]
        else:
            return None


import sys
# class MinStack:
#     # @param x, an integer
#     # @return an integer
#     list=[]
#     min=sys.maxint
#     def push(self, x):
#         if self.min>=x:
#             self.list.append(self.min)
#             self.min=x
#         self.list.append(x)
#         return x
#
#
#     # @return nothing
#     def pop(self):
#         tmp=self.top()
#         if tmp!=None:
#             if tmp==self.min:
#                 self.list.pop()
#                 self.min=self.top()
#                 self.list.pop()
#             else:
#                 self.list.pop()
#
#
#
#
#     # @return an integer
#     def top(self):
#         return None if len(self.list)==0 else  self.list[-1]
#
#
#     # @return an integer
#     def getMin(self):
#         return None if len(self.list)==0 else  self.min

if __name__ == '__main__':
    b = MinStack()
    b.push(-1)
    print b.top()
    print b.getMin()
    a = MinStack()
    a.push(0)
    a.push(1)
    a.push(0)
    print a.getMin()
    a.pop()
    print a.getMin()

    print a.getMin()
    while a.top() != None:
        print a.top()
        a.pop()
