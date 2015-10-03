class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxs=0
        for idx,item in enumerate(A):
            if maxs<idx:
                return False
            maxs=max(maxs,idx+item)
            if maxs>=len(A)-1:
                return True


class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A)==0:
            return True
        ref=[0 for i in A]
        ref[0]=1
        maxs=0
        for idx,item in enumerate(A):
            if ref[idx]==1 and idx+item>maxs:
                for i in range(maxs+1,idx+item+1):
                    if i<len(ref):
                        ref[i]=1
                maxs=idx+item
                
        return ref[-1]==1



public boolean canJump(int[] A) {
    int max = 0;
for(int i=0;i<A.length;i++){
if(i>max) {return false;}
max = Math.max(A[i]+i,max);
}
return true;
}