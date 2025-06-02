''' 
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dictionary
        items = {}
        
        #go over every item in the provided list
        for i in range(len(nums)):
            if items.get(nums[i]) is None:
                # add a new item
                items[nums[i]] = 1
                print (items[nums[i]])
            else:
                # already existing item in the dictionary
                # Every item appears exactly twice, at most, per description
                items[nums[i]] = 2
        # return the only index with 1 in value
        for i in range(len(nums)):
            if items.get(nums[i]) == 1:
                return nums[i]
                
