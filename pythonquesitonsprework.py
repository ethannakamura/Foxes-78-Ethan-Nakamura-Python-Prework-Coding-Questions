#Question 1
#write a function to print "hello_USERNAME!" USERNAME is the input of the
#function. The first line of the code has been defined as below.
def hello_name():
    username = input("Enter your username")
    print("Hello " + username.upper())

hello_name()

#Question 2
#write a python function, first_odds that prints the odd numbers
#from 1-100 and returns nothing 
def first_odds():
    for num in range(1,100,2):
        print(num)

first_odds()
#Question 3
#Please write a Python function, max_num_in_list to return the
#max number of a given list. The firs tline of the code has 
#been defined as below.
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list([2,80])

#Question 4
#Write a function to return if the given year is a leap year. A
#leap year is divisible by 4, but not divisible by 100, unless
#it is also divisible by 400. The return should be boolean Type 
#(true/false)
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        if a_year % 400 == 0:
            return True
    elif a_year % 4 != 0:
        return False
    return True # if it doesn't catch any of the ones above
print(is_leap_year(1968))


#Question 5
#write a function to check to see if all numbers in list are consecutive
#numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but
#[1,2,4,5] are not consecutive numbers. The return should be boolean 
#Type.
def is_consecutive(a_list):
    counter=a_list[0]
    for num in a_list:
        if num != counter:
            return False
        counter += 1
        # num
    return True
print(is_consecutive([2,4,5,6,7]))