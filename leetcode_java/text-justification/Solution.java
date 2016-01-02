import java.util.LinkedList;
import java.util.List;

public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new LinkedList<String>();
        int index = 0;
        List<String> tmpres = new LinkedList<>();
        while (index < words.length) {
            int count = words[index].length();
            tmpres.clear();
            tmpres.add(words[index++]);
            while (index < words.length && count + words[index].length() + 1 <= maxWidth) {
                count += words[index].length() + 1;
                tmpres.add(words[index++]);
            }
            int left = maxWidth - count;
            int mins = left - 1;
            if (tmpres.size() != 1) mins = left / (tmpres.size() - 1);
            left -= mins * (tmpres.size() - 1);
            String tmpstring = "";
            for (int j = 0; j < tmpres.size(); j++) {
                tmpstring += tmpres.get(j);
                if (j != tmpres.size() - 1) {
                    for (int tmp1 = 0; tmp1 < mins + 1; tmp1++)
                        tmpstring += " ";
                }
                if (left > 0) {
                    left--;
                    tmpstring += " ";
                }
            }
            while (tmpstring.length() < maxWidth) tmpstring += " ";
            res.add(tmpstring);
        }
        String s = res.get(res.size() - 1), news = "";
        for (index = 0; index < s.length(); index++) {
            if (s.charAt(index) == ' ') {
                while (index + 1 < s.length() && s.charAt(index + 1) == ' ') index++;
                news += " ";
            } else {
                news += s.charAt(index);
            }
        }
        while (news.length() < maxWidth) news += " ";
        res.remove(res.size() - 1);
        res.add(news);
        return res;
    }
}

https://leetcode.com/discuss/13610/share-my-concise-c-solution-less-than-20-lines
public class Solution {
    public List<String> fullJustify(String[] words, int L) {
        List<String> list = new LinkedList<String>();

        for (int i = 0, w; i < words.length; i = w) {
            int len = -1;
            for (w = i; w < words.length && len + words[w].length() + 1 <= L; w++) {
                len += words[w].length() + 1;
            }

            StringBuilder strBuilder = new StringBuilder(words[i]);
            int space = 1, extra = 0;
            if (w != i + 1 && w != words.length) { // not 1 char, not last line
                space = (L - len) / (w - i - 1) + 1;
                extra = (L - len) % (w - i - 1);
            }
            for (int j = i + 1; j < w; j++) {
                for (int s = space; s > 0; s--) strBuilder.append(' ');
                if (extra-- > 0) strBuilder.append(' ');
                strBuilder.append(words[j]);
            }
            int strLen = L - strBuilder.length();
            while (strLen-- > 0) strBuilder.append(' ');
            list.add(strBuilder.toString());
        }

        return list;
    }
}


public class Solution {
    public List<String> fullJustify(String[] words, int L) {
        List<String> lines = new ArrayList<String>();

        int index = 0;
        while (index < words.length) {
            int count = words[index].length();
            int last = index + 1;
            while (last < words.length) {
                if (words[last].length() + count + 1 > L) break;
                count += words[last].length() + 1;
                last++;
            }

            StringBuilder builder = new StringBuilder();
            int diff = last - index - 1;
            // if last line or number of words in the line is 1, left-justified
            if (last == words.length || diff == 0) {
                for (int i = index; i < last; i++) {
                    builder.append(words[i] + " ");
                }
                builder.deleteCharAt(builder.length() - 1);
                for (int i = builder.length(); i < L; i++) {
                    builder.append(" ");
                }
            } else {
                // middle justified
                int spaces = (L - count) / diff;
                int r = (L - count) % diff;
                for (int i = index; i < last; i++) {
                    builder.append(words[i]);
                    if (i < last - 1) {
                        for (int j = 0; j <= (spaces + ((i - index) < r ? 1 : 0)); j++) {
                            builder.append(" ");
                        }
                    }
                }
            }
            lines.add(builder.toString());
            index = last;
        }


        return lines;
    }
}

public class Solution {
    public List<String> fullJustify(String[] words, int L) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < L; ++i) {
            sb.append(" ");
        }
        final String pads = sb.toString();
        final List<String> strs = new ArrayList<>();
        for (int i = 0, sum = 0, j = 0; i < words.length; i = j) {
            for (j = i + 1, sum = words[i].length(); j < words.length && sum + j - i + words[j].length() <= L; ++j) {
                sum += words[j].length();
            }

            final StringBuilder l = new StringBuilder();
            final int n = j - 1 - i;
            final int m = (j == words.length || 0 == n) ? 1 : ((L - sum) / n);
            final int b = (j == words.length) ? 0 : (L - sum - m * n);

            for (int k = i; k < j - 1; ++k) {
                l.append(words[k]);
                l.append(pads.substring(0, (k - i < b) ? (m + 1) : m));
            }

            l.append(words[j - 1]);
            if (j == words.length || 0 == n) {
                l.append(pads.substring(0, L - sum - n));
            }

            strs.add(l.toString());
        }

        return strs;
    }
}

public class Solution {

    String space(int len) {
        char[] s = new char[len];
        Arrays.fill(s, ' ');
        return new String(s);
    }

    public List<String> fullJustify(String[] words, int L) {

        ArrayList<String> text = new ArrayList<String>();

        int p = 0;
        int lastp = 0;
        while (p < words.length) {

            if (L == 0 && "".equals(words[p])) {
                text.add("");
                p++;
                continue;
            }

            int l = 0;
            while (l < L && p < words.length) {
                l += words[p++].length() + 1;
            }

            if (l - 1 > L) l -= words[--p].length() + 1;

            int count = p - lastp;
            int left = L - l + count;

            int add;
            if (count == 1) add = left;
            else if (p - 1 == words.length - 1) {
                add = 1;
                left = count - 1;
            } // fuck...
            else add = left / (count - 1);

            left -= add * (count - 1);

            String s = "";
            for (int i = lastp; i < p - 1; i++) {
                if (left > 0) {
                    s += words[i] + space(add + 1);
                    left--;
                } else {
                    s += words[i] + space(add);
                }
            }

            left = L - s.length() - words[p - 1].length();

            if (count == 1 || p - 1 == words.length - 1) // fuck...
                s += words[p - 1] + space(left);
            else
                s += space(left) + words[p - 1];

            text.add(s);
            lastp = p;
        }

        return text;

    }
}
