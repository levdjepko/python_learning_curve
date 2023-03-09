    def runningSum(self, nums: List[int]) -> List[int]:
        # declare a new List to return it.
        return_list = []
        for i in range(len(nums)): # for loop with i as an iterator
            return_list.append(nums[i] + sum(nums[0:i]))
        return return_list    
    
