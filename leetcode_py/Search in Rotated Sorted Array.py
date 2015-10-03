
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
                return mid
            if A[mid]<A[r]:
                if A[mid]<target<=A[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if A[l]<=target<A[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[r]:
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


#https://leetcode.com/discuss/11701/concise-o-log-n-binary-search-solution


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A)==0 or (len(A)==1 and A[0]!=target):
            return -1
        low,high=0,len(A)-1
        while low<high:
            mid=(high+low)>>1
            if  (A[low] < A[mid] and target < A[mid] and target >= A[low]) or \
            (A[mid] < A[high] and (target < A[mid] or target > A[high])):
                high=mid-1
            elif A[mid] == target:
                return mid
            else:
                low+=1
        if A[low]==target:
            return low
        return -1
            




