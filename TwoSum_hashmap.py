'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices in `nums` whose values add up to `target`.

        Args:
            nums (List[int]): List of integers.
            target (int): Target sum.

        Returns:
            List[int]: A list [i, j] of the two indices such that nums[i] + nums[j] == target.

        Complexity:
            Time: O(n) average, Space: O(n).
        """
        nums_hash = {}
        for i in range(len(nums)):
            if target- nums[i] in nums_hash:
                return[nums_hash[target- nums[i]] , i]
            else:
                nums_hash[nums[i]] = i 