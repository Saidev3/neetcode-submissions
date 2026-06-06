class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        ans = []
        pre = 1
        suf = 1
        for i in range(len(nums)):
            prefix[i]=pre
            pre *= nums[i]
            suffix[len(nums)-i-1] = suf
            suf *= nums[len(nums)-i-1]
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 6,1]


        # [-1,0,1,2,3]
        # [1, -1, 0, 0,0]
        # [0,6,6,3,1]
        # [0, -6, 0, 0, 0]