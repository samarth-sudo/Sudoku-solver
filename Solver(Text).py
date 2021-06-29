import pprint
""" Function to solve the Sudoku using backtracking algorithm
    :parameter Back: 2d list of int
    :return: solution"""
def solve(back):

    find = find_empty(back)
    if find:
        row, col = find
    else:
         return True
    for i in range(1,10):
        if valid(back, (row,col), i):
            back[row][col] = i

            if solve(back):
                return True

            back[row][col] = 0
    return False
"""Function to Check validity of the input values
   :parameter back: 2d list of int
   :parameter pos: (row, col)
   :parameter num: int
   :return: bool"""
def valid(back, pos, num):


 for i in range(0, len(back)):
        if back[pos[0]][i] == num and pos[1] != i:
         return False

 for i in range(0, len(back)):
      if back[i][pos[1]] == num and pos[1] != i:
          return False

 box_x = pos[1]//3
 box_y = pos[0]//3

 for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if back[i][j] == num and (i,j) != pos:
                return False
        return True
"""Function to print the board
   :parameter back: 2d list of int
   :return: None"""
def print_board(back):


    for i in range(len(back)):
        if i %3 == 0  and i != 0:
            print("- - - - - - - - - - - -")
        for j in range( len(back[0])):
            if j % 3 ==0:
                print(" | ", end =" ")

            if j == 8:
                print(back[i][j], end = "\n")
            else:
                print(str(back[i][j])+ " ", end = " ")

"""Function to find the empty space to fill in the board
    :parameter back: partially complete board
    :return: (int,int) row col"""
def find_empty(back):

    for i in range(len(back)):
        for j in range(len(back[0])):
            if back[i][j] == 0:
                return (i,j)

    return None

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)

