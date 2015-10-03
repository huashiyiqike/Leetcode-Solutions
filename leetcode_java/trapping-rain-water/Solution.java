public class Solution {
    public int trap(int[] height) {
        int maxs = -1, idx = -1;
        for(int i = 0; i < height.length; i++){
            if(height[i] > maxs){
                maxs = height[i];
                idx = i;
            }
        }
        int res = 0, leftmax = -1, rightmax = -1;
        for(int i = 0; i < idx; i++){
            if(height[i] > leftmax){
                leftmax = height[i];
            }
            else{
                res += leftmax - height[i];
            }
        }
        for(int i = height.length - 1;i > idx; i--){
            if(height[i] > rightmax){
                rightmax = height[i];
            }
            else{
                res += rightmax - height[i];
            }
        }
        return res;
    }
}

public class Solution {
    
    static class Bar{
        int pos;
        int height;
        
        Bar(int pos, int height){
            this.pos = pos;
            this.height = height;
        }
    }
    
    int containWater(Deque<Bar> queue){
        
        Bar left  = queue.peekFirst();
        Bar right = queue.peekLast();
        
        int water = 0;
        
        if(right.height >= left.height){
        
            water += Math.min(right.height, left.height) * (right.pos - left.pos - 1);
            
            queue.removeFirst(); // remove left
            
            // remove stones
            while(queue.size() > 1){
                water -= queue.removeFirst().height;
            }
        }
        
        return water;
    }
    
    int[] reverseAndToInt(Deque<Bar> queue){
        int[] a = new int[queue.size()];
        int i = 0;

        while(!queue.isEmpty()){
            a[i++] = queue.removeLast().height;

        }

        return a;
    }
    
    public int trap(int[] A) {
        
        if (A.length <= 2) return 0;
        
        Deque<Bar> queue = new LinkedList<Bar>();
        
        int s = 0;
        while(s < A.length && A[s] == 0) s++;
        
        if(s < A.length)
            queue.add(new Bar(s, A[s]));
        
        int water = 0;
        
        for(int i = s + 1; i < A.length; i++){
            
            queue.add(new Bar(i, A[i]));
            
            water += containWater(queue);
        }
        
        water += trap(reverseAndToInt(queue));
        
        return water;
    }
}
