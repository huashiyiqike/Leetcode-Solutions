/*
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
*/

public class Solution {
    class Trie{
        String word;
        Trie[] child=new Trie[26];
    }
    Trie root=new Trie();
    public List<String> findWords(char[][] board, String[] words) {
        List<String> list=new ArrayList<String>();
        if(board==null||board.length==0||words==null||words.length==0){
            return list;
        }
        for(String s :words){
            trieInsert(s.toCharArray(),root);
        }
        int xLen=board.length;
        int yLen=board[0].length;
         for(int i=0;i<xLen;i++){
             for(int j=0;j<yLen;j++){
                 dfs(board,i,j,xLen-1,yLen-1,root,list);
             }
         }
         return list;
    }
    public void dfs(char[][] board,int i,int j,int xLen,int yLen,Trie root, List<String> list){
        if(i<0||j<0||i>xLen||j>yLen) return ;
        char c=board[i][j];
        if(board[i][j]=='#'||root.child[c-'a']==null) return ;
        root=root.child[c-'a'];
        if(root.word!=null){
            list.add(root.word);
            root.word=null;
        }
       
        board[i][j]='#';
        if(i>0){
            dfs(board,i-1,j,xLen,yLen,root,list);
        }
        if(j>0){
            dfs(board,i,j-1,xLen,yLen,root,list);
        }
        if(i<xLen){
            dfs(board,i+1,j,xLen,yLen,root,list);
        }
        if(j<yLen){
            dfs(board,i,j+1,xLen,yLen,root,list);
        }
        board[i][j]=c;
    }
    public void trieInsert(char[] word,Trie root){
        Trie node=root;
        for(char c :word){
            int temp=c-'a';
            if(node.child[temp]==null){
                node.child[temp]=new Trie();
            }
            node=node.child[temp];
        }
        node.word=String.valueOf(word);
    }
}