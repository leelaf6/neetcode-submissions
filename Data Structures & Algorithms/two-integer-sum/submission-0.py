class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            com=target-nums[i]
            if com in d:
                return [d[com],i]
            d[nums[i]]=i
        