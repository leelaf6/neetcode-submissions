class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        pre=[nums[0]]*n
        suf=[nums[-1]]*n
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        for i in range(n-2,-1,-1):
            suf[i]=max(suf[i+1],nums[i])
        res=0
        for i in range(n):
            res+=min(pre[i],suf[i])-nums[i]
        
        return res