import random
while True:   
    print("Its time to number guessing game")
    print("difficulty :- ")
    print("1. easy (1 to 50) and 5 attempts")
    print("2. medium (1 to 100) and 7 attempts")
    print("3. hard (1 to 500) and 9 attempts")
    diff = input("difficulty : ")
    if diff == "1":
        n = 50
        max_attempts = 5
        print("mode easy")
    elif diff == "2":
        n = 100
        max_attempts = 7
        print ("mode medium")
    elif diff == "3":
        n = 500
        max_attempts = 9
        print ("mode hard")
    else:
        print ("invalid option")
        continue 
    sec = random.randint( 1, n )
    attempts = 0
    while True:
        
        try:    
            guess = int(input("guess : "))
        except:
            print("enter a valid number")
            continue
        if guess == sec:
            print("you won in ", attempts + 1, " attempts")
            break
        elif guess > sec:
            if guess - sec > 3:
                print ("too high")
            else:
                print ("close, but high")
        elif guess < sec:
            if sec - guess > 3:
                print ("too low")
            else :
                print ("close, but low")
        attempts += 1
        print(f"you have  { max_attempts - attempts}  attempts left")
        
        if attempts == max_attempts:
            print ("you lose, secret_number is ", sec)
            break
        print("-------------------------------")
    again = input("play again ? (y/n)")
    if again != "y":
        break