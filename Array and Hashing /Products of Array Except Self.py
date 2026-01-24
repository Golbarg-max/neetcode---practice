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
