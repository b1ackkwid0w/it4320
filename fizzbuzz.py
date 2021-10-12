#FizzBuzz
#This program prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five prints “FizzBuzz”
#by Amy Snell 10/11/2021

def main():

    #adding program description and start control
    print('FizzBuzz Numbers: ')
    print('\n')
        
    #fizzbuzz numbers
    for n in range ( 1, 101 ): #looping thru numbers 1-100
        #multiples of both 3 and 5
        if n % 15 == 0: 
            print('FizzBuzz') 
        #multiples of 3
        elif n % 3 == 0: 
            print('Fizz')
        #multiples of 5
        elif n %  5 == 0: 
            print('Buzz')
        #regular numbers
        else:
            print(n)

main()

