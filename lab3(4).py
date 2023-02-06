
import random

# n=int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# for i in range(random.randint(1, n)):
#     print(i)
#     for i in range(n-1):
#         sum-=i
#     print(sum)


n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
for i in range(n - 1):
    sum -= int(input(random.randint(1, n)))
print(sum)
