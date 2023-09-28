class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in dictionary.keys()):
                return [dictionary[complement], i]
            dictionary[nums[i]] = i
        raise ValueError("combination not found")
    
    output = twoSum([2, 4, 5, 7, 11], 9)

    print(output)