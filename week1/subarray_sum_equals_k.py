def subarraySum(nums: list[int], k: int) -> int:
    # # brute force method: run through all possible subarrays size 1 to len(nums) left to right, find all that sum to k, increment counter
    # # save the sum of smaller-size subarrays to be used in calculating sums for larger subarrays that contains them

    # # brute force attempt (failed)
    # counter = 0
    # for i in range(1,len(nums)):
    #     for j, value in enumerate(nums):
    #         if sum(nums[j:j+i]) == k:
    #             counter += 1
    # return counter

    # after watching solution video
    res = 0
    current_sum = 0
    prefix_sums = {0:1}
    for num in nums:
        current_sum += num
        diff = current_sum - k
        res += prefix_sums.get(diff, 0)
        prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
    return res


print(subarraySum([1,2,3], 3))

# time complexity is O(n) because we are iterating through the list once, 
# and the operations inside the loop (dictionary lookups and updates) 
# are O(1) on average. 

# The space complexity is also O(n) in the worst case, 
# as we may store up to n different prefix sums in the dictionary.


# brute force method failed because 
# I didn't figure out how to get the correct subarray slices
# and gave up because I knew there was a better solution