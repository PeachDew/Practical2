# 10 (Finding the largest n such that n​3​< 12000) ​q10_find_largest.py
# Use a while loop to find the largest integer n such that n
# 3 is less than 12,000.

n = 1
while pow(n, 3) < 11999:
    n = n + 1

if pow(n, 3) > 12000:
    n = n - 1

print(n)
