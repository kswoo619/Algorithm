from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)

        values = list(cnt.values())
        mx = max(values)
        
        return values.count(mx) * mx