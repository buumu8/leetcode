# Binary Search

- Time: O(logn)
- sorted array

## Binary Search

```python
left,right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

## Smallest Greater Than Target

```python
left,right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid - 1
return nums[left]
```

## Rotated Array

- one side must always be sorted

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return target
    elif nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
return -1
```

## Min in rotated array

```python
left, right = 0, len(nums) -1
while left < right:
    mid = (left + right) // 2
    if nums[right] <= nums[mid]:
        left = mid + 1
    else:
        right = mid
return nums[left]
```

## Flatten a 2D matrix

```python
rows = len(matrix)
columns = len(matrix[0])

row = index // columns
col = index % columns
```

## Array of unknown size

```python
while valueOf(right) < target:
    left = right
    right *= 2
```

### Perfect divide an array

```python
    left,right = 0, length(nums) - 1
    while left<right:
        length = right - left + 1
        mid = (left + right) // 2
        if length % 2 == 0:
            c = compare(left,mid,mid+1,right)
        else:
            c = compare(left,mid-1,mid+1,right)
```

### LIS with tails

```python
def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num
        return len(tails)

```
