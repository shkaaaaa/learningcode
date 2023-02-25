import random
comp=random.randint(1,100)
guesses=0

while True:
    user=int(input("Guess a number between 1 to 100 : "))
    if user==comp:
        print(f"Guessed it right! in {guesses} Guesses")
        with open("D:\Python\Data structures\highscore.txt","r") as f:
            currenthighscore=int(f.read())
        if currenthighscore>guesses:
            with open("D:\Python\Data structures\highscore.txt","w") as f:
                f.write(str(guesses))

        break
    elif user<comp:
        print("Guessed wrong value is bigger")
        guesses+=1
    else:
        print("Guessed it wrong value is smaller")
        guesses+=1
with open("D:\Python\Data structures\highscore.txt") as f:
    currenthighscore=int(f.read())
print(f"highest score is: {currenthighscore}")