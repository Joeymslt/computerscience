def get_grade(result):
    grade = "Unsuccessful"
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
    elif result >= 50:
        grade = "Lower Merit"
    elif result >= 40:
        grade = "Pass"
    else:
        grade = "Unsuccesful"
         return grade
results = [39, 32, 62, 88, 51, 62, 64, 81, 77]
N = len(results)
total = 0
for i in range(N):
    total = total+results[i] 
arithatic_mean = round(total/N, 2)
print("The mean percentage mark is", arithmatic_mean)
grade = get_grade(arithmatic_mean)
print("The grade for the average result is", grade)
highest = max(results)
lowest = min(results)
print("The lowest score is", lowest)
print("The highest score is", highest)
count1 = 0
count2 = 0 
for i in results:
    if i < 40:
        count1 += 1
    elif i >=50 and i <=79:
        count2 += 1
print("The number of scores below 40 is", count1)
print("The number of scores between 50 and 79 inclusive is", count2)
longest = []
current = [results[0]]
for i in range(1, N):
    if results[i] > results [i-1]:
        current.append(results[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [results[i]]   
if len(current) > len(longest):
    longest = current   
print("Longest run of result increase is", longest)
x = int(input("Enter how many numbers you would want to calculate: "))
numbers = [] 
for i in range(0,x):
    number = int(input("Enter a number: "))
    numbers.append(number) 
print("The initial list of values is:", numbers) 
if len(numbers) == 0: 
    print("Error, the list is empty. Cannot compute median") 
