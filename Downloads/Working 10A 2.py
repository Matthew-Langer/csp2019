from __future__ import print_function
import matplotlib.pyplot as plt
import random

 

plt.ion() 
       
def roll_hundred_pair():
    '''This simulated rolling 2 dice one hundred times 
        and constructs a histogram of the data'''    
    a = []
    b = []
    a += [random.randint(1,6) for number in range(0,100)]
    b += [random.randint(1,6) for number in range(0,100)]
    #combines the results of dice a and b into a histogram and prints out the values/length to confirm 200 digits.
    print (a + b)
    print (len(a + b))

    plt.hist(a + b)
    plt.show()
    
def dice(n):
    #creates an empty list for a. Then adds values (1-6) to the list the number of times specified (due to range 0-n). 
    a = []
    a += [random.randint(1,6) for number in range(0,n)]
    print(a)
    print (sum (a))
    
def hangman(guessed, secret):
  # Creates an empty list 
  show = []
  
  #Looks at all characters in 'secret' and checks to see if there is a space. 
  #Then it checks to see if the character wasn't in guessed (and puts a dash)
  #Then it checks to see if the character was in guessed (and shows the character)
  #When it prints, it goes through each character individually, and I don't know how to make it show up on one line. 
  
  for character in secret:
    if character == ' ':
        show += ' '
    elif character not in guessed:
      show += '-'
    else:
      # If letter guessed, replace with letter
        if character in guessed:
            show += character
    print(show)


#1.3.8 Number 8
 
def goguess():
    print("I have a number between 1 and 20 inclusive.")
    number = random.randint(1, 20)
    print (number)
    guess = raw_input("Guess: ")
    
    if int(guess) > number: 
        print("You guessed too high!")
    elif int(guess) < number:
        print("You guessed too low!")
    else:
        print("You guessed correctly!")
    