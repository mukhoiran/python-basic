player1 = {"name":"songoku", "power":100}
player2 = {"name":"bejita", "power":250}

def train(player):
    player['power'] += 100

def attack(attacker, defender):
    if(attacker['power'] > defender['power']):
        print('Attack successfully', attacker['name'])
    else:
        print('Attack failed', attacker['name'])

train(player1)
train(player1)
attack(player1, player2)
