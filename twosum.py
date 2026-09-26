def twosum(nums, target):
    seen = {}
    for ix, value in enumerate(nums):
        if target - value in seen:
            return [seen[target-value], ix]
        seen[value] = ix
    return []


