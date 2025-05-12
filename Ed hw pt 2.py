# Author: Helyanny Perozo
# Student ID: 261238389
# September 2024
# Program that determines if user is a bot or a human

print("Bot or Human? Let's figure this out!")

# Code for the availability of responder
availability = float(input("When did you receive your\
 response (type a float between 0 and 24)?"))
if 2 <= availability <= 5 :
    print('You just talked to a bot')
    
# Code for wait time of the response
else :
    wait_time = float(input("How long did it take to get your response (in min)?"))
    if wait_time < 0.15 :
        print('You just talked to a bot')
        
# Code for words per minute
    else :
        number_of_words = int(input("How many words in your response?"))
        if number_of_words < 66 :
            print("You just talked to a fellow human")
            
# Code for typos
        else :
            number_of_typos = int(input("How many typos in the response \
(grammatical errors, misspelled words, etc.)?"))
            if number_of_typos > 0 :
                print("You just talked to a fellow human")
            else :
                final_test = int(input("Ask the responder how many 't' there are \
in 'eeooeotetto' and typoe their answer?"))
                
#Code for final test
                if final_test == 3 :
                    print("You just talked to a fellow human")
                else :
                    print("You just talked to a bot")

                
            
                
