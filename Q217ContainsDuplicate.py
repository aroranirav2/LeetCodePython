class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
    
    print(containsDuplicate([1,2,3,1]))