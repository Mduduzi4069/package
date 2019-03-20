def sum_array(array):

    '''Return sum of all items in array'''

    if type(array) == int:
        return array

    total = 0
    for i in array:
        if type(i) == array:
            total = total+total_array(i)
        else:
            total = total+i
    return total



def nth_fib(n):
   if n == 0:
       return 1
   elif n == 1:
       return 0
   else:
       return nth_fib(n - 1) + nth_fib(n - 2)




def factorial(n):

    '''Return n!'''

    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num



def reverse(a_string):
    return a_string[::-1]
