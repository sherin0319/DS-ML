
print("SHERIN MATHEW")
print("21MCA039")
a = []
number = int(input("Please Enter the Total Elements :"))
for i in range(number):
 value = int(input("Please enter the %d Item : " %i))
a.append(value)
for i in range(number -1):
 for j in range(number - i - 1):
   if(a[j]>a[j+1]):
      temp = a[j]
a[j] = a[j + 1]
a[j + 1] = temp
print("The Result in Ascending Order :", a)