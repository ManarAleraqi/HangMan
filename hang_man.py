# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:42:15 2023

@author: ADMIN
"""




from random import randint

list_of_words=["manar","berst","person"]

list_of_letters=[]
list_of_guess=[]

player=True
counter=4
c=0

guess=randint(0,len(list_of_words)-1)
for let in list_of_words[guess]:
    list_of_letters.append(let)
    
    
for i in list_of_letters:
    list_of_guess.append(len(i)*'_')


while player:
    print(list_of_guess)
    guess_in=input("guess the word")
    
    if guess_in in list_of_letters:
        
        if guess_in in list_of_guess:
                    index_val=list_of_guess.index(guess_in)
                    if guess_in in list_of_letters[index_val+1:]:
                        print("exist in :",list_of_letters[index_val+1:].index(guess_in))
                        list_of_guess[
                            index_val + list_of_letters[index_val+1:].index(guess_in)+1
                            ] = guess_in
        else:
             list_of_guess[list_of_letters.index(guess_in)] = guess_in
        if list_of_guess==list_of_letters:
            print("you win")
            print(list_of_guess)
            player=False
            
    else:
        counter-=1
        if counter==0:
            print("loseeerrr!!!!")
            player=False
            
   













