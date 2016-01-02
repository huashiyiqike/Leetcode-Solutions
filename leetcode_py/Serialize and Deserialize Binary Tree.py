class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = [root]
        res = ""
        while q:
            nextq = []
            while q:
                tmpnode = q.pop()
                count = 0
                if tmpnode.left: count += 1
                if tmpnode.right: count += 1

                res += str(count)
                if tmpnode.left:
                    res += "#" + str(tmpnode.left.val)
                    nextq.append(tmpnode.left)
                if tmpnode.right:
                    res += "#" + str(tmpnode.right.val)
                    nextq.append(tmpnode.right)

            q = nextq
        return res


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        datas = map(int, data.split("#"))
        root = TreeNode(datas[0])
        idx = 1
        q = [root]
        while idx < len(datas):
            for node in q:
                if datas[idx] != 0:
                    #for i in range(datas[idx]):
                    if datas[idx] == 1:




        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))