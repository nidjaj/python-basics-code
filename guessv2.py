import random
random_number = random.randint(1,10)
guess = input("pick a number from 1 to 10:")
guess = int(guess)
while guess != random_number:
    guess = input("pick a number from 1 to 10:")
    guess = int(guess)

if guess < random_number:
    print ("too low")
elif 
    print("too high")
print(random_number)
    
              
