#The challenge here was to change the code in the def and return the message "Hello FirstName LastName! You just delved into python."

def print_full_name(first, last):
    first = raw_input(' ')
    last = raw_input(' ')
    print("Hello ", first_name, last_name, "! You just delved into python")

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)