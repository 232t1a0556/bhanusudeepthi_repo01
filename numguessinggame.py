import random
n=int(input())
a=int(input("Guess: "))
if a==n:
    print("Correct..!")
elif a<n:
    print("Too Low!")
else:
    print("Too High!")