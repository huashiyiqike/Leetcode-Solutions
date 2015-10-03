class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s1.append(x)

    # @return nothing
    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        self.s2.pop()

    # @return an integer
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    # @return an boolean
    def empty(self):
        return len(self.s1) + len(self.s2) == 0

if __name__ == "__main__":
    a = Queue()
    a.push(1)
    a.pop()
    print a.empty()