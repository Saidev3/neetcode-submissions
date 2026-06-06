class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        pre = 1
        suf = 1
        for i in range(len(nums)):
            ans[i]= ans[i] * pre
            pre *= nums[i]
            ans[len(nums)-i-1] =  ans[len(nums)-i-1] * suf
            suf *= nums[len(nums)-i-1]
        print(ans)

        return ans