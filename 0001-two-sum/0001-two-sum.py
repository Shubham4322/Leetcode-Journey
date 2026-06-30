class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        d ={}
        for j in nums:
            if target - j in d:
                return [d[target-j],i]
            else:
                d[j]=i
            i+=1





        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]