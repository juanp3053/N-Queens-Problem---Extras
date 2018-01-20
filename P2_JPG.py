# P2_JPG.py

maxrange = int(input("What is the maximun range, 1 to __? "))
minrange = 1
got = False

while got!= True:
    guess = (maxrange + minrange)//2
    print("Is it " + str(guess) + " ?")
    Uinput = input("Tell me too high with >, too low with <, or y if I got it! ")
    
    if Uinput == "y":
        print("Wow I got it! " + str(guess))
        got=True
        
    if Uinput == "<":
        minrange = guess+1

    if Uinput == ">":
        maxrange = guess-1

print("Thanks for the game!")
