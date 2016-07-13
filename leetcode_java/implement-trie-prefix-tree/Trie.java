import java.util.*;

class TrieNode {
    HashMap<Character, TrieNode> next;
    boolean end;
    // Initialize your data structure here.
    public TrieNode() {
        end = false;
        next = new HashMap<Character, TrieNode>();
    }
}
public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode tmp = root;
        for(char c : word.toCharArray()){
            if(tmp.next.containsKey(c))
                tmp = tmp.next.get(c);
            else {
                TrieNode t = new TrieNode();
                tmp.next.put(c, t);//new TrieNode());
                tmp = t;
            }
        }
        tmp.end = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode tmp = root;
        for(char c : word.toCharArray()){
            if(tmp.next.containsKey(c)){
                tmp = tmp.next.get(c);
            }
            else return false;
        }
        return tmp.end;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode tmp = root;
        for(char c : prefix.toCharArray()){
            if(tmp.next.getOrDefault(c, null) != null){
                tmp = tmp.next.get(c);
            }
            else return false;
        }
        return true;
    }
}
// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");

class TrieNode {
    // Initialize your data structure here.
    
    TrieNode[] children = new TrieNode[26];
    
    int count = 0;
    
    public TrieNode() {
        
    }
    
    TrieNode safe(int i){
        if(children[i] == null){
            children[i] = new TrieNode();
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
        
        TrieNode t = safe(index(word[st]));
        
        t.insert(word, st + 1, len - 1);
    }
    
    boolean search(char[] word, int st, int len){
        if(len == 0){
            return this.count > 0;
        }
        
        TrieNode t = children[index(word[st])];
        
        if(t == null){
            return false;
        }
        
        return t.search(word, st + 1, len - 1);
    }
    
    boolean startsWith(char[] prefix, int st, int len) {
        if(len == 0){
            return true;
        }
        
        TrieNode t = children[index(prefix[st])];
        
        if(t == null){
            return false;
        }
        
        return t.startsWith(prefix, st + 1, len - 1);        
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        root.insert(word.toCharArray(), 0, word.length());
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        return root.search(word.toCharArray(), 0, word.length());
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        return root.startsWith(prefix.toCharArray(), 0, prefix.length());
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
