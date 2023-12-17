def init_board(board):
    t1 = []
    for i in range(board['size']):
        t1.append(i+1)
    board['towers'] = [t1, [], []]


def draw_board(board):
    # prepare
    size = board['size']
    towers = []
    for i in range(3):
        tower = board['towers'][i]
        towers.append([0]*(size-len(tower))+tower)
    # draw
    for h in range(size):
        for i in range(3):
            b = size-towers[i][h]
            w = towers[i][h]*2-1
            if towers[i][h] != 0:
                print(" "+" "*b+"#"*w+" "*b+" ", end="")
            else:
                print(" "*(2*size+1), end="")
            if i != 2:
                print('|', end="")
        print()


def move_board(board, src, dst):
    board['towers'][dst].insert(0, board['towers'][src][0])
    dsk = board['towers'][src][0]
    del board['towers'][src][0]
    print(dsk, ": ", src, "->", dst)


def hanoi(n, board, src, dst, tmp):
    if n > 0:
        hanoi(n-1, board, src, tmp, dst)
        move_board(board, src, dst)
        # draw_board(board)
        hanoi(n-1, board, tmp, dst, src)


board = dict()
size = 2
board['size'] = size
init_board(board)
# draw_board(board)
hanoi(size, board, 0, 2, 1)
