def isValidSudoku( board: [[]]) -> bool:
    for r in range(9):
        row_set = set()
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            if val in row_set:
                return  False
            row_set.add(val)

    for c in range(9):
        col_set = set()
        for r in range(9):
            val = board[r][c]
            if val == '.':
                continue
            if val in col_set:
                return False
            col_set.add(val)


    for box_r in range(0,9,3):
        for box_c in range(0, 9, 3): #3x3 box
            box_set = set()

            for r in range(box_r, box_r+3):
                for c in range(box_c, box_c+3):
                    val = board[r][c]
                    if val == '.':
                        continue
                    if val in box_set:
                        return False
                    box_set.add(val)



    return True

#Time_complexity -> o(1) #-> Because the board size is strictly fixed at 9x9, making the maximum number of operations (81cell * 3 passes) constant.
#Space_complexity -> o(1) #-> Because the hash sets will store a maximum of 9 elements (digits 1-9) at any given time, requiring constant memory.

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","8","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

