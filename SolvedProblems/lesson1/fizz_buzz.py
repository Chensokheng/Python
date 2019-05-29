# In this program, I'm also check wheather the user provide the input or not

def fizz_buzz(num):
    
    try:
        input = int(num)
        if input % 3 == 0 and input % 5 != 0:
            return 'Fizz'
        elif input % 5 == 0 and input % 3 != 0:
            return 'Buzz'
        elif input % 3 == 0 and input % 5 == 0:
            return 'FizzBuzz'
        else:
            return input
    except ValueError :
        print('Invalid Input!')
        return '...'

print(fizz_buzz(input('Enter the number to Fizz_Buzz: ')))
