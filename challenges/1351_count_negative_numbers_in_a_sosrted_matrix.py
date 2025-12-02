"""1351. Count Negative Numbers in a Sorted Matrix
Solved
Easy
Topics
conpanies icon
Companies
Hint
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for mtx in grid:
            left, right = 0, len(mtx) - 1
            while left <= right:
                mid = (left + right) // 2
                if mtx[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += len(mtx) - left

        return count
