"""
Given a list of numbers and a number k, return whether any two
numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def sum2(lst, k):
	n = len(lst)
	if n < 2:
		return False
	for i in range(n):
		if k - lst[i] in lst[i+1:]:
			return True
	return False


if __name__ == '__main__':
	tests = [[10, 15, 3, 7],
			 [2, 3],
			]
	ks = [17,
		  10,
		 ]
	answers = [True,
			   False,
			  ]
	for test, k, answer in zip(tests, ks, answers):
		actual = sum2(test, k)
		message = "Failed test {0}\n got {1}" \
		          "expected {2}".format(test, actual, answer)
		assert actual == answer, message
