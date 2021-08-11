# Basic loop study

n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')   
    
# Definite Loops

friends = ['Daniela','Micaela','Ricardo','Kellen']
for friend in friends:
    print ('Happy New Year: ', friend)
print('Done!')

# Another type of loop:

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Counting a loop

Count = 0
print('Before', Count)
for thing in [9, 41, 12, 3, 74, 15] :
    Count = Count + 1
    print(Count, thing)
print('After', Count)

# Sum of all the numbers in the list

Count = 0
print('Before', Count)
for thing in [9, 41, 12, 3, 74,15] :
    Count = Count + thing
    print(Count, thing)
print('After', Count)

# Finding the avarage in a loop

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)