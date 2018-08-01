"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

"""
we will use algorith from the family of reservoir sampling algorithms:
https://en.wikipedia.org/wiki/Reservoir_sampling
"""

"""
given on the information on the Internet we will assume
that there is an object called stream that has method hasnext()
that can give us information if there any objects left in the stream
also we will assume that current element in stream can be obtained with
the method read()
"""

from random import random

stream = someStream

i = 0

while True:
	tmp = stream.read()
	i += 1
	x = random()
	if random() < 1/i:
		res = tmp
	if not stream.hasnext():
		break

print(res)