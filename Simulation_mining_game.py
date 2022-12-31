# a: blocks mined in advance by the attacker
# h: blocks mined in advance by the bank
# n: number of remaining actions

import functools

a = 0
h = 0
n = 400
@functools.cache
def E (a, h, n, q, c): 
    if n == 0:
        return 0

    if a > h:
        return max(((h+1) - c + E(a-h-1, 0, n-1, q, c)),
                    (q * E(a+1, h, n-1, q, c) + (1-q) * (E(a, h+1, n-1, q, c) - c)))

    if a <= h:
        return max(E(0, 0, n-1, q, c),
                    (q * E(a+1, h, n-1, q, c) + (1-q) * (E(a, h +1, n-1, q, c) - c)))


q4 = 0.10 # unprofitable threshold
q3 = 0.20 # sunprofitable threshold
q = 0.3293929 # minimum limit
q1 = 0.40 # profitable threshold
q2 = 0.50 # profitable threshold
print(E(a, h, n, q, q))
print(E(a, h, n, q1, q1))
print(E(a, h, n, q2, q2))
print(E(a, h, n, q3, q3))
print(E(a, h, n, q4, q4))