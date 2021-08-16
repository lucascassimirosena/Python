string1 = "I'm "
string2 = "going to get "
string3 = "a Dev job!"

print(string1 + string2 + string3)
print( "I'm " "going to get " "a Dev job!")
#both outputs will be the same

#it's possible to multiply string in python
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "monday"
print("day" in today) #True
print("mon" in today) #True
print("night" in today) #False