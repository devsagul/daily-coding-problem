"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def longest_k(s, k):
	res = s[:k]
	l_res = k
	cur = res
	letters = set(cur)
	num_letters = len(letters)
	s_size = len(s)

	i = k
	while i < len(s):
		letter = s[i]
		if letter not in letters and num_letters >= k:
			letters.remove(cur[0])
			cur = cur.lstrip(cur[0])
		else:
			num_letters += 1
		letters.update(letter)

		tmp = s[i:].lstrip(letter)
		chunk_size = s_size - i - len(tmp)
		cur += chunk_size * letter
		i += chunk_size
		l_cur = len(cur)
		if l_cur > l_res:
			l_res = l_cur
			res = cur
	return res

if __name__ == '__main__':
	tests = [["abcba", 2],
			 ["contains", 4],
			]
	answers = ["bcb",
			   "ntain",
			  ]

	for test, answer in zip(tests, answers):
		actual = longest_k(*test)
		message = "Failed test {0}\ngot {1}" \
				  " expected {2}".format(test, actual, answer)
		assert actual == answer, message