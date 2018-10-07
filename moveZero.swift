// Challenge: 
// Given an array nums, write a function to move all 0's to 
// the end of it while maintaining the relative order of the 
// non-zero elements.

func moveZeroes(_ nums: inout [Int]) {
    var count = 0
    var n = nums.count
    for i in 0..<n {
        if nums[i] != 0 {
            nums[count] = nums[i]
            count = count + 1
        }
    }
    while count < n {
        nums[count] = 0
        count = count + 1
    }
}