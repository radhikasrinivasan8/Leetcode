import os

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        s = ''.join(map(str,digits))
        s = int(s) + 1
        k = [int(i) for i in str(s)]
        return k
        

    
if __name__=='__main__':
    x = [1,2,3]
    print(x)
    s = Solution()
    a=s.plusOne(x)
    #print(a)

    
