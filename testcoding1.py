d = {'X':9, 'Z':1, 'Y':5}
print(sorted(d))

d = {i: i*i for i in range(10)}
print(d)

import collections
b=collections.Counter([2,2,3,4,4,4])
b.most_common(1)
a=collections.Counter([2,2,3,3,3,4])
b=collections.Counter([2,2,3,4,4])
print(a|b)