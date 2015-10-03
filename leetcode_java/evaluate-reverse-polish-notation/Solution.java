public class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new LinkedList<>();
        for(int i = 0; i < tokens.length; i++){
            if(tokens[i].equals("-")){
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a-b);
            }else if(tokens[i].equals("+")){
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a+b);
            }else if(tokens[i].equals("*")){
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a*b);
            }else if(tokens[i].equals("/")){
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a/b);
            }else{
                stack.push(Integer.valueOf(tokens[i])); // parseInt TLE
            }
        }
        return stack.pop();
    }
}

public class Solution {
    public int evalRPN(String[] tokens) {
        
        final Deque<Integer> stack = new LinkedList<Integer>();
        
        for(String t : tokens){
            if("+".equals(t)){
                Integer v2 = stack.pop();
                Integer v1 = stack.pop();
                
                stack.push(v1 + v2);
            }else if("-".equals(t)){
                Integer v2 = stack.pop();
                Integer v1 = stack.pop();
                
                stack.push(v1 - v2);
            }else if("*".equals(t)){
                Integer v2 = stack.pop();
                Integer v1 = stack.pop();
                
                stack.push(v1 * v2);
            }else if("/".equals(t)){
                Integer v2 = stack.pop();
                Integer v1 = stack.pop();
                
                stack.push(v1 / v2);
            }else{
                stack.push(Integer.valueOf(t));
            }
        }
        
        return stack.pop();
        
    }
}
