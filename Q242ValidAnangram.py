class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sortedS = sorted(s)
        sortedT = sorted(t)
        for x in range(len(s)):
            if(sortedS[x] != sortedT[x]):
                return False
        return True
    
    print(isAnagram("anagram", "nagaram"))