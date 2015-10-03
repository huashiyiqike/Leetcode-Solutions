from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.end = False

class Solution:
    def finds(self, board, res, path, i, j, node):
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
            return

        if node.end:
            res.append(path)
            node.end = False  # no repeat word add to res

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for d in dir:
            inew = i + d[0]
            jnew = j + d[1]
            if 0 <= inew < len(board) and 0 <= jnew < len(board[0]) and \
                    not self.flag[inew][jnew] and board[inew][jnew] in node.child:
                self.flag[inew][jnew] = True
                self.finds(board, res, path+board[inew][jnew], inew, jnew, node.child[board[inew][jnew]])
                self.flag[inew][jnew] = False

    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        self.root = TrieNode()
        self.flag =[[False]*len(board[0]) for i in range(len(board))]

        def insert(word):
            cur = self.root
            for i in word:
                cur = cur.child[i]
            cur.end = True
        for i in words:
            insert(i)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.root.child:
                    self.flag[i][j] = True
                    self.finds(board, res, board[i][j], i, j, self.root.child[board[i][j]])
                    self.flag[i][j] = False
        return res


if __name__=="__main__":
    a=Solution()
    print a.findWords(["bbaaba","bbabaa","bbbbbb","aaabaa","abaabb"], ["abbbababaa"])
    print a.findWords(["aaaa","aaaa","aaaa"], ['aaa','ba',"aaaaaaaaaaab",'aa'])
    print a.findWords(["b","a"],["ca",'a'])

#https://leetcode.com/discuss/36401/python-ac-solution
# class TrieNode:
# def __init__(self):
#     self.children = collections.defaultdict(TrieNode)
#     self.flag = False
# 
# class Solution:
# def __init__(self):
#     self.root = TrieNode()
#     self.result = []
# 
# def insert(self, word):
#     node = self.root
#     for letter in word:
#         node = node.children[letter]
#     node.flag = True
# 
# def findWords(self, board, words):
#     for w in words:
#         self.insert(w)
#     for j in range(len(board)):
#         for i in range(len(board[0])):
#             self.dfs(self.root, board, j, i)
#     return self.result
# 
# def dfs(self, node, board, j, i, word=''):
#     if node.flag:
#         self.result.append(word)
#         node.flag = False
#     if 0 <= j < len(board) and 0 <= i < len(board[0]):
#         char = board[j][i]
#         child = node.children.get(char)
#         if child is not None:
#             word += char
#             board[j][i] = None
#             self.dfs(child, board, j + 1, i, word)
#             self.dfs(child, board, j - 1, i, word)
#             self.dfs(child, board, j, i + 1, word)
#             self.dfs(child, board, j, i - 1, word)
#             board[j][i] = char
#             
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.end=False
        self.child=defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current=self.root 
        for i in word:
            current=current.child[i]
        current.end=True
    def search(self, word):
        current=self.root 
        for i in word:
            current=current.child.get(i)
            if current is None:
                return False
        return current.end

    def startsWith(self, prefix):
        current=self.root 
        for i in prefix:
            current=current.child.get(i)
            if current is None:
                return False
        return True
    
class Solution:
    def f(self,board,word,i,j,visited,current,now,pos=0): 
        if current.end:
            self.res.add(now)
         #   return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited.get((i,j)):
            return False
        current=current.child.get(board[i][j])
        if current !=None:
            visited[(i,j)]=True
            now+=board[i][j]
            res=self.f(board,word,i,j+1,visited,current,now,pos+1)\
            |self.f(board,word,i ,j-1,visited,current,now,pos+1)\
            |self.f(board,word,i+1,j ,visited,current,now,pos+1)\
            |self.f(board,word,i-1,j,visited,current,now,pos+1)
            visited[(i,j)]=False
            return res
        else:
            return False

    def findWords(self, board, words):
        self.trie=Trie()
        for i in words:
            self.trie.insert(i)
        visited={}
        self.res=set([])
        for i in range(len(board)):
            for j in range(len(board[0])):
              #  print i,j,board[i][j]
                self.f(board,words,i,j,visited,self.trie.root,'')
        return list(self.res)
    
if __name__=="__main__":
    a=Solution()
    print a.findWords(["bbaaba","bbabaa","bbbbbb","aaabaa","abaabb"], ["abbbababaa"])
    print a.findWords(["aaaa","aaaa","aaaa"], ['aaa','ba',"aaaaaaaaaaab",'aa'])
    print a.findWords(["b","a"],["ca",'a']) 