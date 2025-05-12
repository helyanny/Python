#Midnight Man game simulation
#Programmer: Helyanny Perozo

#Global variables
move1 = ""
othermove1 = ""
othermove2 = ""
othermove3= ""

#Introduction to the Midnight Man game
print('''
'  ▄▄▄█████▓ ██░ ██ ▓█████     ███▄ ▄███▓ ██▓▓█████▄  ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓    ███▄ ▄███▓ ▄▄▄       ███▄    █ 
'  ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██▒▀█▀ ██▒▓██▒▒██▀ ██▌ ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒   ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
'  ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██    ▓██░▒██▒░██   █▌▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░   ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
'  ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██    ▒██ ░██░░▓█▄   ▌▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░    ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
'    ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒   ░██▒░██░░▒████▓ ▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░    ▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
'    ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ░  ░░▓   ▒▒▓  ▒ ░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░      ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
'      ░     ▒ ░▒░ ░ ░ ░  ░   ░  ░      ░ ▒ ░ ░ ▒  ▒ ░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░       ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
'    ░       ░  ░░ ░   ░      ░      ░    ▒ ░ ░ ░  ░    ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░         ░      ░     ░   ▒      ░   ░ ░ 
'            ░  ░  ░   ░  ░          ░    ░     ░             ░  ░        ░  ░  ░  ░                   ░         ░  ░         ░ 
'                                             ░                                                                                 
''')
input("Welcome, venerable daredevil. You have been wanting to play with the spirits, and one has caught your attention. Press Enter")
print()
input("There's been a lot of talk about a Midnight Man. A spirit who is summoned through a candle ritual at 12:00am,\nand follows \
players around until 3:33. As long as he is present, players may not: Turn on the lights, \nfall asleep, leave the facility or \
let the candle go out. Pretty simple, right? Do not let him catch you")
print()

#Players chooses to light the candle
while True:
    candle_lit = str(input("It is now midnight. Are you willing to light the candle? ")).lower()
    #Candle is lit, game keeps going
    if candle_lit == "yes": break
    #Candle is not lit, game ends
    if candle_lit == "no":
        print()
        print("Good choice. You are safe and may continue living")
        exit()
    print("Invalid answer, please try again")


print()
input("You are a cunning one. You have chosen to awaken the Midnight Man.")
input("You must now remain awake until 3:33 am. Should you break the rules, you will meet your end.\nYour fate is in your hands.")
input("And his.")
    
while True:
    print()
    move1 = str(input("What is your first move? (Stairs, Guest room, Bathroom): ")).lower()
    if move1 in ["stairs", "guest room", "bathroom"]: break
    print("Invalid answer, please try again")
    
#Player chose the guest room
if move1 == "guest room":
    print()
    input("You chose to enter the guest room.")
    input("The week has been long. Despite your numerous attempts to keep your eyes open. Tiredness overtakes you.")
    
    while True:
        sleep = str(input("There is a cozy bed in front of you. Do you wish to fall asleep?: ")).lower()
        
        #Player broke the rules, game ends
        if sleep == "yes":
            print("You fell asleep and broke the rules. The Midnight Man caught you!")
            print('''

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
''')
            exit(1)
            
        #Game continues
        elif sleep == "no":
            print()
            print("Perhaps you are not tired enough. There is not much to do, so you head to a different location")
            while True:
                othermove1 = str(input("What is your next move? (Stairs, Bathroom): ")).lower()
                if othermove1 in ["stairs", "bathroom"]: break
                print("Invalid answer, please try again")
            break
            
        else: print("Invalid answer, please try again")

#Player chose the bathroom
if move1 == "bathroom" or othermove1 == "bathroom":
    input("You chose to enter the Bathroom")
    print("Ironically, entering the bathroom gave you the urge to do your business")
    while True:
        lights = str(input("The bathroom lights are off, do you wish to turn them on? ")).lower()
        
        #Player broke the rules, game over
        if lights == "yes":
            print("You turned on the lights and broke the rules. The Midnight Man caught you!")
            print('''

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
''')
            exit(2)
            
         #Game continues   
        elif lights == "no":
            print()
            print("Doing your business with the lights off? You fear nothing!")
            while True:
                othermove2 = str(input("What is your next move? (Stairs, Keep walking): ")).lower()
                if othermove2 in ["stairs", "keep walking"]: break
                print("Invalid answer, please try again")
            break
        
        else: print("Invalid answer, please try again")
            
    
#Player chose stairs
if move1 == "stairs" or othermove1 == "stairs" or othermove2 == "stairs":
    input("You chose to go downstairs")
    print("As you reach the bottom of the stairs, you are suddenly striken with fear")
    
    
    while True:
        door = str(input("The front door is right in front of you, do you wish to run away?")).lower()
        
         #Player broke the rules, game over
        if door == "yes":
            print("You left the facility and broke the rules. The Midnight Man caught you!")
            print('''

  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
''')
            exit(3)
            
        #Game continues   
        elif door == "no":
            print()
            print("You chose to face your fears and continue the game. Little did you know, it also saved your life!")
            othermove3 = "keep walking"
            break
        
        else: print("Invalid answer, please try again")
        

#Endgame
if othermove2 == "keep walking" or othermove3 == "keep walking":
    print("You kept walking and the clock reached 3:33am. You reached the end of the game and\n survived \
the night!")
    print('''

 ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .     ▄▄·       • ▌ ▄ ·.  ▄▄▄·▄▄▌  ▄▄▄ .▄▄▄▄▄▄▄▄ .·▄▄▄▄  
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▐█ ▌▪▪     ·██ ▐███▪▐█ ▄███•  ▀▄.▀·•██  ▀▄.▀·██▪ ██ 
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄    ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█· ██▀·██▪  ▐▀▀▪▄ ▐█.▪▐▀▀▪▄▐█· ▐█▌
▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▪·•▐█▌▐▌▐█▄▄▌ ▐█▌·▐█▄▄▌██. ██ 
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀     ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀.▀   .▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• 
''')
    exit(4)
    

    
    
    
    
    



    
    



