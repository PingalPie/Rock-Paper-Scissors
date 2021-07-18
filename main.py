import random
# Module required 
# random module is in-built so, you there is no need to install it

def loop():
    ans = random.choice(['Rock', 'Paper', 'Scissors'])
    # Making command for computer to choose any option
    opt = input('Rock, Paper or Scissors - ')
    # Asking user their answer
    if opt == 'rock':
        # If your answer is rock
        if ans == 'Paper':
            # If your answer is rock and computer has paper
            print('You lost, computer was having paper')
            loop()
        elif ans == 'Scissors':
            # If your answer is rock and computer answer is scissors
            print('You won, computer was having scissors')
            loop()
        elif ans == 'Rock':
            # If your answer is rock and computer answer is also rock
            print('Try again, you and computer was having same answer')
            loop()
    elif opt == 'paper':
        if ans == 'Scissors':
            # If your answer is paper and computer answer is scissors
            print('You lost, computer was having scissors')
            loop()
        elif ans == 'Rock':
            print('You won, computer was having rock')
            # If your answer is paper and computer answer is rock
            loop()
        elif ans == 'Paper':
            # If your answer is paper and computer answer is also paper
            print('Try again, you and computer was having same answer')
            loop()
    elif opt == 'scissors':
        if ans == 'Rock':
            # If your answer is scissors and computer answer is rock  
            print('You lost, computer was having rock')
            loop()
        if ans == 'Paper':
            # If your answer is scissors and computer answer is paper
            print('You won, computer was having paper')
            loop()
        if ans == 'Scissors':
            # If your answer is scissors and computer answer is also scissors
            print('Try again, you and computer was having same answer')
            loop()
    else:
        print('Enter correct option')
        # If your answer is not from rock paper scissors
        loop()
    print(ans)
    # Here all logs will come what were the computer answers every time
    # It is for if an error comes
    
loop()
