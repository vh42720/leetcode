"""
Group Anagrams
----------------
https://leetcode.com/problems/group-anagrams/
"""


def groupAnagrams(strs: list[str]) -> list[list[str]]:
	dict = {}
	for str in strs:
		sorted_str = ''.join(sorted(str))
		if sorted_str in dict:
			dict[sorted_str].append(str)
		else:
			dict[sorted_str] = [str]

	return list(dict.values())


if __name__ == '__main__':
	str = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(groupAnagrams(str))
