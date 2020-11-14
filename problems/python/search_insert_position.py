from typing import List


class Solution:
    def searchInsert(_, nums: List[int], target: int) -> int:
        '''Assume nums are sorted in ascending order
           return targets index if the target is in the array
           or return where it would be in the array if it were to be inserted
        '''
        try:
            ind = nums.index(target)
            return ind
        except:
            for index, num in enumerate(nums):
                if target < num:
                    return index

        return len(nums)

    def searchInsert2(_, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if target <= num:
                return index

        return len(nums)


def check_solution():
    solution = Solution()
    assert solution.searchInsert2([1, 2, 3], 4) == 3
    assert solution.searchInsert2([5, 10, 15, 25, 40], 35) == 4
    assert solution.searchInsert2([1, 2, 3, 4, 5], 2) == 1
    print("Correct!")


check_solution()
