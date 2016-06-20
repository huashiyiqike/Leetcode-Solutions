public class Solution {
    public boolean isValidSerialization(String preorder) {
        if(preorder == null){
            return false;
        }
        String[] arr = preorder.split(",");
        int len = arr.length;
        if(len%2 == 0){
            return false;
        }
       
       
        if(len == 1 && arr[0].equals("#") ){
            return true;
        }
        int node = 0;
        int leaf = 0;
        for(int i = len-1 ;i >= 0 ; i--){
            if(arr[i].equals("#")){
                leaf++;
            }else{
                node++;
            }
            if(leaf-node<1){
                return false;
            }
        }
        return (leaf-node) == 1;
    }
}