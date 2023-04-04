class Solution {
    public boolean isSubsequence(String s, String t) {
        /*
        *   Plan: cycle through s, maintain cur place in s with char,
        *   when char is found in t, inc s 1, ONLY loop through t one time.
        */

        int cur = 0;

        if(s.equals("")) {
            return true;
        }

        for(int i = 0; i < t.length(); i++) {
            if(s.charAt(cur) == t.charAt(i)) {
                cur++;
            }
            if(cur >= s.length()) {
                return true;
            }
        }

        if(cur >= s.length()) {
            return true;
        }


        return false;
    }
}