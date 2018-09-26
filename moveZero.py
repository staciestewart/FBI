# nums is a random list of number
# create a count and set at 0
# increment the array from left to right, if non-zero then set to that value
# and increate the count by 1
# after reaching the end of the array
# set the rest of array to 0 while increase the count

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < n:
        nums[count] = 0
        count +=1