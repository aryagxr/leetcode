#36
import collections


def validSudoku(board):
    #hashset
    column_set = collections.defaultdict(set)
    row_set = collections.defaultdict(set)
    square_set = collections.defaultdict(set)

    for row in range(9):
        for column in range(9):
            if board[row][column] == '.':
                continue
            if(board[row][column] in row_set[row] 
               or board[row][column] in column_set[column] 
               or board[row][column] in square_set[(row//3,column//3)]):
                return False
            column_set[column].add(board[row][column])
            row_set[row].add(board[row][column])
            square_set[(row//3,column//3)].add([board[row][column]])
    return True 















def validSudoku1(board):
    
    square_set=collections.defaultdict(set)
    
    for column in range(9):
        column_set = set()
        for row in range(9):
            
            #check rows
            row_set = set()
            for num in board[row]:
                if num in row_set and num!='.':
                    return False
                row_set.add(num)
                
            
            # check columns
            for i in board[row][column]:
                if i in column_set and i!='.':
                    return False
                column_set.add(i)

        
                     
    return True


    

print(validSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))