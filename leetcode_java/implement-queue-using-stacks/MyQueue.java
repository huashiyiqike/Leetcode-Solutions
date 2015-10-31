/**
 * Created by lq on 15/7/31.
 */
import java.util.*;
class MyQueue {
    Stack<Integer> s1 = new Stack<Integer>(), s2 = new Stack<Integer>();

    // Push element x to the back of queue.
    public void push(int x) {
        s1.push(x);
    }

    // Removes the element from in front of queue.
    public void trans(){
        if(s2.isEmpty()){
            while(!s1.isEmpty()){
                s2.push(s1.pop());
            }
        }
    }
    public void pop() {
        trans();
        s2.pop();
    }

    // Get the front element.
    public int peek() {
        trans();
        return s2.peek();
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}