#numbers = []

#for i in range(5):
#    number = int(input("Enter a number: "))
#    numbers.append(number)

#for i in range(len(numbers)):
#    numbers[i] = numbers[i] + 1

#print(numbers)

#hours = [12, 7, 9, 9, 6, 8, 2]

#tHours = sum(hours)
#tMilk = tHours * 0.5

#print("Total hours at home:", tHours)
#print("Total milk consumed:", tMilk, "litres")

#cost = tMilk * 1.35

#print("Total milk consumed:", tMilk, "litres")
#print("Amount Stephen must pay: €", cost)

#rainfall = []

#for i in range(7):
#    amount = float(input("Enter rainfall for day " + str(i + 1) + " (cm): "))
#    rainfall.append(amount)

#total = 0

#for amount in rainfall:
#    total = total + amount

#print("Total rainfall for the week:", total, "cm")

#average = total / 7

#print("Average rainfall:", average, "cm")

#for i in range(7):
#    if rainfall[i] > 3.5:
#        print("Rainfall exceeded 3.5 cm on day", i + 1)

names = []
sales = []

number = int(input("Enter the number of salespeople: "))

for i in range(number):
    name = input("Enter salesperson name: ")
    sale = float(input("Enter sales amount (€): "))

    names.append(name)
    sales.append(sale)

print("\nSalesperson Details")
for i in range(number):
    print(names[i], "€", sales[i])

total = 0

for sale in sales:
    total = total + sale

maximum = max(sales)
minimum = min(sales)

average = total / number

print("\nTotal sales: €", round(total, 2))
print("Maximum sales: €", round(maximum, 2))
print("Minimum sales: €", round(minimum, 2))
print("Average sales: €", round(average, 2))
