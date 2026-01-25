class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        product1 = 1
        product2 = 1
        zero_count = nums.count(0)
        for i in nums:
            if zero_count == 1:
                if i != 0:
                    product1 *= i
            elif zero_count > 1:
                product1 = 0
            else:
                product *= i
        for j in nums:
            if zero_count > 0:
                if j == 0:
                    res.append(product1)
                else:
                    res.append(0)
            else:
                res.append(int(product/j))
        return res

# optimal solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
