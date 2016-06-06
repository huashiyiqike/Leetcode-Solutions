import java.util.*;
public class Solution {
    class TrieNode{
        boolean end = false;
        Map<Character, TrieNode> next = new HashMap<>();
        public void add(String word){
            TrieNode root = this;
            for(char c: word.toCharArray()){
                if(root.next.containsKey(c)){
                    root = root.next.get(c);
                }else{
                    TrieNode tmp = new TrieNode();
                    root.next.put(c, tmp);
                    root = tmp;
                }
            }
            root.end = true;
        }
    }
    public void search(char[][] board, int x, int y,
                          TrieNode root, Set<String> res, String path, boolean[][] vis){
        int[][] dir = {{-1,0},{1,0},{0,1},{0,-1}};
        if(root.next.containsKey(board[x][y])){
            root = root.next.get(board[x][y]);
            if(root.end) res.add(path);
            vis[x][y] = true;
            for(int[] i:dir){
                int tmpx = i[0] + x, tmpy = i[1] + y;
                if(tmpx < 0 || tmpx >= board.length || tmpy < 0 || tmpy >= board[0].length || vis[tmpx][tmpy])
                    continue;
                search(board, tmpx, tmpy, root, res, path + board[tmpx][tmpy], vis);
            }
            vis[x][y] = false;
        }
    }

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for(String i: words) root.add(i);
        Set<String> res = new HashSet<>();
        boolean[][] vis = new boolean[board.length][board[0].length];
        for(int x = 0; x < board.length; x++){
            for(int y = 0; y < board[0].length; y++){
                vis[x][y] = false;
            }
        }
        for(int x = 0; x < board.length; x++){
            for(int y = 0; y < board[0].length; y++){
                search(board, x, y, root, res, String.valueOf(board[x][y]), vis);
            }
        }
        return new ArrayList<>(res);
    }
}

public class Solution {

    static class TrieNode {
        // Initialize your data structure here.
        TrieNode parent;
        int depth = 0;

        char character;

        TrieNode[] children = new TrieNode[26];

        int count = 0;

        public TrieNode(TrieNode parent, char character) {
            this.parent = parent;
            this.character = character;

            if(parent != null) {
                this.depth = parent.depth + 1;
            }
        }

        TrieNode safe(char c){
            int i = index(c);

            if(children[i] == null){
                children[i] = new TrieNode(this, c);
            }

            return children[i];
        }

        int index(char c){
            return (int)(c - 'a');
        }

        void insert(char[] word, int st, int len){
            if(len == 0){
                this.count++;
                return;
            }

            TrieNode t = safe(word[st]);

            t.insert(word, st + 1, len - 1);
        }

        TrieNode child(char c){
            return children[index(c)];
        }

        boolean hasChild(char c){
            return child(c) != null;
        }

        String recover(){
            // assert count > 0
            TrieNode t = this;
            char[] s = new char[depth];

            for(int i = depth - 1; i >= 0; i--){
                s[i] = t.character;
                t = t.parent;
            }

            return new String(s);
        }
    }

    int flatten(int x, int y, int wide){
        return x * wide + y;
    }

    boolean vaild(int x, int y, char[][] board){
        return x >= 0 &&
               y >= 0 &&
               x < board.length &&
               y < board[0].length;
    }

    Set<String> found = new HashSet<>();

    void findWords(int x, int y, char[][] board, boolean[] vi, TrieNode current) {

        vi[flatten(x, y, board[0].length)] = true;

        if(current.count > 0){
            found.add(current.recover());
        }

        for(int[] xy : new int[][] {
            {x + 1, y},
            {x, y + 1},
            {x - 1, y},
            {x, y - 1},
        }) {
            int _x = xy[0];
            int _y = xy[1];

            if(!vaild(_x, _y, board)){
                continue;
            }

            if(vi[flatten(_x, _y, board[0].length)]) {
                continue;
            }

            TrieNode t = current.child(board[_x][_y]);

            if(t == null){
                continue;
            }

            findWords(_x, _y, board, vi, t);

            vi[flatten(_x, _y, board[0].length)] = false;
        }

    }

    public List<String> findWords(char[][] board, String[] words) {

        TrieNode root = new TrieNode(null, '\0');

        for(String w : words){
            root.insert(w.toCharArray(), 0, w.length());
        }

        final int LEN = board.length * board[0].length;

        for(int x = 0; x < board.length; x++){
            for(int y = 0; y < board[0].length; y++){
                if(root.hasChild(board[x][y])){
                    findWords(x, y, board, new boolean[LEN], root.child(board[x][y]));
                }
            }
        }

        return new ArrayList<>(found);
    }
}
