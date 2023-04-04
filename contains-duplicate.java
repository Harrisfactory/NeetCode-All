class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> dupes = new HashMap<>();

        for (int number : nums) {
            if (dupes.containsKey(number)) {
                return true;
            } else {
                dupes.put(number, 1);
            }
        }

        return false;
    }
}