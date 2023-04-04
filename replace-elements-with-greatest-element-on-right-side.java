class Solution {
    public int[] replaceElements(int[] arr) {
        
        for(int i = 0; i < arr.length; i++) {

           
           int cur_max = 0;


            for(int j = i + 1; j < arr.length; j++) {
                if(arr[j] > cur_max) {
                    cur_max = arr[j];
                    arr[i] = cur_max;
                }
            }
        }

        arr[arr.length - 1] = -1;
        return arr;

    }
}