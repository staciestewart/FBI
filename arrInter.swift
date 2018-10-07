// Given two arrays, write a function to compute their intersection.

class Solution {
    func intersect(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        // Counting length of each input arrays
        let l1 = nums1.count
        let l2 = nums2.count
        
        // Create an Empty Intersection Array
        var intersection: [Int] = []
        
        // Sorting input arrays
        var a1 = nums1.sorted()
        var a2 = nums2.sorted()
        
        // Create counter for each arrays
        var c1 = 0, c2 = 0
        
        // Iterate over the array
        while c1 < l1 && c2 < l2 {
            if a1[c1] < a2[c2] {
                c1 += 1
            } else if a1[c1] > a2[c2] {
                c2 += 1
            } else {
                intersection.append(a1[c1])
                c1 += 1
                c2 += 1
            }
        }
        
        // When there is a common number in the array then add the number into the array
        return intersection
    }
}