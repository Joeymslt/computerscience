#character = "A"
#ascii = ord(character)
#print(type(ascii))
#print("The decimal value for letter A is:" ,ascii)

#output = chr(ascii)
#print(type(output))
#print("The character represented by decimal value", ascii , "is:", output)

#character = input("Enter a letter A-Z:")
#key = int(input("Enter an number 1-9:"))
#ascii= ord(character)
#encLetter = chr(ascii+key)
#print ("The Encrypted Letter is: ", encLetter)

string1 = "Hello"
length = len(string1)
print (length)
print(type(length))

myWord = "Hello"
myWord = myWord.upper()
print (myWord)

myNotWord = "HELLO"
myNotWord = myNotWord.lower()
print (myNotWord)

myIsWord = "Hello"
myIsWord = myIsWord.count("l")
print (myIsWord)

myAllWord = "Hello"
myAllWord = myAllWord.isalpha()
print (myAllWord)
