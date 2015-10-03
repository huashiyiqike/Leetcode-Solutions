// recursive
public class Solution {
    public boolean isMatch(String s, String p) {

    }
}
public class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
        dp[0][0] = true;
        for (int i = 1; i < p.length(); i++) {
            if (i >= 1 && dp[0][i - 1] && p.charAt(i) == '*')
                dp[0][i + 1] = true;
        }
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if (dp[i][j]) {
                    if (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.')
                        dp[i + 1][j + 1] = true;
                }
                if (p.charAt(j) == '*') {
                    //as one
                    if (dp[i + 1][j]) dp[i + 1][j + 1] = true;
                        // as zero
                    else if (j > 0 && dp[i + 1][j - 1]) dp[i + 1][j + 1] = true;
                        // as many
                    else if (dp[i][j] && j > 0 && (p.charAt(j - 1) == s.charAt(i) || p.charAt(j - 1) == '.'))
                        dp[i + 1][j + 1] = true;
                        // as any
                    else if (dp[i][j + 1] && j > 0 && p.charAt(j - 1) == '.')
                        dp[i + 1][j + 1] = true;
                }
            }
            return dp[s.length()][p.length()];
        }
    }
}

public class Solution {
    static final Character EPSILON = 0;

    static class State{

        static Set<Character> allchar = new HashSet<Character>();

        boolean end;

        Map<Character, Set<State>> next = new HashMap<Character, Set<State>>();

        State(){
            this(false);
        }

        State(boolean end){
            this.end = end;
        }

        State match(Character c) {
            Set<State> states = next.get(c);

            if(states == null){
                states = next.get('.');
            }

            if(states != null) {
                for (State s : states) {
                    return s;
                }
            }

            return null;
        }

        Set<State> matchAll(Character c) {
            Set<State> match = next.get(c);

            return match;
        }

        void addNext(Character c, State s){

            if(c != EPSILON)
                allchar.add(c);

            Set<State> l = next.get(c);

            if(l == null){
                l = new HashSet<State>();
                next.put(c, l);
            }

            l.add(s);
        }
    }

    State nfa(char[] pattern){

        final State end = new State(true);

        State last = end;

        for(int i = pattern.length - 1; i >= 0; i--){
            if(pattern[i] == '*'){
                i--;

                State s1 = new State();
                State s2 = new State();
                State s3 = new State();
                State s4 = last;

                s1.addNext(EPSILON, s2);
                s1.addNext(EPSILON, s4);

                s2.addNext(pattern[i], s3);

                s3.addNext(EPSILON, s4);

                s4.addNext(EPSILON, s2);

                last = s1;

            }else{
                State curr = new State();
                curr.addNext(pattern[i], last);
                last = curr;
            }
        }


        return last;
    }

    boolean end(Set<State> states){
        for (State state : states) {
            if(state.end){
                return true;
            }
        }
        return false;
    }

    State dfa(State start){

        Map<Set<State>, HashMap<Character, Set<State>>> table = new HashMap<Set<State>, HashMap<Character, Set<State>>>();
        Map<Set<State>, State> toone = new HashMap<Set<State>, State>();

        final Set<State> enter = allEpslilon(Collections.singleton(start));

        LinkedList<Set<State>> queue = new LinkedList<Set<State>>();
        queue.add(enter);

        while(!queue.isEmpty()){

            Set<State> key = queue.poll();

            if(!toone.containsKey(key)){
                State maps = new State();
                maps.end = end(key);

                toone.put(key, maps);
            }

            HashMap<Character, Set<State>> targets = searchTarget(key);
            table.put(key, targets);

            for (Set<State> states : targets.values()) {
                if(table.get(states) == null){
                    queue.add(states);
                }
            }

        }

        for (Map.Entry<Set<State>, HashMap<Character, Set<State>>> entry : table.entrySet()) {
            State s = toone.get(entry.getKey());

            for (Map.Entry<Character, Set<State>> t : entry.getValue().entrySet()) {
                s.addNext(t.getKey(), toone.get(t.getValue()));
            }

        }

        return toone.get(enter);
    }

    HashMap<Character, Set<State>> searchTarget(Set<State> form) {
        HashMap<Character, Set<State>> targets = new HashMap<Character, Set<State>>();

        for(State s : form) {
            for (Character c : State.allchar) {
                Set<State> ns = s.matchAll(c);

                if (ns == null) continue;

                Set<State> states = allEpslilon(ns);
                
                Set<State> t = targets.get(c);
                if(t == null){
                    t = new HashSet<State>();
                    targets.put(c, t);
                }

                t.addAll(states);           
                
            }
        }

        return targets;
    }

    Set<State> allEpslilon(Set<State> ns) {
        Set<State> states = new HashSet<State>();
        states.addAll(ns);


        int oldsize = 0;


        while (states.size() != oldsize) {

            oldsize = states.size();

            Set<State> temp = new HashSet<State>();

            for (State target : states) {
                Set<State> t = target.matchAll(EPSILON);
                if (t != null) temp.addAll(t);
            }

            states.addAll(temp);

        }
        return states;
    }

    boolean isMatch(char[] s, State state, int p){

        if(state == null){
            return false;
        }

        if(p >= s.length){
            return state.end;
        }

        for (Map.Entry<Character, Set<State>> entry : state.next.entrySet()) {

            Character key = entry.getKey();
            if(key.equals(s[p]) || key.equals('.')){
                if(isMatch(s, entry.getValue().iterator().next(), p + 1)){
                    return true;
                }
            }
        }

        return false;
    }    

    public boolean isMatch(String s, String p) {

        State.allchar = new HashSet<Character>();

        State state = nfa(p.toCharArray());
        state = dfa(state);

        char[] chars = s.toCharArray();

        return isMatch(chars, state, 0);
    }
}