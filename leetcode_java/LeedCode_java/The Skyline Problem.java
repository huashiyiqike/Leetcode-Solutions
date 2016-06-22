/*
A   city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
*/

public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> list=new ArrayList<int[]>();
        if( buildings == null || buildings.length == 0 ){
            return list;
        }
        List<int[]> height=new ArrayList<int[]>();
        int len=buildings.length;
        
        for(int i = 0 ; i < len ; i++){
            height.add(new int[]{buildings[i][0] , -buildings[i][2]});
            height.add(new int[]{buildings[i][1] , buildings[i][2]});
        }
        
        Collections.sort(height , new Comparator<int[]>(){  
            @Override  
            public int compare(int[] a , int[] b) {  
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
               pre=cur;
           }
       }
       return list;
    }
}