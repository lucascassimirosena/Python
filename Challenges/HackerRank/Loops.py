# The provided code stub reads an integer, n , from STDIN. 
# #For all non-negative integers i<n, print i**2 .

n = int(input("Type a number: "))
for number in range(n):
    print(number**2)

# First we scan the input and assing it to "n"
# Then we use a for loop saying that for each number inside the variable n
# and in this case ranging from 0 to n, it must print number**2.