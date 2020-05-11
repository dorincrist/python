#!/usr/bin/env python3

domain = [1, 2, 3, 4, 5]

# f(x) = x * 2
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))