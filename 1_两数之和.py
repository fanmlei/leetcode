class Solution:
    def twoSum(self, nums, target):
        for index, item in enumerate(nums):
            if target-item in nums and index != nums.index(target-item):
                return [index, nums.index(target-item)]
