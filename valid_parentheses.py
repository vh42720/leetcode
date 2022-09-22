"""
Valid Parentheses
-----------------
https://leetcode.com/problems/valid-parentheses/
"""


def matches(open, close):
	opens = '([{'
	closes = ')]}'
	return opens.index(open) == closes.index(close)


def isValid(s: str) -> bool:
	if dif := [x for x in s if x not in ('(', '[', '{', '}', ']', ')')]:
		raise RuntimeError(f'Invalid parentheses: {dif}')

	# store as stack
	stack = []

	balanced = True
	index = 0
	while index < len(s) and balanced:
		symbol = s[index]
		if symbol in '([{':
			stack.append(symbol)
		else:
			if not stack:
				balanced = False
			else:
				top = stack.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1

	if balanced and not stack:
		return True
	else:
		return False


if __name__ == '__main__':
	inputs = ['()', '()[]{}', '(]', '[']
	outputs = [True, True, False]
	for s in inputs:
		print(isValid(s))
