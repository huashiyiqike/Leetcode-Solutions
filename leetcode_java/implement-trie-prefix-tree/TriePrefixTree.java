class TrieNode {
    // Initialize your data structure here.
		boolean isLeaf = false;
		TrieNode[] child = new TrieNode[26];
		public TrieNode() {
    }
}

public class Trie {
    private TrieNode root;
    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        insertNode(word.toCharArray(),0,root);
    }
   public void insertNode(char[] word,int index,TrieNode root){
       if(index == word.length){
           root.isLeaf = true;
           return ;
       }
       char c = word[index];
       if(root.child[c-'a'] == null){
           root.child[c-'a'] = new TrieNode();
       }
       insertNode(word,index+1,root.child[c-'a']);
   }
    // Returns if the word is in the trie.
    public boolean search(String word) {
       return  searchNode(word.toCharArray(),0,root);
    }
   public boolean searchNode(char[] word,int i,TrieNode root){
       if(root != null){
			if(i == word.length){
			   return root.isLeaf;
			}
			char c = word[i];
			return searchNode(word, i+1,root.child[c-'a']);
       }else{
           return false;
       }
      
   }
    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
       return  startsWith(prefix.toCharArray(),0,root);
    }
    public boolean startsWith(char[] word,int i,TrieNode root) {
         if(root != null){
            if(i == word.length){
               return true;
			}
           char c = word[i];
           return startsWith(word, i+1,root.child[c-'a']);
		}else{
           return false;
		}
	}
}