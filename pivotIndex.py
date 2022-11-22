def pivotIndex(self, nums: List[int]) -> int:
        # return the index of an element such as
        # the sum of elements 0...i-1 == i+1...n
        for i in range(len(nums)):
            left = sum(nums[0 : i]) # 0...i-1, doesn't include i
            right = sum(nums[i+1:]) # i+1 to the end of the array
            if left == right:
                return i
        return -1  
