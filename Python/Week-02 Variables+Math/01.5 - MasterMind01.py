import random
Guessing = True

while True:
    COMP1 = random.randint(0, 1)
    COMP2 = random.randint(0, 1)
    COMP3 = random.randint(0, 1)
    COMP4 = random.randint(0, 1)
    COMP = str(COMP1) + str(COMP2) + str(COMP3) + str(COMP4)
    COMPA = list(COMP)
    correct = 0
    tryes = 0
    while Guessing:
        tryes = tryes + 1
        UGS = input("Whats your guess? (max 4 e.g. 1010  ) (type STOP to stop) \n")
        if UGS == "STOP":
            break
        UGA = list(UGS)
        for i in range(4):
            if UGA[i] == COMPA[i]:
                correct = correct + 1
        print("you got ", correct, "correct")
        if correct == 4:
            print("You Guessed Correctly!! in", tryes, "Goes!!")
            Guessing = False
        correct = 0
    UGS = input("do you want to play again? (Yes or STOP) \n")
    if UGS == "Yes":
        print("Going Again!!!")
        Guessing = True
    if UGS == "STOP":
        break
