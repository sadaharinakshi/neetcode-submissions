class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}

        for i in range(len(nums)):
            targ=target-nums[i]

            if targ in hm:
                return [hm[targ],i]
            else:
                hm[nums[i]]=i
        