import random
n= random.randint(1,11)
a = -1
guesses = 0
while(a!=n):
    guesses += 1
    a= int(input("Guess the number: "))
    if(a>n):
        print("Lower number pleasee")
    else:
        print("Higher number please")
print(f"You have correctly guessed the number in {guesses} attempts.")