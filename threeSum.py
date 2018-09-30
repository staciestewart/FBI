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

            # If sum of nums[i], nums[l] and nums[r] = 0 then print out the array, l++, r--
            while l < r:
                if (a[i] + a[l] + a[r] == 0):
                    # results.append([nums[i], nums[l], nums[r]]
                    t = [a[i],a[l],a[r]]
                    if t not in results:
                        results.append([a[i],a[l],a[r]])
                    l+=1
                    r-=1
                    
                # If sum of nums[i], nums[l] and nums[r] < 0 then l++
                elif (a[i] + a[l] + a[r] < 0):
                    l+=1
                
                # If sum of nums[i], nums[l] and nums[r] > 0 then r--
                else:
                    r-=1
        return results
            
            
    
        