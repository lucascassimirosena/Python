import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    check = {True: "Not Weird", False: "Weird"} #Boolean values True or False, it'll print a message depending
    #on the value
    print(check[                #this  will start and print the value of the variable
        n%2==0 and (            #if the value meets these specification it will be true and not weird
            n in range(2, 6) or
            n > 20)
    ])
