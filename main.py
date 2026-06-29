import random
n = random.randint(1,10)

print("======WELCOME TO NUMBER GUESSING GAME======")
print("---You have 10 Chances to guess the number---")
print("   ---The secret number is between 1-10---")

print("===========================================")

attempt=10

num = 1

is_guess_correct = False

while num<=10:
    print(f"{attempt} attempts remaining.")
    user_guess=int(input("Enter any number between (1-10):"))

    if (user_guess == n):
        print(f"Congratulations, You guessed the correct number i.e {n}")
        is_guess_correct = True
        print("------------------------------------")
        break
    else :
                
        if(user_guess>n):
            print("Wrong Guess, Try a lower number")
            print("------------------------------------")
        elif(user_guess<n):
            print("Wrong Guess, Try a higher number")
            print("------------------------------------") 


    num=num+1 
    attempt-=1

if is_guess_correct == False:
    print("Bad Luck!!!, Limit Exhausted")

print(f"Secret number is {n}, Game Over")       
             
