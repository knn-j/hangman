def hangman(word):
    wrong = 0
    stages = ["",
             "__________      ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\\     ",
             "|       / \\     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    # print(stages)
    len_stages = len(stages)
    print("\n".join(stages))
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess one character: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        # print("board", board)
        # print("rletters", rletters)
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        # print("\n".join(stages[0:wrong + 1]))
        print("You lose! Answer is {}".format(word))


answers = ["cat", "dog", "bird"]
import random
pick = random.choice(answers)
stages = ["",
             "__________      ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\\     ",
             "|       / \\     ",
             "|               "
              ]

hangman(pick)
