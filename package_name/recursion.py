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



def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n == 1:
        return 1
    elif n == 2:
        return 1:
    elif n > 2 :
        return fibonacci(n-1) + fibonacci(n-2)




def factorial(n):

    '''Return n!'''

    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num






    def reverse(word):

    '''Return word in reverse'''
    for i in range(len(word)):
        return word[::1]










        
