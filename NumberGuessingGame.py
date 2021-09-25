import random
# Variable defining

Num = random.randint(0,10)

guess = int(input("Guess The Correct Number Between 0 to 10! "))
Attempt = 1
print(" ")

# While loop that starts when guess is wrong

while guess != Num:
  print("Wrong guess, Try again Attempt number", Attempt)
  Attempt += 1
  print(" ")
  guess = int(input("Guess again: "))
  if guess == Num:
    break
# While loop ends when guess is correct

print("Correct guess! Your total attempts are:", Attempt)
print("Done")
  

