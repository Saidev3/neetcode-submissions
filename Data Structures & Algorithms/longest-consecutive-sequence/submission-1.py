class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        for num in nums:
            curr_seq = 0
            while num in nums:
                curr_seq += 1
                num += 1
            if curr_seq > max_seq:
                max_seq = curr_seq
        return max_seq
