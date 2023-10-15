import random
def hangman():
    word_list = ['dog', 'cat', 'fly', 'key', 'you']
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print("Welcome to Hangman!!")
    
    while wrong < len(stages) - 1:
        print('\n')
        msg = '１文字を予想してね'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
            print(" ".join(board))
        else:
            wrong += 1
        # print(" ".join(board))
        print("\n".join(stages[wrong:wrong+1]))
        if '_' not in board:
            print('あなたの勝ち！！')
            print(' '.join(board))
            win = True
            break
    if not win:
        # print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！！正解は{}'.format(word))
        
hangman()