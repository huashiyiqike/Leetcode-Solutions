import java.util.*;
public class Solution {
    public String simplifyPath(String path) {
        LinkedList<String> paths = new LinkedList<>(Arrays.asList(path.split("/")));
//        if(!paths.isEmpty()) paths.remove(0);
        LinkedList<String> stack = new LinkedList<>();
        for(String c : paths){
            if(c.equals("..")){
                if(!stack.isEmpty()) stack.pop();
            }
            else if(c.equals("")) continue;
            else if(!c.equals(".")) stack.push(c);
        }
        String res = "";
        for(String c: stack){
            res = "/" + c + res;
        }
        return res.equals("")?"/":res;
    }
}

public class Solution {
    public String simplifyPath(String path) {
        
        String[] names = path.split("/");
        
        int eat = 0;
        
        LinkedList<String> stack = new LinkedList<String>();
        
        for(int i = names.length - 1; i >= 0; i--){
            
            String token = names[i];
            
            if("..".equals(token)){
                eat++;
            }else if(".".equals(token)){
                // do nothing
            }else if("".equals(token)){
                // do nothing
            }else {
                
                // dir name
                if(eat > 0){
                    eat--;
                }else{
                    stack.push(token);
                }
            }
        }
        
        StringBuilder s = new StringBuilder();
        
        s.append("/");
        
        while(stack.size() > 1){
            s.append(stack.pop());
            s.append("/");
        }
        
        if(!stack.isEmpty()) s.append(stack.pop());
        
        return s.toString();
    }
}
