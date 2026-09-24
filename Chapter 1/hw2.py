myString = "Frank Lampey"
print(myString)
myStringList = list(myString)
print(myStringList)

print(type(myString))
print(type(myStringList))

myStringList = ['F','r','a','n','k',' ','L','a','m','p','e','y']

print(myStringList[1])
print(myStringList[3])
print(myStringList[6])

print(myStringList[2:8])

if 'a' in ['t', 'e', 'a', 'c', 'u', 'p']:
  print("It is in the list.")
myCars = ['Fiat', 'Honda', 'Toyota', 'BMW']
print("Enter a make of car: ")
carName = input()
if carName not in myCars:
print("We do not stock", carName)
else:
print("Yes, we stock," carName)

myList = [1, 19, 27, 8, 5, 9]
print(myList)
