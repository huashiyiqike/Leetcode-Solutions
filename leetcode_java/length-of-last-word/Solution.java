import java.util.LinkedList;

public class Solution {
    public int lengthOfLastWord(String s) {
        String use = s.trim();
        int count = 0;
        for (int i = use.length() - 1; i >= 0; i--) {
            if (use.charAt(i) != ' ') count++;
            else break;
        }
        return count;
    }
}

public class Solution {
    public int lengthOfLastWord(String s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.

        if (s == null) return 0;

        char[] chars = s.toCharArray();

        int upper = chars.length - 1;
        while (upper >= 0 && chars[upper] == ' ') upper--;

        int len = 0;
        for (int i = 0; i <= upper; i++) {
            if (chars[i] == ' ') len = 0;
            else len++;
        }

        return len;

    }
}