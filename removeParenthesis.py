# Remove the minimum number of invalid parentheses in order to # # make the input string valid. Return all possible results.
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def removeInvalidParentheses(self, s):
   			level = {s}
    		while True:
        		valid = []
       		for s in level:
            	try:
                	eval('0,' + filter('()'.count, s).replace(')', '),'))
                	valid.append(s)
            	except:
                	pass
        	if valid:
            	return valid
        	level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}