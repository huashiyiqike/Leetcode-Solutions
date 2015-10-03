class TrieNode{
    boolean end = false;
    Map<Character, TrieNode> next = new HashMap<>();
};
public class WordDictionary {
    TrieNode root = new TrieNode();
    // Adds a word into the data structure.
    public void addWord(String word) {
        char[] words = word.toCharArray();
        TrieNode cur = root;
        for(char c: words){
            if(cur.next.containsKey(c)){
                cur = cur.next.get(c);
            }else{
                TrieNode newnode = new TrieNode();
                cur.next.put(c, newnode);
                cur = newnode;
            }
        }
        cur.end = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        char[] words = word.toCharArray();
        List<TrieNode> cur = new ArrayList<>();
        cur.add(root);
        for(char c: words){
            List<TrieNode> next = new ArrayList<>();
            for(TrieNode t:cur){
                if(c == '.'){
                    next.addAll(new ArrayList<>(t.next.values())); //for(TrieNode tmpnode: t.next.values()){
                }
                else if(t.next.containsKey(c)){
                    TrieNode tmp = t.next.get(c);
                    next.add(tmp);

                }
            }
            if(next.isEmpty()) return false;
            cur = new ArrayList<>(next);
        }
        for(TrieNode t:cur){
            if(t.end) return true;
        }
        return false;
    }
};



// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
public class WordDictionary {

    static class TrieNode {
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

            if(word[st] == '.'){

                for(TrieNode t : children){
                    if(t != null){
                        if(t.search(word, st + 1, len - 1)){
                            return true;
                        }
                    }
                }

                return false;
            }

            TrieNode t = children[index(word[st])];

            if(t == null){
                return false;
            }

            return t.search(word, st + 1, len - 1);
        }
    }

    TrieNode root = new TrieNode();

    // Adds a word into the data structure.
    public void addWord(String word) {
        root.insert(word.toCharArray(), 0, word.length());
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return root.search(word.toCharArray(), 0, word.length());
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
