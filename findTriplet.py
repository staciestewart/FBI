class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the Array
        a = sorted(nums)
        results = []
        # Get array length of n
        n = len(nums)
        
        # Iterate over the array from i = 0 to n-2
        for i in range(0, n-2):
            
            # Create 2 index l and r, l = i + 1 and r = n-1
            l,r = i+1, n-1
            print(l,r)

            # If sum of nums[i], nums[l] and nums[r] = 0 then print out the array, l++, r--
            if sum(nums[i], nums[l], nums[r]) == 0:
                l++
                r--
                results.append[[nums[i], nums[l], nums[r]]]
            # If sum of nums[i], nums[l] and nums[r] < 0 then l++
            elif sum(nums[i], nums[l], nums[r]) < 0:
                l++
                
            # If sum of nums[i], nums[l] and nums[r] > 0 then r--
            elif sum(nums[i], nums[l], nums[r]) > 0:
                r--
            
            # If no exist then print not found
            else:
                print("there is no triplet")

        return result
            
            
    
        