"""
1146. Snapshot Array
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
"""


class SnapshotArray:

    def __init__(self, length: int):
        # stores only history of each index
        # in the format of (snap_id,value)
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # two cases
        ## 1) if snap_id exist, replace it
        if self.array[index][-1][0] == self.snap_id:
            self.array[index][-1] = (self.snap_id, val)
        ## 2) else (new snap), append the list at that index
        else:
            self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # looking at the list inside requested index
        arr = self.array[index]

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return arr[right][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
