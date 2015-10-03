import java.util.*;

public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordDict) {
        // BFS with queue
        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);
        wordDict.remove(beginWord);
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> bpmap = new HashMap<>();
        while(!queue.isEmpty()){
            Set<String> next = new HashSet<>();
            for(String s:queue) {
                wordDict.remove(s);
                if (s.equals(endWord)) {
                    List<String> path = new ArrayList<>();
                    path.add(endWord);
                    bp(res, path, endWord, beginWord, bpmap);
                    return res;
                }
            }
            while(!queue.isEmpty()) {
                String s = queue.poll();
                wordDict.remove(s);
                if(s.equals(endWord)){
                    List<String> path = new ArrayList<>();
                    path.add(endWord);
                    bp(res, path, endWord, beginWord, bpmap);
                    return res;
                }
                for (int i = 0; i < s.length(); i++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        String newstr = s.substring(0, i) + c + s.substring(i + 1, s.length());
                        if (wordDict.contains(newstr)) {
                            List<String> l;
                            if (bpmap.containsKey(newstr))
                                l = bpmap.get(newstr);
                            else
                                l = new ArrayList<>();
                            l.add(s);
                            bpmap.put(newstr, l);
                            next.add(newstr);
                        }

                    }
                }

            }
            queue = new LinkedList<>(next); //queue = new LinkedList<>(next);
        }
        return res;
    }
    public void bp(List<List<String>>res, List<String> path, String endWord,
                   String beginWord, Map<String, List<String>> bpmap ){
        List<String> l = bpmap.get(endWord);
        if(l == null) return;
        for(int i = 0; i < l.size(); i++){
            List<String> newpath = new ArrayList<>(path);
            newpath.add(0,l.get(i));
            if(l.get(i).equals(beginWord)) {
                res.add(newpath);
                continue;
            }
            bp(res, newpath, l.get(i), beginWord, bpmap);
        }
    }
}
public class Solution {
    
    static class Word {

        String word;
        Set<Word> next;

        boolean end;

        Word(String word){
            this.word = word;
        }
    }

    static class Trace {

        Word obj;
        Trace prev;

        Trace(Word obj,Trace prev){
            this.obj  = obj;
            this.prev = prev;
        }
    }


    HashMap<String, Word> wmap;

    void connect(Word w, Set<String> dict){
        if(w.next != null) return;

        Set<Word> n = new HashSet<Word>();

        char[] ws = w.word.toCharArray();

        for(int i = 0; i < ws.length; i++){
            char t = ws[i];

            for(char r = 'a'; r <= 'z'; r++){
                ws[i] = r;

                String d = new String(ws);
                if(dict.contains(d)){
                    Word c = wmap.get(d);
                    n.add(c);
                }
            }

            ws[i] = t;
        }

        w.next = n;
    }


    public List<List<String>> findLadders(String start, String end, Set<String> dict) {


        List<List<String>> rt = new ArrayList<List<String>>();

        wmap = new HashMap<String, Word>();

        for(String d : dict){
            Word w = new Word(d);
            wmap.put(d, w);
        }

        Word _end = new Word(end);
        _end.end = true;
        wmap.put(end, _end);

        // help to connected to end
        dict.add(end);


        final Trace SEP = new Trace(null, null);
        LinkedList<Trace> queue = new LinkedList<Trace>();
        
        queue.add(new Trace(new Word(start), null));
        queue.add(SEP);

        boolean found = false;

        HashSet<Word> vi = new HashSet<Word>();
        HashSet<Word> svi = new HashSet<Word>();

        while(!queue.isEmpty()){

            Trace step = queue.poll();

            if(step == SEP) {
                vi.addAll(svi);
                svi.clear();
                
                if (found) break;
                if (!queue.isEmpty()) queue.add(SEP);
                
            } else {

                Word word = step.obj;
                connect(word, dict);
    
                
                if(word.end){
    
                    LinkedList<String> r = new LinkedList<String>();
    
    
                    Trace t = step;
    
                    while (t != null){
                        r.addFirst(t.obj.word);
                        t = t.prev;
                    }
    
                    rt.add(r);
    
                    found = true;
                    
                }else if(!found){ // prevent deeper level to be visited
    
                    for (Word p : word.next) {
    
                        if(!vi.contains(p)) {
                            queue.add(new Trace(p, step));
                            svi.add(p);
                        }
                    }
                }
            }
        }


        return rt;
    }
}
