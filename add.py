print("SHERIN MATHEW ")
print('21MCA039')
a = input('Enter elements of a list ')
b = a.split()
print('list: ', b)
for i in range(len(b)):
    b[i] = int(b[i])
print("Sum = ", sum(b))
