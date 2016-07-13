import java.util.LinkedList;

class MinStack {
    int min_value = Integer.MIN_VALUE;
    LinkedList<Integer> stack = new LinkedList<>();
    public void push(int x) {
        if(x < min_value){
            min_value = x;
        }
        stack.push(min_value);
        stack.push(x);
    }

    public void pop() {
        if(!stack.isEmpty()) {
            stack.pop();
            stack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        if(stack.size()>=2)
            return stack.get(1);
        return 0;
    }
}

class MinStack {

    static class Stack {

        static class Node {
            int val;
            Node next;
            Node prev;
        }

        Node head = new Node();
        int size = 0;

        public void push(int x) {
            Node n = new Node();
            n.val = x;
            n.prev = head;

            head.next = n;
            head = n;

            size++;
        }

        public void pop() {
            head = head.prev;
            size--;
        }

        public int top() {
            return head.val;
        }
    }

    Stack data = new Stack();
    Stack mins = new Stack();

    public void push(int x) {
        data.push(x);

        if(mins.size == 0 || getMin() >= x){
            mins.push(x);
        }
    }

    public void pop() {
        int last = data.top();
        data.pop();

        if(last <= getMin()){
            mins.pop();
        }
    }

    public int top() {
        return data.top();
    }

    public int getMin() {
        if(mins.size > 0){
            return mins.top();
        }

        throw new IllegalStateException();
    }
}
