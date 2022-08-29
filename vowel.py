print("SHERIN MATHEW")
print("21MCA039")

a = input("Enter a string: ")
a = a.casefold()
count = {x:sum([1 for char in a if char == x]) for x in 'aeiou'}
print(count)