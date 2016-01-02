class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        current, res = [root], []
        while current:
            next = []
            tmpres = []
            for i in current:
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
                tmpres.append(i.val)
            res.append(tmpres)
            current = next
        return res


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            count = len(queue)
            tmp = []
            for i in range(count):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                tmp.append(queue.pop(0).val)
            res.append(tmp)

        return res
