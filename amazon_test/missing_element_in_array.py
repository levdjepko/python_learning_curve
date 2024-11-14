def find_missing(nums):
  
    # we can find a missing one number by using the principles of algebra
    # i.e. the sum of all the elements in a consecutive array should equal to n(n-1)/2
    n = len(nums) + 1
    expected_sum = int((n * (n + 1)) / 2)
    actual_sum =sum(nums)
    
    return expected_sum - actual_sum
