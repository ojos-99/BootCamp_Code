from random import randint

a = randint(1,100)
while True:
    i = (input("Guess: "))
    try:
        i = int(i)
    except:
        print("Input an integer")
        continue
    if i < a:
        print("Too Low")
    elif i > a:
        print("Too High")
    else:
        print("Got It!")
        break
