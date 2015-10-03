class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count=0
        while n:
            if n&1:
                count+=1
            n>>=1
        return count

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count=0
        for i in range(64):
            if n & (1 <<i):
                count+=1
        return count
        

class Solution {
    public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n != 0) {
            count++;
            n &= (n - 1);
        }
    
        return count;
    }
};