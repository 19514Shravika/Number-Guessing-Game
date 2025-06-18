import random
def user_attempts(user,random_num,loop_moves):
    if user_num == num:
        return f"You got it right!!, **YOU WON**"
    elif user_num > num:
        print(f"Chosen number is too-high, u got {moves-1} attempts to retry")
    elif user_num < num:
        print(f"Chosen number is too-low, u got {moves-1} attempts to retry")
    return None

num=random.randint(0,100)
choice=input("WHich level ur interested in : easy or hard")
if choice=="easy":
    max_moves=10
else:
    max_moves=5

for moves in range(max_moves,0,-1):
    user_num = int(input("Choose the number: "))
    result=user_attempts(user_num,num,moves)
    if result:
        print(result)
        break
else:
    print("**GAME OVER**, Refresh to play again")