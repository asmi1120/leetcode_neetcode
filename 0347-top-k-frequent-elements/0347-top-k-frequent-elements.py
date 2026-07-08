class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        arr = sorted(s, key=s.get, reverse=True)
        return arr[:k]