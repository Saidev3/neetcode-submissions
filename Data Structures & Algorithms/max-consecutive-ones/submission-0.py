class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_sequence = 0
        maximum_sequence = 0
        for num in nums:
            if num == 1:
                current_sequence += 1
                if current_sequence > maximum_sequence:
                    maximum_sequence = current_sequence
            else:
                current_sequence = 0
        return maximum_sequence
