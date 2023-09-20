"""
Two Sum
----------------
https://leetcode.com/problems/two-sum/
"""


def twoSum(nums: list[int], target: int) -> list[int]:
	# for idx, val in enumerate(nums):
	# 	for idx2, val2 in enumerate(nums):
	# 		if idx == idx2:
	# 			continue
	# 		if val + val2 == target:
	# 			return [idx, idx2]
	dict = {}
	for idx, val in enumerate(nums):
		if val in dict:
			return [dict[val],idx]
		else:
			dict[target-val] = idx

if __name__ == '__main__':
	nums = [2,5,5,11]
	target = 10
	print(twoSum(nums, target))

