class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        pre = 1
        suf = 1
        #[1, 1, 12, 1]
        for i in range(len(nums)):
            ans[i]= ans[i] * pre
            pre *= nums[i]      # 1, 2, 8
            ans[len(nums)-i-1] =  ans[len(nums)-i-1] * suf
            suf *= nums[len(nums)-i-1]     # 6, 24
        print(ans)

        return ans
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 6,1]


        # [-1,0,1,2,3]
        # [1, -1, 0, 0,0]
        # [0,6,6,3,1]
        # [0, -6, 0, 0, 0]