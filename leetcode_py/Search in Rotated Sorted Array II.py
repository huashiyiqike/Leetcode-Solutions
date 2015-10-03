class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if target == nums[mid]:
                return True
            if nums[mid] <= nums[r]: # notice =
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r -= 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l += 1
        return False

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A)==0 or (len(A)==1 and A[0]!=target):
            return False
        low,high=0,len(A)-1
        while low+1<len(A)-1 and A[low]==A[low+1]:
            low+=1
        while high>0 and A[high]==A[high-1]:
            high-=1
        while low<high and A[low]==A[high]:
            low+=1
            
        while low<high:
            mid=(high+low)>>1
            if  (A[low] <= A[mid] and target < A[mid] and target >= A[low]) or \
            (A[mid] <= A[high] and (target < A[mid] or target > A[high])):
                high=mid-1
            elif A[mid] == target:
                return True
            else:
                low+=1
        if A[low]==target:
            return True
        return False
#     
#    https://leetcode.com/discuss/223/when-there-are-duplicates-the-worst-case-is-could-we-do-better
#     bool search(int A[], int n, int key) {
#     int l = 0, r = n - 1;
#     while (l <= r) {
#         int m = l + (r - l)/2;
#         if (A[m] == key) return true; //return m in Search in Rotated Array I
#         if (A[l] < A[m]) { //left half is sorted
#             if (A[l] <= key && key < A[m])
#                 r = m - 1;
#             else
#                 l = m + 1;
#         } else if (A[l] > A[m]) { //right half is sorted
#             if (A[m] < key && key <= A[r])
#                 l = m + 1;
#             else
#                 r = m - 1;
#         } else l++;
#     }
#     return false;
# }

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A)==0:
            return -1
        l,r=0,len(A)-1
        while l<=r:
            mid=(l+r)/2
            if target==A[mid]:
                return True
            if A[mid]<A[r]:
                if A[mid]<target<=A[r]:
                    l=mid+1
                else:
                    r=mid-1
            elif A[mid]>A[r]:
                if A[l]<=target<A[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                r-=1 # cannot use l+=1
        return False

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A)==0 or (len(A)==1 and A[0]!=target):
            return False
        low,high=0,len(A)-1
        while low+1<len(A)-1 and A[low]==A[low+1]:
            low+=1
        while high>0 and A[high]==A[high-1]:
            high-=1
        while low<high and A[low]==A[high]:
            low+=1

        while low<high:
            mid=(high+low)>>1
            if  (A[low] <= A[mid] and target < A[mid] and target >= A[low]) or \
                    (A[mid] <= A[high] and (target < A[mid] or target > A[high])):
                high=mid-1
            elif A[mid] == target:
                return True
            else:
                low+=1
        if A[low]==target:
            return True
        return False