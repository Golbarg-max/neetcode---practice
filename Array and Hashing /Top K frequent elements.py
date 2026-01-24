class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        freqKey = []
        for num, cnt in count.items():
            freqKey.append([cnt, num])
        freqKey.sort()
        res = []
        while len(res) < k:
            res.append(freqKey.pop()[1])
        return res
