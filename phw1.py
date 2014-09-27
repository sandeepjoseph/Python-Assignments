#Program to find the number a user guessed
#Author : Sandeep Joseph
#Date   : 09/12/2014
#Version: V1.0

#import Statements

import sys

print("--------------------------Number Guess Game------------------------\n")

#Initial Variable declaration
choice = True

MyName1  = input("Please enter your name : ")
l        = len(MyName1)
MyName11 = MyName1[0].upper()
MyName   = MyName11+MyName1[1:l]

#Iterating loop for multiple user attempts
while choice == True:
    invalid  =  False
    count    =  0
    hi       =  100
    lo       =  1
    mid      =  ( hi + lo ) // 2
    
    print("\nDear "+MyName+" Please Guess A Number between 0 and 100!!!")
    UserResponse = " "      

    while UserResponse.lower() != "yes":
        CalculatedGuess         = mid
        UserResponse            = input("\nIs "+ str(mid) +" your Number??\n")

        if UserResponse.lower() == "no":
            UserResponse1       = input("\nIs your number higher??\n")
            
            if UserResponse1.lower()      == "yes":
                lo  = CalculatedGuess + 1
                mid = (lo + hi) // 2
          
            elif UserResponse1.lower()    == "no":
                hi  = CalculatedGuess - 1
                mid = (lo + hi) // 2
          
            else:
               print("\nInvalid User Input!!!\n")
               invalid = True
               break
        else:
            print("\nInvalid User Input!!!\n")
            invalid = True           

        count += 1
        
    if invalid != True:     
        print("\nThe Number you guessed : "+str(CalculatedGuess))
        print("\nNumber of Attempts     : "+str(count))
            
    ch = input("\nDo you wish to play again??\nplease enter yes/no!!\n")
          
    if ch.lower()   == "yes":
          choice    =   True
          continue
        
    elif ch.lower() == "no":
          choice    ==  False
          print("\nThank you "+MyName+" visit back again!!")
          sys.exit() #system termination of program
#------------------------------------------------------------------------------#
          
          
