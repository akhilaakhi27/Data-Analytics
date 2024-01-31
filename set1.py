a={1,2,3,4,5,6,7,8,9,10}
b={2,4,6,8,10}
c={1,3,5,7,9}
d={1,3,2,4,5}

print(len(a))

a.add(11)
print(a)

for i in b:
    print(i)

c.update(d)
print(c)

c.remove(5)
print(c)

c.discard(9)
print(c)

set1=a.union(b)
print(set1)

set2=b.intersection(a)
print(set2)

set3=b.intersection_update(a)
print(set3)

set4=a.difference(b)
print(set4)

set5=a.issuperset(b)
print(set5)

set6=b.issubset(a)
print(set6)


