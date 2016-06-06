public class WordDictionary {
   class Node{
       boolean isLeaf;
       Node[] child = new Node[26];
       public Node() {
        }
   }
   Node root = new Node();
    // Adds a word into the data structure.
    public void addWord(String word) {
        addWord(word.toCharArray(),0,root);
    }
  public void addWord(char[] word,int i,Node root) {
        if(i == word.length){
            root.isLeaf = true;
            return ;
        }
        char c = word[i];
        if( root.child[ c - 'a'] == null){
          Node node = new Node();
          root.child[c - 'a'] = node;
          
        }
           root = root.child[c - 'a'];
   
        addWord(word,i+1,root);
    }
    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return search(word.toCharArray(),0,root);
    }
     public boolean search(char[] word,int i,Node root) {
         if(root != null){
           if(i == word.length){
             return root.isLeaf;
            }
           char c = word[i];
           if(c =='.'){
               for(int j=0;j<26;j++){
                   if(root.child[j] != null){
						if(search(word,i+1,root.child[j])){
							 return true;
						};
                   }
                   
               }
               return false;
           }else{
               return search(word,i+1,root.child[c-'a']);
           }
           
         }else{
             return false;
         }
       
    }
}
