'''
1099. Two Sum Less Than K

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 1000
1 <= k <= 2000
'''

# Binary Search Approach O(N log N)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < k:
                max_sum = max(max_sum,nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return max_sum

# Solution: Brute Force O(N^2)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = nums[i] + nums[j]
                if curr_sum < k:
                    max_sum = max(max_sum, curr_sum)
        return max_sum
    
# Solution: Dynamic Programming O(N^2)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        dp = [-1] * k
        n = len(nums)
        max_sum = -1

        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = nums[i] + nums[j]
                if curr_sum < k:
                    dp[curr_sum] = 1
                    max_sum = max(max_sum, curr_sum)
        return max_sum

# Solution: O(N) with Hash map
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        seen = set()
        max_sum = -1

        for num in nums:
            target = k - num
            for val in seen:
                if val < target:
                    max_sum = max(max_sum, val + num)
            seen.add(num)
        return max_sum
# Solution: Counting Sort O(N + M)
class Solution: 
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        count = [0] * 1001
        max_sum = -1

        for num in nums:
            count[num] += 1

        for i in range(1, 1001):
            if count[i] == 0:
                continue
            count[i] -= 1
            for j in range(min(1000, k - i - 1), 0, -1):
                if count[j] > 0:
                    max_sum = max(max_sum, i + j)
                    break
            count[i] += 1
        return max_sum