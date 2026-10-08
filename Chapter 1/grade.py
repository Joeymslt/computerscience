#Question 16 (a)
#Examination Number:

def get_grade(result):
    grade = "Unsuccessful"
    
    if result >= 80:
        grade = "Distinction"
    elif result >= 65:
        grade = "Upper Merit"
        
    return grade

#Calculate and display the mean of a list of results
results = [39,32,62,88,51,62,64,81,77] # Initialise the list
N = len(results) #Initialise N to the number of results
total = 0 # Initialise the runnning to total to 0

#Loop N time
for i in range(N):
    total = total + results[i] #Running total
    
#Divide by the total number of results to give the mean
arithmetic_mean = total/9

#Display the answer
print("The mean percentage mark is",arithmetic_mean)

#(i) Round the mean percentage to two decimal places
print (round(arithmetic_mean,2))

#(ii) Modify the code so it divides the total by the number of elements
arithmetic_mean2 = total/N
print(round(arithmetic_mean2,2))

#(iii) Variable grades
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
    elif result < 40:
        grade = "Unsuccesful"
        
    return grade
print(round(arithmetic_mean,2))

#(iv) Print the grade result
print("The mean percentage mark is",arithmetic_mean)
print("The grade for the average result it", )
