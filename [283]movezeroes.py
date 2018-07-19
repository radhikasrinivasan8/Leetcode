class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anytls
        hing, modify nums in-place instead.
        """
        count = 0
        for i in range(0,len(nums)):
            if 0 in nums:
                nums.remove(0)
                count = count + 1
                #print(count)

        while count > 0:
            #nums.remove(0)
            nums.append(0)
            count = count - 1
        #print(nums)
        

        


if __name__=='__main__':
    
    numsa=[1,0,0,2,3,0]
    print(numsa)
    #numsa.remove(0)
    s = Solution()
    a=s.moveZeroes(numsa)
    #print(numsa)
