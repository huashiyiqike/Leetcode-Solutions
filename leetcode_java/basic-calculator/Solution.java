import java.util.*;

public class Solution {
    public int calculate(String s) {
        s = s.trim();
        Deque<String> stack = new LinkedList<>();
        int i = 0;
        while(i < s.length()){
            if(s.charAt(i) == '+'|| s.charAt(i) == '-' || s.charAt(i) =='('){
                stack.push(String.valueOf(s.charAt(i)));
                i++;
            }else if(s.charAt(i) == ' '){
                i++;
                continue;
            }else if(s.charAt(i) == ')'){
                String num = stack.pop();
                stack.pop();
                stack.push(num);
                i++;
            }else{
                int j = i;
                while(j < s.length() && s.charAt(j) <= '9' && s.charAt(j) >='0'){
                    j++;
                }
                String num = s.substring(i, j);
                stack.push(num);
                i = j;
            }
            String tmp = stack.peek();
            while(stack.size() >= 3 && !tmp.equals("(") && !tmp.equals("+") &&
                    !tmp.equals("-")){
                String num = stack.pop();
                if(tmp.equals("-") || tmp.equals("+")){
                    stack.push(num);
                }else {
                    String op = stack.pop();
                    if (op.equals("+")) {
                        String num1 = stack.pop();
                        String res = String.valueOf(Integer.valueOf(num1) + Integer.valueOf(num));
                        stack.push(res);
                    } else if (op.equals("-")) {
                        String num1 = stack.pop();
                        String res = String.valueOf(Integer.valueOf(num1) - Integer.valueOf(num));
                        stack.push(res);
                    }
                }
            }
        }
        return Integer.valueOf(stack.pop());
    }
}

public class Solution {
    public int calculate(String s) {
        String s1 = s.trim();
    }
}
public class Solution {
    enum TokenType { DIGIT, OP }

    static class Token {
        TokenType type;
        int val;

        public Token(int val, TokenType type) {
            this.val = val;
            this.type = type;
        }
    }

    static final Token EOL = new Token(0, TokenType.OP);

    static final Token[] TOKENS = new Token[256];

    static {
        TOKENS['+'] = new Token('+', TokenType.OP);
        TOKENS['-'] = new Token('-', TokenType.OP);
        TOKENS['*'] = new Token('*', TokenType.OP);
        TOKENS['/'] = new Token('/', TokenType.OP);
        TOKENS['('] = new Token('(', TokenType.OP);
        TOKENS[')'] = new Token(')', TokenType.OP);
    }

    static class Tokenizer {

        Scanner scanner;

        Tokenizer(String s){
            scanner = new Scanner(s);
            scanner.useDelimiter("");
        }

        Token next(){
            if(!scanner.hasNext()){
                return EOL;
            }

            boolean num = false;
            int buf = 0;
            while (scanner.hasNextInt()){
                num = true;
                buf = buf * 10 + scanner.nextInt();
            }

            if(num){
                return new Token(buf, TokenType.DIGIT);
            }

            char c = scanner.next().charAt(0);

            if(TOKENS[c] != null){
                return TOKENS[c];
            }

            return next();
        }
    }

    static class RPNCalculator {
        LinkedList<Integer> stack = new LinkedList<>();

        void addToken(Token t){
            if(t.type == TokenType.OP){

                int v2 = stack.pop();
                int v1 = stack.pop();

                switch (t.val){
                    case '+':
                        stack.push(v1 + v2);
                        break;
                    case '-':
                        stack.push(v1 - v2);
                        break;
                    case '*':
                        stack.push(v1 * v2);
                        break;
                    case '/':
                        stack.push(v1 / v2);
                        break;
                    default:
                        // cant happen
                }

            } else { // DIGIT
                stack.push(t.val);
            }
        }

        int val(){
            return stack.peek();
        }
    }

    public int calculate(String s) {

        RPNCalculator calculator = new RPNCalculator();

        Tokenizer tokenizer = new Tokenizer(s);

        LinkedList<Token> op = new LinkedList<>();

        Token t;

        next:
        while ((t = tokenizer.next()) != EOL){

            // convert to RPN

            if(t.type == TokenType.DIGIT){
                calculator.addToken(t);

            } else { // type == OP

                retry:
                while(true) {

                    if(op.isEmpty()){
                        op.push(t);
                        continue next;
                    }

                    Token top = op.peek();

                    switch (t.val) {
                        case '(':
                            op.push(t);
                            break;

                        case '+':
                        case '-':
                            if (top.val == '+' || top.val == '-' ||
                                top.val == '*' || top.val == '/') {

                                calculator.addToken(op.pop());
                                continue retry;
                            }

                            op.push(t);

                            break;

                        case '*':
                        case '/':
                            if (top.val == '*' || top.val == '/') {
                                calculator.addToken(op.pop());
                                continue retry;
                            }

                            op.push(t);

                            break;

                        case ')':

                            while (!op.isEmpty()) {
                                top = op.pop();

                                if (top.val == '(') continue next;

                                calculator.addToken(top);
                            }

                        default:
                            // cant happen
                    }

                    continue next;
                }
            }
        }

        while (!op.isEmpty()){
            calculator.addToken(op.pop());
        }

        return calculator.val();
    }

}
