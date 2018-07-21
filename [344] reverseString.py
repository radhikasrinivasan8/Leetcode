class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

    #for i in len(s):
        strrev = s[::-1]
        return strrev

if __name__ == '__main__':
    x = "hello world"
    s = Solution()
    a= s.reverseString(x)
    print(a)
        