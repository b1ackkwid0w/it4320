#FizzBuzz challenge
#by Amy Snell 10/11/2021


def main():

    #adding program description and start control
    print('Welcome to my FizzBuzz Challenge!')
    input('Press enter to display FizzBuzz numbers 1 to 100...')
    print('\n')
    
    
    for n in range ( 1, 101 ): #listing numbers 1 to 100
    #adding condition for multiples of 3
        if n % 3 == 0: 
            print('Fizz')
    #adding condition for multiples of 5
        elif n %  5 == 0: 
            print('Buzz')
    #adding condition for multiples of both 3 and 5
        elif n % 15 == 0: 
            print('FizzBuzz') 
    #adding else condition for printing the numbers only
        else:
            print(n)

    #adding description and end control
    input('Press enter to exit...')
    exit()


main()
