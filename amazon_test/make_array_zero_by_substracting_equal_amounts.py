class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # we need to select the smallest element x of the array
        # then, we can reduce each element of the array to the same element x
        # after doing that, we have to repeat the steps for each unique element of the array
        # But! In reality, we only care about this: "How many distinct non-zero elements are there in an array?"
        # let's create a hashset and get the number, it should be the answer to our question
        distinct_elements = set()
        count_of_elements = 0

        for element in nums:
            if element not in distinct_elements and element != 0:
                distinct_elements.add(element)
                count_of_elements += 1

        return count_of_elements        



        
