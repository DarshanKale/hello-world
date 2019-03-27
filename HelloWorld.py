a = [1,2,3]
b=[1,2,3]
language = 'Testing'

print (id(a))
print(id(b))


if True:
    print('Thanks for using ' + language)
elif a==b:
    print('The values are equal')
else:
    print('Whatever')