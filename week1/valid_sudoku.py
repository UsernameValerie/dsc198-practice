def isValidSudoku(board: list[list[str]]) -> bool:
    perrow = [""]*9
    percol = [""]*9
    perbox = [""]*9
    boxtopright = [1,2,5] # row < col
    boxdiag = [0,4,8] # row = col
    boxbottomleft = [3,6,7] # row > col

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            box_loc = (i // 3) * 3 + (j // 3)
            
            if cell == ".":
                continue
            if cell in perrow[i] or cell in percol[j] or cell in perbox[box_loc]:
                return False
            else:
                perrow[i] += cell
                percol[j] += cell
                perbox[box_loc] += cell
    return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))

# time complexity is O(9^2) because we are iterating through the 
# 9x9 board once.
# The space complexity is similar; we store the values of each row, 
# column, and box in separate lists.

# my first attempt failed because I used an overly complicated and incorrect
# method to determine which box a cell was in.
# I could improve the current solution by using sets in dictionaries
# instead of strings in lists
# it's faster and if I use sets as the key for the dictionary for 
# the boxes I don't need to calculate the box location as a single number, 
# I can use row and col as coordinates