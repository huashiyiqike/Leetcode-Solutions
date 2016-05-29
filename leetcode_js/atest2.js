/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    if(nums1.length > nums2.length){
        var tmp = nums2;
        nums2 = nums1;
        nums1 = tmp;
    }
    if((nums1.length + nums2.length) % 2 == 0){
        return (findKth(nums1, nums2, Math.floor( (nums1.length + nums2.length) / 2)) +
        findKth(nums1, nums2, Math.floor( (nums1.length + nums2.length) / 2)+1))  / 2;
    }else{
        return findKth(nums1, nums2, Math.floor( (nums1.length + nums2.length) / 2) + 1);
    }
};

function findKth(A, B, k){
    if(A.length == 0){
        return B[k-1];
    }else if(B.length == 0){
        return A[k-1];
    }else if(k <= 1){
        return Math.min(A[0], B[0]);
    }
    small_a = Math.min(A.length, Math.floor(k/2));
    small_b = k - small_a;
    if(A[small_a - 1] < B[small_b - 1]){
        return findKth(A.slice(small_a - 1), B, k - small_a);
    }else if(A[small_a - 1] > B[small_b - 1]){
        return findKth(A, B.slice(small_b - 1), k - small_b);
    }else{
        return A[small_a - 1];
    }
}
/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/
var m  = findMedianSortedArrays([1,2],[1,2]);
console.log(m);
