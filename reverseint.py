class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        neg_limit= -0x80000000
        pos_limit= 0x7fffffff

        if x>0 :
            
            y = ([int(i) for i in str(x)])
            z = (y[::-1])
            w = ''.join(map(str,z))
            w = int(w)
            val1 = w & pos_limit
            
            if val1 == w :
                return w
            else: 
                return 0
            
        else:
            x = abs(x)
            y = ([int(i) for i in str(x)])
            z = (y[::-1])
            w = ''.join(map(str,z))
            w = - int(w)
            
            val2 = w & neg_limit
            if val2 == neg_limit:
                return w
            else: 
                return 0