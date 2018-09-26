class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        let c1:Int = a.count
        let c2:Int = b.count
        let m:Int = [c1, c2].max()!
        var A = String(repeating: "0", count: m-c1) + a
        var B = String(repeating: "0", count: m-c2) + b
        var carry = 0
        var result = ""  
        for i in (0...m-1).reversed() {
            var total = carry
            let index = A.index(A.startIndex, offsetBy: i)
            print(A[index])
            print(B[index])
            if A[index] == "1" {
                total = total + 1
            } else {
                total = total + 0
            }
            if B[index] == "1" {
                total = total + 1
            } else {
                total = total + 0
            }
            if total < 2 { 
                carry = 0 
            } else {
                carry = 1
            }
            if total%2 == 1 { result = "1" + result } else { result = "0" + result}
        }
        // add additional 1 for larger value
        if carry != 0 { 
            result = "1" + result 
        } 
        return result
    }
}

