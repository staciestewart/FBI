class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        // Sorting the input array
        Arrays.sort(nums);

        // Create new linked list
        List<List<Integer>> res = new LinkedList<>(); 

        // Iterate over the list from 0 to list last 2 elements
        for (int i = 0; i < nums.length-2; i++) {

            // if i == 0 or (i > 0 and element i is equal to i -1)
            if (i == 0 || (i > 0 && nums[i] != nums[i-1])) {

                // create index for second and third elements
                int lo = i+1, hi = nums.length-1, sum = 0 - nums[i];
                
                // while lower element is smaller than larger element
                while (lo < hi) {

                    // if total sum of 3 elements is equal to 0 and the add to result array
                    if (nums[lo] + nums[hi] == sum) {
                        res.add(Arrays.asList(nums[i], nums[lo], nums[hi]));

                        // skip one lo increment if element lo == element lo++
                        while (lo < hi && nums[lo] == nums[lo+1]) lo++;

                        // skip one lo increment if element hi == element hi--
                        while (lo < hi && nums[hi] == nums[hi-1]) hi--;

                        // increment lo and hi
                        lo++; hi--;

                    // if 3 sum is smaller than 0 then increment lo
                    } else if ( nums[lo] + nums[hi] < sum)
                        lo++;
                    // else when 3 sum is larger than 0 and decrement hi
                    else hi--;
               }
            }
        }
        return res;   
    }
}