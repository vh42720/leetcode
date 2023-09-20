"""
Contains Duplicate
----------------
https://leetcode.com/problems/contains-duplicate/
"""


def containsDuplicate(nums: list[int]) -> bool:
	return len(set(nums)) != len(nums)


if __name__ == '__main__':
	inputs = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
	print(containsDuplicate(inputs))
