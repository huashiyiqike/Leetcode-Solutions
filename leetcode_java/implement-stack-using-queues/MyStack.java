import java.util.*;
class MyStack {
    Queue<Integer> q1 = new LinkedList<>();
    // Push element x onto stack.
    public void push(int x) {
        q1.offer(x);
    }

    // Removes the element on top of the stack.
    public void pop() {
        for(int i = 0; i < q1.size()-1; i++){
            q1.offer(q1.poll());
        }
        if(q1.size() > 0)
            q1.poll();
    }

    // Get the top element.
    public int top() {
        int tmp = 0;
        for(int i = 0; i < q1.size(); i++){
            tmp = q1.poll();
            q1.offer(tmp);
        }
        return tmp;

    }

    // Return whether the stack is empty.
    public boolean empty() {
        return q1.isEmpty();
    }
}

class MyStack {

    Queue<Integer> queue = new LinkedList<>();

    // Push element x onto stack.
    public void push(int x) {
        Queue<Integer> swap = new LinkedList<>();

        swap.add(x);

        while(!queue.isEmpty()){
            swap.add(queue.remove());
        }

        queue = swap;
    }

    // Removes the element on top of the stack.
    public void pop() {
        // pop from front
        queue.remove();
    }

    // Get the top element.
    public int top() {
        // peek from front
        return queue.peek();
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return queue.isEmpty();
    }
}
