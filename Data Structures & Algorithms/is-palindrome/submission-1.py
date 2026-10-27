class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        s = s.lower()
        s = s.replace(" ", "")

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not (ord('a') <= ord(s[l]) <= ord('z') or
                ord('0') <= ord(s[l]) <= ord('9')):
                    l += 1
            while r > l and not (ord('a') <= ord(s[r]) <= ord('z') or
                ord('0') <= ord(s[r]) <= ord('9')):
                    r -= 1

            if ord(s[l]) != ord(s[r]):
                return False
            else:
                l += 1
                r -= 1
        return True