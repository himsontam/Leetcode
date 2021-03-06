#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum 
# https://leetcode.com/problems/two-sum/description/
# 
# Given an array of integers nums and an integer target, return indices of the two numbers # such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the # same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Solution 1
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target - num], i])
                break 
            hash_table[num] = i
        return([])
        
        # Solution 2
        # k = 0
        # for i in nums:
        #     k += 1
        #     if target - i in nums[k:]:
        #         return(k - 1, nums[k:].index(target - i) + k)
# @lc code=end

# Online Solution
# https://medium.com/@havbgbg68/leetcode-1-two-sum-python-8d77c223abd3
# https://leetcode.com/problems/two-sum/discuss/?currentPage=1&orderBy=most_relevant&query=python
