import java.util.*;


// As we know, the area = width * height
// For every bar, the 'height' is determined by the loweset bar.
//
// 1) We traverse all bars from left to right, maintain a stack of bars. Every bar is pushed to stack once.
// 2) A bar is popped from stack when a bar of smaller height is seen.
// 3) When a bar is popped, we calculate the area with the popped bar as smallest bar.
// 4) How do we get left and right indexes of the popped bar –
//    the current index tells us the ‘right index’ and index of previous item in stack is the ‘left index’.
//
//
// In other word, the stack only stores the incresing bars, let's see some example
//
// Example 1
// ---------
// height = [1,2,3,4]
//
//    stack[] = [ 0, 1, 2, 3 ], i=4
//
//    1) pop 3,  area = height[3] * 1 = 4
//    2) pop 2,  area = height[2] * 2 = 4
//    3) pop 1,  area = height[1] * 3 = 6
//    4) pop 0,  area = height[0] * 4 = 4
//
//
// Example 2
// ---------
// height = [2,1,2]
//
//    stack[] = [ 0 ], i=1
//    1) pop 0,  area = height[0] * 1 = 2
//
//    stack[] = [ 1,2 ], i=3, meet the end
//    1) pop 2,  area = height[2] * 1 = 2
//    2) pop 1,  area = height[1] * 3 = 3
//
//
// Example 3
// ---------
// height =  [4,2,0,3,2,5]
//
//    stack[] = [ 0 ], i=1, height[1] goes down
//    1) pop 0,  area = height[0] * 1 = 4
//
//    stack[] = [ 1 ], i=2, height[2] goes down
//    1) pop 1,  area = height[1] * 2 = 4 // <- how do we know the left?
//                                              start from the 0 ??
//
//    stack[] = [ 2, 3 ], i=4, height[4] goes down
//    1) pop 3,  area = height[3] * 1 = 3
//    2) pop 2,  area = height[2] * ? = 0 // <- how do we know the left?
//                                              start from the 0 ??
//
//    stack[] = [ 2,4,5 ], i=6,  meet the end
//    1) pop 5,  area = height[5] * 1 = 5
//    2) pop 4,  area = height[4] * 3 = 6 // <- how do we know the left?
//                                              need check the previous item.
//    3) pop 2,  area = height[2] * ? = 4 // <- how do we know the left?
//                                              start from the 0 ??
//
//    so, we can see, when the stack pop the top, the area formular is
//
//          height[stack_pop] *  i - stack[current_top] - 1,   if stack is not empty
//          height[stack_pop] *  i,                            if stack is empty
//
public class Solution {
    public int largestRectangleArea(int[] height) {
        Deque<Integer> stack = new LinkedList<>();
        height = Arrays.copyOf(height, height.length + 1);
        // height[height.length-1] = 0;
        int idx = 0, res = 0;
        while (idx < height.length) {
            while (!stack.isEmpty() && height[stack.peek()] > height[idx]) {
                int h = height[stack.pop()];
                int w = stack.isEmpty() ? idx : idx - stack.peek() - 1;
                res = Math.max(h * w, res);
            }
            stack.push(idx++);
        }
        return res;
    }
}

public class Solution {

    static class Rect {
        int width = 1;
        int height;

        Rect(int height) {
            this.height = height;
        }
    }

    public int largestRectangleArea(int[] height) {

        if (height.length == 0) return 0;

        height = Arrays.copyOf(height, height.length + 1);
        height[height.length - 1] = 0;

        Deque<Rect> stack = new LinkedList<Rect>();

        stack.push(new Rect(height[0]));

        int max = 0;

        next:
        for (int i = 1; i < height.length; i++) {
            int h = height[i];

            Rect r = new Rect(h);

            int sl = 0;
            while (true) {

                if (stack.isEmpty() || h > stack.peek().height) {
                    stack.push(r);
                    continue next;
                }


                Rect left = stack.pop();

                sl += left.width;
                max = Math.max(max, left.height * sl);

                r.width = 1 + sl; // merge left into new
            }

        }

        return max;
    }
}