class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            count = [0] * 26 # char count of each string

            for char in st:
                count[ord(char) - ord("a")] += 1
            
            res[tuple(count)].append(st) # tuple because immutable bject
            
        return list(res.values())