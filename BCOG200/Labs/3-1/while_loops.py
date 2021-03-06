'''
    here is a basic while loop. in comments, type in what is happening
'''
# your comments here
print('Example 1')
i = 1
while i < 6:
    print(i)
    i += 1
print()

'''
    what is an 'infinite' while loop?
'''
# type your answer here
# while True:
#     pass

'''
    this code is an example of an infinite while loop. What happens if you run it?
        It will keep running for ever. Value of sum or i won't be changed
    edit the code so it does what is intended, printing 20 (the sum of the even numbers between 0 and 9)
'''
print('Example 2')
sum = 0
i = 0
while i < 10:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)
print()

'''
    break and continue are both ways to modify the behavior of a loop
    break exits the loop completely
    continue immediately restarts the loop from the top
    what does the code below do?
'''
# It will add all the even numbers from 0 to 10 inclusively
print('Example 3')
sum = 0
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    sum += i
print(sum)
print()

'''
    what happens if you change the code above from 'continue' to 'break'?
'''
# It will increment i. But it won't change the value of sum

'''
    write code that 
        - asks you to type in a number using the input function
        - computes the factorial of that number using a while loop
        - prints out the result
        
'''
print('Factorial code')
number = int(input('Factorial up to? \n'))
inc = 1
while number > 0:
    inc *= number
    number -= 1
print(inc)
