public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
        List<List<String>>  result = new ArrayList<List<String>>();
        List<String> path = new ArrayList<String>();
        HashMap<String,List<String>> neibor = new HashMap<String,List<String>>();
        HashMap<String,Integer>dis = new HashMap<String,Integer>();
        wordList.add(endWord);
        bfs(beginWord,endWord,wordList,neibor,dis);
        dfs(beginWord,endWord,wordList,neibor,dis,result,path);
        return result;
    }
     public void dfs(String cur,String end, Set<String> wordList,HashMap<String,List<String>>neibor,HashMap<String,Integer> dis, List<List<String>> result, List<String> path){
         path.add(cur);
          if(end.equals(cur)){
             // System.out.println(path.size());
              result.add(new ArrayList<String>(path));
              
          }else{
         List<String> nei = neibor.get(cur);
         for(String s:nei){
             if(dis.get(s) == dis.get(cur)+1){
                 dfs(s,end,wordList,neibor,dis,result,path);
             }
            }
          }
          path.remove(path.size()-1);
      }
    public void bfs(String start,String end, Set<String> wordList,HashMap<String,List<String>>neibor,HashMap<String,Integer> dis){
         LinkedList<String>  queue = new LinkedList<String>();
         queue.offer(start);
         dis.put(start,0);
         neibor.put(start,new ArrayList<String>());
         for(String s:wordList){
             neibor.put(s,new ArrayList<String>());
         }
         boolean flag = false;
             while(!queue.isEmpty()){
                int size = queue.size();
                for(int i = 0;i < size; i++){
                    String front = queue.poll();
                    int high = dis.get(front);
                    List<String> nei = getNeibor(front,wordList);
                    for(String s:nei){
                        neibor.get(front).add(s);
                        if(!dis.containsKey(s)){
							dis.put(s,high+1);
							if(s.equals(end)){
								flag =true ;
                                }
							queue.offer(s);
                        }
                    }
                }
				if(flag==true){
					break;
				}
        }
    }
    public  List<String> getNeibor(String cur,Set<String>wordList){
        char[] temp = cur.toCharArray();
        int len = temp.length;
        List<String> nei = new ArrayList<String>();
         for(int i = 0;i < len; i++){
                    for(char c = 'a';c <= 'z'; c++){
                        char tem = temp[i];
                        if(tem == c) continue;  
                        temp[i] = c;
                        String newWord = new String(temp);
                        if(wordList.contains(newWord)){
                           nei.add(newWord);
                           //wordList.remove(newWord);
                        }
                        temp[i] = tem;
                    }
                }
                return nei;
    }
}
  