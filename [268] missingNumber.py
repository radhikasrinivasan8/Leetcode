class Solution:

    """
    class Solution:
    
    def missingNumber(self, nums):
       
        print(len(nums))
        
        if len(nums)%2 == 0:
            size = len(nums)/2
            
        else:
            size = (len(nums)+1)//2
        
        #print(size)
        
        
        for i in range(0, len(nums)):    
            if i in range(0, size):
                nums.remove(i)
            elif i in range (size +1, len(nums)):
                nums.remove(i)
            else:
                return i
        """
    def missingNumber(self, nums):
    
        nums.sort()
        print(nums)

        if nums[0] != 0 :
            return 0
        elif nums[len(nums) -1]!= len(nums):
            return len(nums)
        
        for i in range(1, len(nums)+1):
            cornum = nums[i-1] +1
            #print(cornum)
            #print(i)
            if nums[i] != cornum:
                #print(nums[i])
                return cornum

    
        
if __name__ == '__main__':
    x = [3,0,1]
    #print(x)
    s = Solution()
    a = s.missingNumber(x)
    print(a)


            