numbers = [7, 2, 3, 4, 9, 5, 6, 7, 89, 99, 1]

current_run = numbers[:1]
longest_run = numbers[:1]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current_run.append(numbers[i])
    else:
        current_run = [numbers[i]]

    if len(current_run) > len(longest_run):
        longest_run = current_run.copy()

print("Longest run:", longest_run)


'''
Understanding current_run and longest_run

Look at this list:

numbers = [7, 2, 3, 4, 9, 5, 6, 7, 89, 99, 1]

We are trying to find the longest run of numbers that keep increasing.

We start with:

current_run = numbers[:1]
longest_run = numbers[:1]

This gives:

current_run = [7]
longest_run = [7]

current_run stores the run we are checking right now.

longest_run stores the longest run we have found so far.

The loop checks each number:

for i in range(1, len(numbers)):

If the current number is bigger than the previous number:

if numbers[i] > numbers[i - 1]:
    current_run.append(numbers[i])

the number is added to current_run.

For example:

5
6
7
89
99

creates:

current_run = [5, 6, 7, 89, 99]

Because this is the longest run found so far, it is copied into:

longest_run = [5, 6, 7, 89, 99]

What happens when Python reaches the final 1?

Python checks:

if numbers[i] > numbers[i - 1]:

At this point this means:

if 1 > 99:

This is false.

So the else runs:

else:
    current_run = [numbers[i]]

The current number is 1, so:

current_run = [1]

Python then checks:

if len(current_run) > len(longest_run):

This is really checking:

if 1 > 5:

That is false, so longest_run does not change.

At the end:

current_run = [1]

longest_run = [5, 6, 7, 89, 99]

Therefore:

print("Longest run:", longest_run)

prints:

Longest run: [5, 6, 7, 89, 99]

Easy way to remember

current_run = the run we are checking now.

longest_run = the best run we have found so far.


current_run.copy() is the safer choice.
Without it:
longest_run = current_run
both variables can end up referring to the same list in memory.
'''



numbers = [7, 2, 3, 4, 9, 5, 6, 7, 45, 89, 1,12]
numbers.sort()
print(numbers)
listLen = int(len(numbers))

if listLen % 2 == 1:
    listMedian = numbers[int(listLen/2)]
    print("The list is odd so the median is: ",listMedian)
else:
    listMedian1 = numbers[int(listLen/2 + 1)]
    listMedian2 = numbers[int(listLen/2 - 1)]
    listMedian = (listMedian1 + listMedian2) / 2
    print("The list is even so the median is: ",listMedian)



