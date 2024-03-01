from art import logo
import random
from art import vs
from game_data import data
print(logo)
list_len = len(data)
def random_elem():
    rand = random.randint(0, list_len)
    return rand
value1 = data[random_elem()]
lost = False
count= 0
while (lost == False):
    value2 = data[random_elem()]
    print(f"Compare A: {value1['name']}, a {value1['description']}, from {value1['country']}")
    print(vs)
    print(f"Against B: {value2['name']}, a {value2['description']}, from {value2['country']}")
    ch = input("Who has more followers? A or B")
    maxim = max(value1['follower_count'], value2['follower_count'])
    if ch=="A":
        ch = value1['follower_count']
    else:
        ch = value2['follower_count']
    if ch >= maxim:
        count+=1
        print(f"You are right! Current score {count}")
        value1 = value2
    else:
        print(f"Sorry that's wrong. The final score is {count}")
        lost = True