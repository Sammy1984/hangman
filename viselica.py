def hangman(word):
    wrong=0
    stages=['',
            '_______       ',
            '|             ',
            '|      |      ',
            '|      O      ',
            '|     /|\     ',
            '|     / \     ',
            '|             '
            ]
    rletters = list(word)
    board = ('__')*len(word)
    win = False
    print('Добро пожаловать на казнь!')

    while wrong < len(stages)-1:
        print('\n')
        msg='Введите букву>>'
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            char=board[cind]
            rletters[cind]='$'
        else:
            wrong+=1
        print(''.join(board))
        e=wrong+1
        print(''.join(stages[0:e]));
        if "__" not in board:
            print('Вы выиграли. Было загадано слово: ')
            print(''.join(board))
            win=True
            break
    if not win:
      print('\n'.join(stages[0:wrong]))
      print('Вы проиграли было загадано слово:{}.'.format(word))
hangman('кот')