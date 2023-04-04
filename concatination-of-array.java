class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] result = new int[nums.length*2];
        int arrplace = 0;
        
            for(int i = 0; i < nums.length ; i++) {
                result[arrplace] = nums[arrplace];
                result[arrplace + nums.length] = nums[arrplace];
                arrplace++;
            }
            

        return result;
    }
}