class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in nums_set:
                longest = 0
                while num + longest in nums_set:
                    longest += 1
                ans = max(longest, ans)
        return ans
            