class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        we need to get the sum of each element pair in the array.
        Then, we get the remainder after division by 10, and create a new array
        Do this until the array is exhausted
        [1,2,3,4,5]
         [3,5,7,9]
          [8,2,6]
           [0,8]
            [8]
        '''
        def calculate_array_sum(nums: List[int]):
            # recursive method to get the sum of the array elements in a triangular sum
            new_array = []
            for i in range(len(nums) - 1):                            
                new_array.append((nums[i] + nums[i + 1]) % 10)
                
            if len(new_array) == 1:
                return new_array[0]
            else:
                return calculate_array_sum(new_array)                 

        if len(nums) == 1:
            return nums[0]
        else:
            return calculate_array_sum(nums)    
        
        
