import os

class Solution:
    def isPalindrome(self, x):
        """
        type x: int
        rtype: bool
        """
        if x < 0:
            rtype = False
        else:
            
            if x <10:
                rtype = True
            
            else:
                print(">>>")
                y = 0
                z = x
                while z > 0:
                    y=y*10 + z%10
                    z = z//10
                    print(y)
                print(z)
                if y==x:
                    print("@@@@@")
                    print(y)
                    print(x)
                    rtype = True
                else:
                    rtype = False


            

        return rtype
                
    
if __name__=='__main__':
    x = 121
    print(x)
    s = Solution()
    a=s.isPalindrome(x)
    print(a)

    
