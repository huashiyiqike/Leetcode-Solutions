/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    nums1.sort(function(a,b){return a-b;});
    nums2.sort(function(a,b){return a-b;});
    var p1 = p2 = 0, res = [];
    while(p1 < nums1.length && p2 < nums2.length){
    	if(nums1[p1] < nums2[p2]){
    		p1++;
    	}else if(nums1[p1] > nums2[p2]){
    		p2++;
    	}else{
    		res.push(nums1[p1]);
    		while(p1+1 < nums1.length && nums1[p1+1] == nums1[p1]){
    			p1++;
    		}
    		p1++;
    		while(p2+1 < nums2.length && nums2[p2+1] == nums2[p2]){
    			p2++;
    		}
    		p2++;
    	}
    }
    return res;
};