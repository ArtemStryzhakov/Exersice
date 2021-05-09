# How do you reverse a given string in place without using a loop only?
#-----------------------------------------------------------------------

#import re

#text = input('Enter the sentence: ')
#text = re.findall('[a-zа-яё]+', text, flags=re.IGNORECASE)

#n = len(text) - 1
#for myText in text:
    #print(text[n], end=' ')
    #n -= 1

#Write a program to display the multiplication table of a given integer.
#-----------------------------------------------------------------------

#number = int(input('Enter the number: '))

#myNumb = 0
#while True:
#    print(f"{number} * {myNumb} = {number * myNumb}")
#    myNumb += 1
#    if myNumb == 10:
#       break

#Write a program to find the maximum and minimum element in an array.
#-----------------------------------------------------------------------

#array = [3,4,87,43,2]
#print(f"maximum element: {max(array)}\nminimum element: {min(array)}")

#Write a program to find the largest of three given (input) numbers. (e.g. 8, 6, 10 → 10)
#-----------------------------------------------------------------------

#a = float(input('First number: '))
#b = float(input('Second number: '))
#c = float(input('Third number: '))

#numberList = [a,b,c]
#print(max(numberList))

#Write a program to calculate the sum of elements in an array. (e.g. 1234 → 1 + 2 + 3 + 4 → 10)
#-----------------------------------------------------------------------

#a = 6789
#b = a//1000
#c = a%1000
#four = c//100
#five = c%11
#six = c%10

#print(f"{b} + {four} + {five} + {six} = {b+four+five+six}")

#Write a program to output a pyramid-like pattern with an asterisk.
#-----------------------------------------------------------------------

#print('  *  ')
#print(' *** ')
#print('*****')

#Write a program to check if a given number is odd or even. Return “odd” if the number is odd, or “even” if the number is even.
#-----------------------------------------------------------------------

#fortuna = float(input('Enter the number: '))

#if fortuna % 2 == 0:
#    print('Number is even.')
#else:
#    print('Number is odd.')
