class Solution:
    def isValid(s: str) -> bool:
        stack = []
        map = {}
        map["["] = "]"
        map["("] = ")"
        map["{"] = "}"

        for c in s:
            if c in map.keys():
                stack.append(map[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
        
        return len(stack) == 0
    
    print(isValid("{}"))
