def productExceptSelf(self, nums: list[int]) -> list[int]:
    """
    Given an integer array nums, return an array answer 
    such that answer[i] is equal to the product of all 
    the elements of nums except nums[i].
    The product of any prefix or suffix of nums is 
    guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs 
    in O(n) time and without using the division operation.
    """
    answer = []
    frontrun = [1]
    backrun = [1]
    for i, v in enumerate(nums):
        frontrun.append(frontrun[-1]*v)
    for i, v in enumerate(reversed(nums)):
        backrun.append(backrun[-1]*v)
    frontrun = frontrun[:-1]
    backrun = backrun[:-1]
    backrun = backrun[::-1]
    for i, v in enumerate(nums):
        answer.append(int(frontrun[i]*backrun[i]))
    return answer