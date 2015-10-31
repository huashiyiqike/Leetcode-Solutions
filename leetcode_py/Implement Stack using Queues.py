class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)

    # @return nothing
    # remove the tail
    def pop(self):
        lens = len(self.q1)
        for i in range(lens - 1):
            tmp = self.q1.pop(0)
            self.q1.append(tmp)
        self.q1.pop(0)

    # @return an integer
    # get the tail of the queue
    def top(self):
        lens = len(self.q1)
        for i in range(lens):
            tmp = self.q1.pop(0)
            self.q1.append(tmp)
        return tmp

    # @return an boolean
    def empty(self):
        if self.q1:
            return False
        return True


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)

    # @return nothing
    def pop(self):
        while self.q1:
            tmp = self.q1.pop(0)
            if self.q1:
                self.q2.append(tmp)
        self.q1 = self.q2
        self.q2 = []

    # @return an integer
    def top(self):
        while self.q1:
            tmp = self.q1.pop(0)
            self.q2.append(tmp)
        self.q1 = self.q2
        self.q2 = []
        return tmp

    # @return an boolean
    def empty(self):
        if self.q1:
            return False
        return True
