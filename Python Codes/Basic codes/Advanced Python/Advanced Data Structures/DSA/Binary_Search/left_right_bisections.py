from typing import List


def binary_search_left(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search_right(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right


# left_index = binary_search_left(nums, target)
# right_index = binary_search_right(nums, target)

# if left_index <= right_index:
#     result = list(range(left_index, right_index + 1))
