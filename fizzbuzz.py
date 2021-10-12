#FizzBuzz challenge
#by Amy Snell 10/11/2021

import time


def main():

    #adding program description and start control
    print('================')
    print(' .-.\n \_/     Fizz\n{|||)<\n / \\     Buzz\n `-`')
    run_app = "Y"
    input('\nHello...Press any key to display FizzBuzz numbers 1 to 100:')
    while run_app == 'Y':
        start = time.time()
        print('\n')
        
        #fizzbuzz numbers
        for n in range ( 1, 101 ): #looping thru numbers 1 to 100
            #adding condition for multiples of both 3 and 5
            if n % 15 == 0: 
                print('FizzBuzz') 
            #adding condition for multiples of 3
            elif n % 3 == 0: 
                print('Fizz')
            #adding condition for multiples of 5
            elif n %  5 == 0: 
                print('Buzz')
            #regular numbers
            else:
                print(n)

        end = time.time()
        
        #asking user to run again or exit
        print(f'\nWow! That was fast...Current Runtime: {end - start} sec')
        answer = input('Would you like to run FizzBuzz again? (Y/N): ')
        run_app = answer.upper()

    else: #exit message
        print('\nThank you for using FizzBuzz...')
        print(' .-.\n \_/     Good\n>(|||}\n / \\      Bye\n `-`')
        exit()


main()

