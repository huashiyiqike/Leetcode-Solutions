class Minheap{
    int[] data;
    int size = 0;
    Minheap(int size){data = new int[size];}
    int parent(int i){return (i-1)/2;}
    int left_child(int i){return i*2+1;}
    int right_child(int i){return i*2+2;}
    void add(int num){
        int i = size;
        size++;
        data[i] = num;
        while(i > 0 && data[i] < data[parent(i)]){
            int tmp = data[parent(i)];
            data[parent(i)] = data[i];
            data[i] = tmp;
            i = parent(i);
        }
    }
    void heapify(int i){
        int min = i;
        int l = left_child(i), r = right_child(i);
        if(l < size && data[l] < data[min]) min = l;
        if(r < size && data[r] < data[min]) min = r;
        if(min != i){
            int tmp = data[i];
            data[i] = data[min];
            data[min] = tmp;
            heapify(min);
        }
    }
}

public class Solution {
    public int findKthLargest(int[] nums, int k) {
        Minheap a = new Minheap(k);
        for(int i = 0; i < k; i++)  a.add(nums[i]);
        for(int i = k; i < nums.length; i++){
            if(a.data[0] < nums[i]){
                a.data[0] = nums[i];
                a.heapify(0);
            }
        }
        return a.data[0];
    }
}




public class Solution {
    
    static class MinHeap {
        
        int[] data;
        
        int currentSize = 0;
        
        MinHeap(int size){
            data = new int[size];    
        }
        
        int parent(int i){
            return (i - 1) / 2;
        }
        
        int left(int i){
            return 2 * i + 1;
        }
        
        int right(int i){
            return 2 * i + 2;
        }

        void add(int n){
            int i = currentSize;
            currentSize++;
            
            data[i] = n;
            
            while(i > 0 && data[parent(i)] > data[i]){
                swap(parent(i), i);
                i = parent(i);
            }
        }        
        
        void heapify(int i){
            
            int l   = left(i);
            int r   = right(i);
            int min = i;
            
            if(l < currentSize && data[l] < data[min]){
                min = l;
            }
            
            if(r < currentSize && data[r] < data[min]){
                min = r;
            }
            
            if(min != i){
                swap(i, min);
                heapify(min);
            }
            
        }
        
        void swap(int x, int y){
            int t   = data[x];
            data[x] = data[y];
            data[y] = t;
        }
    }
    
    public int findKthLargest(int[] nums, int k) {
        
        MinHeap heap = new MinHeap(k);
        
        for(int i = 0; i < Math.min(nums.length, k); i++){
            heap.add(nums[i]);    
        }
        
        for(int i = k; i < nums.length; i++){
            
            if(heap.data[0] < nums[i]){
                heap.data[0] = nums[i];
                heap.heapify(0);
            }
        }
        
        return heap.data[0];
    }
}
