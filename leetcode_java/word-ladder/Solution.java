public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordDict) {
        // BFS with queue
        Queue<String> queue = new LinkedList<>();
        List<List<String>> res = new ArrayList<>();
        queue.offer(beginWord);
        wordDict.remove(beginWord);
        int length = 1;
        while(!queue.isEmpty()){
            Queue<String> next = new LinkedList<>();
            while(!queue.isEmpty()) {
                String s = queue.poll();
                for (int i = 0; i < s.length(); i++) {
                    if (s.equals(endWord)) return length;
                    for (char c = 'a'; c <= 'z'; c++) {
                        String newstr = s.substring(0, i) + c + s.substring(i + 1, s.length());
                        if (wordDict.contains(newstr)) {
                            next.offer(newstr);
                            wordDict.remove(newstr);
                        }
                    }
                }
            }
            length++;
            queue = next; //queue = new LinkedList<>(next);
        }
        return ;
    }
}
public class Solution {

    public int ladderLength(String start, String end, Set<String> dict) {
        
        LinkedList<String> queue = new LinkedList<String>();
        final String END = new String();
        
        queue.add(start);
        queue.add(END);
        
        int level = 0;
        HashSet<String> vi = new HashSet<String>();
        
        while(!queue.isEmpty()){
            
            String current = queue.poll();
            
            if(current == END){
                level++;
                
                if(!queue.isEmpty()) queue.add(END);
            }else{
                
                if(end.equals(current))
                    return level + 1;
                
                char[] word = current.toCharArray();
                
                for(int i = 0; i < word.length; i++){
                    
                    char old = word[i];
                    
                    for(char j = 'a'; j <= 'z' ; j++){
                        
                        if(j == old)
                            continue;
                        
                        word[i] = j;
                        
                        String s = new String(word);
                        
                        if(dict.contains(s) && !vi.contains(s)){
                            queue.add(s);
                            vi.add(s);
                        }
                        
                    }
                    
                    word[i] = old;
                }
                
            }
            
        }
        
        return 0;
        
    }
}
