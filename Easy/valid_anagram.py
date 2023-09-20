"""
Valid Anagram
----------------
https://leetcode.com/problems/valid-anagram/
"""

from collections import Counter


def isAnagram(s: str, t: str) -> bool:
	return Counter(s) == Counter(t)


if __name__ == '__main__':
	s = 'rat'
	t = 'car'
	s1 = 'anagram'
	t1 = 'nagaram'
	print(isAnagram(s, t))
	print(isAnagram(s1, t1))
