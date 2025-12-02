"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


class Solution:
    def binarySearch(self, nums: List[int], target: int, left: int, right: int):

        if left > right:
            return -1

        if len(nums) == 0:
            return left if nums[left] == target else -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        if len(nums) == 0:
            return [-1, -1]

        mid = self.binarySearch(nums, target, left, right)

        if mid < 0:
            return [-1, -1]

        midL, midR = mid, mid
        lo, hi = midL, midR
        while midL > -1 or midR > -1:
            midL = self.binarySearch(nums, target, left, midL - 1)
            midR = self.binarySearch(nums, target, midR + 1, right)
            if midL > -1:
                lo = midL
            if midR > -1:
                hi = midR
        return [lo, hi]
