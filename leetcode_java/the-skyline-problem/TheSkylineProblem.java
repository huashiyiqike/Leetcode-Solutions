public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> list = new ArrayList<int[]>();
        if(buildings == null || buildings.length == 0){
            return list;
        }
        List<int[]> height = new ArrayList<int[]>();
        int len = buildings.length;
        
        for(int i = 0;i < len ; i++){
            height.add(new int[]{buildings[i][0],-buildings[i][2]});
            height.add(new int[]{buildings[i][1],buildings[i][2]});
        }
        
        Collections.sort(height,new Comparator<int[]>(){  
            @Override  
            public int compare(int[] a, int[] b) {  
                if(a[0] == b[0]){
                    return a[1] - b[1];
                }
                return a[0] - b[0];
            }  
       });
       Queue<Integer> queue = new PriorityQueue<>((a, b) -> (b - a));
       queue.offer(0);
       int pre = 0;
       int heightSize = height.size();
       for(int hei[] : height ){
           if(hei[1] < 0){
               queue.offer(-hei[1]);
           }else{
               queue.remove(hei[1]);
           }
           int cur = queue.peek();
           if(pre != cur){
               list.add(new int[]{hei[0],cur});
               pre = cur;
           }
       }
       return list;
    }
}