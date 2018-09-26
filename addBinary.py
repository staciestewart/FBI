class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # max value among a & b        
        m = max(len(a), len(b))
        print("There are %s character in the binary number"%(m))
        
        # initialize result
        result = ''
        
        # fill zero into a or b
        a = a.zfill(m)
        b = b.zfill(m)
        print(a, b)
        
        # carry value in binary sum
        carry = 0 
        
        # adding value from right to left with range(start, stop, step) like how we would do it using pen and paper
        for i in range(m-1, -1, -1):
            t = carry
            t += 1 if a[i] == '1' else 0
            t += 1 if b[i] == '1' else 0
            carry = 0 if t < 2 else 1
            result = ('1' if t % 2 == 1 else '0') + result
        
        # add addtional digit to binary of carry > 0
        if carry != 0:
            result = '1' + result
        
        return result.zfill(m)
            
            
        
        
        
        
        