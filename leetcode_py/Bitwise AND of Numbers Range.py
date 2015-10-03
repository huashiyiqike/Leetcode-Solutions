# int rangeBitwiseAnd(int m, int n) {
#     int c=0;
#     while(m!=n){
#         m>>=1;
#         n>>=1;
#         ++c;
#     }
#     return n<<c;
# }
#
#public class Solution {
# public int maxbit(int n){
#     int tmp = n, count = 0;
# while(tmp > 0){
# tmp>>=1;
# count++;
# }
# return count;
# }
# public int rangeBitwiseAnd(int m, int n) {
# if(maxbit(m) != maxbit(n)) return 0;
# int res = 0, count = maxbit(m)-1;
# while(count >= 0 && (m & (1 << count)) == (n & (1 << count))){
# res |= (m & 1<<count);
# count--;
# }
# return res;
# }
# }
# the result of a range bitwise is the common 'left header' of m and n.

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        k=max(m,n)
        count=0
        while k:
            k/=2
            count+=1

        res=0
        started =False
        while count>-1:
            tmp=1<<count
            if m&tmp != n&tmp:
                if started:
                    return res
            else:
                started=True
                if m&tmp:
                    res+=tmp
            count-=1
        return res
#https://leetcode.com/discuss/34720/my-accepted-and-simple-python-code
    def rangeBitwiseAnd(self, m, n):
        d=n-m
        if d==0:
            return m
        p=0
        while d:
            p+=1
            d>>=1
        return (m&n)& (-1<<p)  #((m&n)>>p)<<p

if __name__=="__main__":
    a=Solution()
    print a.rangeBitwiseAnd(5,7)
    print a.rangeBitwiseAnd(1,1)