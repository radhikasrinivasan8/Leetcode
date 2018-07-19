class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        while val in nums:
            nums.remove(val)
        
        return len(nums)
    
if __name__== "__main__":
    nums = [0,0,0,1,2,4]
    val = 4
    print(nums)
    print(val)
    a= Solution()
    b = a.removeElement(nums,val)
    print(b)
