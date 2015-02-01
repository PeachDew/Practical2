# 9 (Finding the smallest n such that n​2​> 12000) ​q09_find_smallest.py
# Use a while loop to find the smallest integer n such that n
# 2 is greater than 12,000.

n = 1
while pow(n, 2) < 12000:
    n = n + 1

print(n)
