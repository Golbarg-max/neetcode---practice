class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []
        for i in nums:
            if i not in duplicate:
                duplicate.append(i)
            else:
                return True
        return False
