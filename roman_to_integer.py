"""
Roman to Integer
----------------
https://leetcode.com/problems/roman-to-integer/
"""

roman_dict = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}


def romanToInt(s: str) -> int:
	if s is None or len(s) < 1 or len(s) > 15:
		raise RuntimeError('String length must be between 1 and 15')
	if dif := [x for x in s if x not in ('I', 'V', 'X', 'L', 'C', 'D', 'M')]:
		raise RuntimeError(f'Invalid Roman numbers: {dif}')

	num_list = []
	for idx, char in enumerate(s):

		num_list.append(roman_dict.get(char))

		last_char = char if idx == 0 else s[idx - 1]
		current_char = char

		if roman_dict[last_char] < roman_dict[current_char]:
			num_list[idx - 1] *= -1

	return int(sum(num_list))
	# return num_list


if __name__ == '__main__':
	inputs = ['III', 'LVIII', 'MCMXCIV']
	outputs = [3, 25, 1994]

	for roman_str in inputs:
		print(romanToInt(roman_str))
