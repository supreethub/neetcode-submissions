class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in pmap:
                if stack and stack[-1] == pmap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if stack:
            return False
        return True