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

