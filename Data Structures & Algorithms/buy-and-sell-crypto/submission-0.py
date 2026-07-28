class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        mini=float("inf")
        res=0
        n=len(nums)
        for i in range(n):
            mini=min(mini,nums[i])
            res=max(res,nums[i]-mini)
        return res