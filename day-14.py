import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States',
    },
    {
        'name': 'Christiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal',
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician',
        'country': 'United States',
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina',
    }
]

score = 0
game_over = False
B = random.choice(data)

while not game_over:
    A = B
    B = random.choice(data)
    if A == B:
        B = random.choice(data)

    print(f"Score: {score}")
    print(f"COMPARE\n A: {A['name']}, a {A['description']}, from {A['country']}\n"
          f"AGAINST\n B: {B['name']}, a {B['description']}, from {B['country']}\n ")

    guess = input("Who has more followers? Type 'A' or 'B':\n").upper()
    if guess == 'A':
        if A['follower_count'] > B['follower_count']:
            score += 1
        else:
            print(f"You lose!.{B['name']} has more followers than {A['name']}\nFinal score: {score}")
            game_over = True
    elif guess == 'B':
        if B['follower_count'] > A['follower_count']:
            score += 1
        else:
            print(f"You lose!.{A['name']} has more followers than {B['name']}\nFinal score: {score}")
            game_over = True
