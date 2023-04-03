
import random
def gnt_tuple(start, end, size):
    return tuple(random.randint(start, end) for _ in range(size))
t1 = gnt_tuple(0, 5, 10)
t2 = gnt_tuple(-5, 0, 10)
t3 = t1 + t2
cnt_zeros = t3.count(0)
print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("Count of zeros in t3:", cnt_zeros)