# Definition for a undirected graph node
import new


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# depth first
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        start = UndirectedGraphNode(node.label)
        stack = [node]
        dicts = {node: start}
        while stack:
            current = stack.pop()
            for i in current.neighbors:
                if i not in dicts:
                    new = UndirectedGraphNode(i.label)
                    dicts[i] = new
                    stack.append(i)
                dicts[current].neighbors.append(dicts[i])
        return start

# breadth first
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        start = UndirectedGraphNode(node.label)
        dicts, current = {node: start}, [node]
        while current:
            next = []
            for i in current:
                for j in i.neighbors:
                    if j not in dicts:
                        new = UndirectedGraphNode(j.label)
                        next.append(j)
                        dicts[j] = new
                    dicts[i].neighbors.append(dicts[j])

            current = next
        return start


# recursive breadth first
class Solution:
    def deepcopy(self, node):
        if node.label in self.hash.keys():
            return self.hash[node.label]
        else:
            newnode = UndirectedGraphNode(node.label)
            self.hash[node.label] = newnode
            for i in node.neighbors:
                newnode.neighbors.append(self.deepcopy(i))
            return newnode

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.hash = {}
        if node:
            return self.deepcopy(node)
        else:
            return None
