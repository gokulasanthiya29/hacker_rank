def print_full_name(first, last):
    print("Hello {first} {last}! You just delved into python.".format(first=first_name, last=last_name))
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
