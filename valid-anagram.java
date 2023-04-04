class Solution {
    public boolean isAnagram(String s, String t) {
        //storing each in hashmap and counting vals for each key

        HashMap<Character, Integer> s_org = new HashMap<>();
        HashMap<Character, Integer> t_org = new HashMap<>();

        for(char sc : s.toCharArray()) {
            if(s_org.containsKey(sc)) {
                s_org.put(sc, s_org.get(sc) + 1);
            } else {
                s_org.put(sc, 1);
            }
        }
        for(char tc : t.toCharArray()) {
            if(t_org.containsKey(tc)) {
                t_org.put(tc, t_org.get(tc) + 1);
            } else {
                t_org.put(tc, 1);
            }
        }

    

        if(s_org.equals(t_org)) {
            return true;
        }

        return false;
    }
}