class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d = Counter(s1)
        for i in range(len(s1)):
            d[s2[i]] -= 1
            if d[s2[i]] == 0:
                del d[s2[i]]
                
        if not d:
            return True
        for i in range(len(s1), len(s2)):
            char_in = s2[i]
            char_out = s2[i - len(s1)]
            d[char_in] -= 1
            if d[char_in] == 0:
                del d[char_in]
            d[char_out] += 1
            if d[char_out] == 0:
                del d[char_out]
            if not d:
                return True
                
        return False