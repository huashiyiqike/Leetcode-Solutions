import java.util.Collections;
import java.util.PriorityQueue;


class MedianFinder {

    PriorityQueue<Integer> up = new PriorityQueue<>(),
            down = new PriorityQueue<>(Collections.reverseOrder());

    // Adds a number into the data structure.
    public void addNum(int num) {
        up.offer(num);
        down.offer(up.poll());
        if (up.size() < down.size()) {
            up.offer(down.poll());
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (up.size() == down.size()) return (up.peek() + down.peek()) / 2.0;
        else return up.peek();
    }
};
