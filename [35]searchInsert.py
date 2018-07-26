class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        k = len(nums)
        


        

        if target > nums[k-1]:
            ret = k
        elif target <= nums[0]:
            ret = 0
        else:
            while target<= nums[k-1]:
                k = k-1
                ret = k
        return ret





    
if __name__ == '__main__':
    x = [1]
    tgt = 1
    #print(x)
    s = Solution()
    a = s.searchInsert(x,tgt)
    print(a)
