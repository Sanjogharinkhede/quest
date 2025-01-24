names=[i**2 if i%2==0 else i for i in range(20) ]
print(names)

q=['apple','banana','cherry']
print([x.upper() for x in q])

st="some VALue is There"
print([x for x in st if x.lower() in ['a','e','i','o','u']])


celsius=[15,17,26,77,4,38]
fa=[(x*1.8)+32 for x in celsius]
print(fa)

# An iterator is an object that can be iterated upon,
# meaning that you can traverse through all the values.
#__iter__(): returns the iterator object
#__next__(): return next object in the sequence

iterator=iter(celsius)
print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))