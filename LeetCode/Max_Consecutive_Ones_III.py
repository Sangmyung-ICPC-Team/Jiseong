class Solution(object):
    def longestOnes(self, nums, k):
        start, result = 0, 0

        for end, n in enumerate(nums):
            k -= (1-n)
            if k < 0:
                k += (1-nums[start])
                start += 1
            result = max(result, (end - start + 1))

        return result  
       
print(Solution.longestOnes(0,[1,1,1,0,0,0,1,1,1,1,0], 2))
