"""
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def exclusive_multiplication(lst):
	product = 1
	for item in lst:
		product *= item
	return [product / item for item in lst]

def exclusive_multiplocation_wo_division(lst):
	res = []
	for i in range(len(lst)):
		product = 1
		for j in range(len(lst)):
			if i != j:
				product *= lst[j]
		res.append(product)
	return res

if __name__ == '__main__':
	tests = [[1, 2, 3, 4, 5],
			 [3, 2, 1],
			]
	answers = [[120, 60, 40, 30, 24],
			   [2, 3, 6],
			  ]

	for test, answer in zip(tests, answers):
		actual = exclusive_multiplication(test)
		message = "Failed test {0}\ngot {1}" \
				  "expected {2}".format(test, actual, answer)
		assert actual == answer, message

	for test, answer in zip(tests, answers):
		actual = exclusive_multiplocation_wo_division(test)
		message = "Failed test {0}\ngot {1}" \
				  "expected {2}".format(test, actual, answer)
		assert actual == answer, message