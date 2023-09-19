class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentPointer = 1       
        for i in range (1, len(nums)):
            # iterate from 1 to end, and check all the numbers, comparing them to previous ones
            if (nums[i] != nums[i-1]):
                #new number
                nums[currentPointer] = nums[i]
                currentPointer += 1
        return currentPointer        
