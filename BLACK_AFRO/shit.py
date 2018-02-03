import numpy as np # manipulating arrays
import random as rand # random functions
import os # general functions of operating system

#######################################################################
#                                                                     #
# PROGRAM: BLACKJACK BASIC ACTIONS AND FUNCTIONS                      #
# AUTHOR: ORIOL TUBELLA, SERGI DOMINGO                                #
# DATE: 02/02/2018                                                    #
# VERSION: 1                                                          #
#                                                                     #
#######################################################################

#######################################################################
# CREATING A DECK                                                     #
#######################################################################


def create_deck(N_decks): # input:number of decks playing with

    N_cards = 52 # number of cards in a deck
    N_suits = 4 # number of suits in a deck
    N_scards = N_cards/N_suits # number of cards in a suit
    N_tcards = N_cards*N_decks # number of total cards
        
    out_list = np.zeros((N_tcards),dtype=int) # declare output deck
    count = 0 # indexing array

    for i in np.r_[1:(N_scards+1)]: # filling bucle with english cards
        for j in np.r_[0:N_suits*N_decks]: # no jokers 
            
            out_list[count] = i # asign value to position
            count += 1 # sum one to the count

    return (out_list) # output:ordenate deck

#######################################################################
# SHUFFLING A DECK                                                    #
#######################################################################
    
def shuffle_deck(en_deck,intensity): # input deck and low,medium,high
                                     # shuffle intensity
    N_tcards = len(en_deck) # number of total cards in current deck

    if (intensity == 'low'): # if intensity low: 100 iterations

        it = 100

    elif (intensity == 'medium'): # else if intesity is medium then

        it = 1000

    else: # anything else: set intensity value to highest iterations 

        it = 10000
    
    for i in np.r_[0:it]: # do bucle 'it' times

        index1 = int((N_tcards-1)*rand.random()) # throw first rand int
        index2 = int((N_tcards-1)*rand.random()) # throw second rand
        memory = en_deck[index1] # save first value in memory
        en_deck[index1] = en_deck[index2] # change positions
        en_deck[index2] = memory 

        en_deck = en_deck[::-1] # reverse deck

    return (en_deck) # output: shuffled deck 
        
#######################################################################
# PICKING A CARD                                                      #
#######################################################################

def pick_a_card_from_deck(current_deck): #input:deck with N cards

    picked_card = current_deck[0] # pick the first card
    new_deck = np.delete(current_deck,0) # delete this card from deck

    return (picked_card,new_deck) # o: p-c and new deck with N-1 cards

#######################################################################

#######################################################################
# CHECK MAGIC PUNCTUATION                                             #
#######################################################################

def check_magic_points(few_cards): # input: inspecting card
    
    Ncards = len(few_cards) # length of the input card list
    MP = 0 # magic points

    for i in np.r_[0:(Ncards-1)]: # check all cards in the list
 
        if (few_cards[i] > 1 and few_cards[i] < 7): # 2-6: +1
        
            MP += 1

        elif ((few_cards[i] > 6 and few_cards[i] < 10) or 
              few_cards[i]==0): # 7-9 or 0: 0

            MP += 0

        else: # 10,11,12,13,1: 1

            MP += -1

    return (MP) # o: return total magic points

#######################################################################

#######################################################################
#                                                                     #
# END                                                                 #
#                                                                     #
#######################################################################

#######################################################################
# TESTING AREA                                                        #
#######################################################################
'''
a = shuffle_deck(create_deck(6),'high')

for i in np.r_[1:313]:

    print (a,len(a))
    print ('\n')
    b,c = pick_a_card_from_deck(a)
    print (b,'picked card num '+str(i))
    print ('\n')
    a=c
'''

