class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l=[]
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                l.append(nums[i]**2)
        return sum(l)
