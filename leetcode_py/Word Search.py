class Solution:
    def f(self, pos, target, board, i, j, visited):
        if pos >= len(target) or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited:
            return False
        if board[i][j] == target[pos]:
            if pos == len(target)-1:
                return True
            else:
                visited.add((i, j))
                if self.f(pos+1, target, board, i+1, j, visited) | \
                        self.f(pos+1, target, board, i-1, j, visited) | \
                        self.f(pos+1, target, board, i, j+1, visited) | \
                        self.f(pos+1, target, board, i, j-1, visited):
                    return True
                visited.remove((i, j))
        return False
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.f(0, word, board, i, j, set([])):
                    return True
        return False

class Solution:        
    def f(self,board,word,i,j,visited,pos=0):
        if len(word)==pos:
            return True
        if  i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited.get((i,j)) or word[pos]!=board[i][j]:
            return False

        visited[(i,j)]=True
       
        res=self.f(board,word,i,j+1,visited,pos+1)\
            or self.f(board,word,i ,j-1,visited,pos+1)\ # or is better than |, once True short circuit
            or self.f(board,word,i+1,j ,visited,pos+1)\
            or self.f(board,word,i-1,j,visited,pos+1)
        visited[(i,j)]=False
        return res
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited={}
 
        for i in range(len(board)):
            for j in range(len(board[0])):
                #print i,j
                if self.f(board,word,i,j,visited):
                    return True
                 
        return False

if __name__=="__main__":
    a=Solution()
    
    print a.exist(["aaaa","aaaa","aaaa"], "aaaaaaaaaaab")
    print a.exist(["b","a"],"ca")