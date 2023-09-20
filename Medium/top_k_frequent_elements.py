"""
Top K Frequent Elements
----------------
https://leetcode.com/problems/top-k-frequent-elements/
"""
from collections import Counter
import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
	# return [num[0] for num in Counter(nums).most_common(k)]
	# sorted_dict = dict(sorted(Counter(nums).items(), key=lambda item: item[1]))
	# return sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)
	# return list(sorted_dict.values())[:k]

	# heap solution
	freq = Counter(nums)
	heap = [(freq[num], num) for num in nums]
	return [val for val, _ in freq.most_common(k)]

if __name__ == '__main__':
	nums = [1,1,1,2,2,3]
	# nums = [-1,-1]
	k = 2
	print(topKFrequent(nums, k))


# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# 	sorted_dict = dict(sorted(Counter(nums).items(), key=lambda item: item[1]))
# 	return list(sorted_dict.values())[:k]
