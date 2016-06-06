public class NumArray {
   int[] tree;
   int[] copyArr;
   int n;
    public NumArray(int[] nums) {
        n = nums.length;
        copyArr = Arrays.copyOf(nums, n);
        tree = new int[n+1];
        for(int i = 0;i < n;i++){
            updateTree(i+1,nums[i]);
        }
    }
     void updateTree(int j,int val){
         while(j<=n){
             tree[j] += val;
             j+=j&-j;
         }
          
     }
    void update(int j, int val) {
        int diff = val-copyArr[j];
        copyArr[j] = val;
        updateTree(j+1,diff);
        
    }
   int getSum(int j) {
       int sum = 0;
       while(j>0){
           sum += tree[j];
           j-=j&(-j);
       }
       return sum;
   }
    public int sumRange(int i, int j) {
        return getSum(j+1)-getSum(i);
    }
}
