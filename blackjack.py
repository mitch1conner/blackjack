import random

J, Q, K, A = (10, 10, 10, 11)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]

host_hand = random.sample(cards, 2)
my_hand = random.sample(cards, 2)
print("Your deck:", my_hand)
print("PC deck:", host_hand[0], "_")

my_sum = my_hand[0] + my_hand[1]
host_sum = host_hand[0] + host_hand[1]


def add_card():
    global my_sum
    new_card = random.choice(cards)
    my_hand.append(new_card)
    my_sum += new_card
    if my_sum > 21 and A in my_hand:
        ace_index = my_hand.index(A)
        my_hand[ace_index] = 1
        my_sum -= 10  # Change the value of Ace from 11 to 1
    print(my_hand)


def blackjack():
    if my_sum > 21 and len(my_hand) > 2:
        print("Kaybettin")
    elif my_sum <= 21 and my_sum > host_sum:
        print("Kazandin")
    elif host_sum > 21:
        print("Kazandin")
    else:
        print("Kaybettin")


while True:


    choice = input("To take a card press 'k',to continue  'd' (to exit 'q'): ")
    host_hand = random.sample(cards, 2)
    my_hand = random.sample(cards, 2)
    print("Your deck", my_hand)
    print("PC deck:", host_hand[0], "_")

    if choice == "k":
        add_card()
        print("Your hand:", my_hand)
    elif choice == "d":
        while host_sum < 17:
            new_card = random.choice(cards)
            host_hand.append(new_card)
            host_sum += new_card
        print("PC deck:", host_hand)
        blackjack()
    elif choice == "q":
        break
