import random
store=random.randint(1,100)
num:int=0
max_attempts=5
attempts=0
while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))   
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        attempts += 1
        if(guess<store):
         print("your number is less than guessed number")
        elif(guess>store):
         print("your number is greater than guessed number")
        else:
         print("congrats you guessed correct")
         break
if (attempts==max_attempts and guess!=store):
   print(f"you have used all your {max_attempts}atempts, the guessed number was {store},,better luck next time,")           