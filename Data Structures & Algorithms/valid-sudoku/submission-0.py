class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkset = {}

        for i in range(1, 10):
            checkset[i] = [0, 0, 0]
        
        for row in board:
            for block in row:
                if block != ".":
                    if checkset[int(block)][0] == 1:
                        # print("fail row")
                        return False
                    else:
                        checkset[int(block)][0] = 1
            for i in range(1, 10):
                checkset[i][0] = 0

        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if checkset[int(board[j][i])][1] == 1:
                        # print("fail column")
                        return False
                    else:
                        checkset[int(board[j][i])][1] = 1
            for i in range(1, 10):
                checkset[i][1] = 0

        for sub_box in range(9):
            i = (sub_box * 3) % 9
            j = ((sub_box // 3) * 3) % 9

            # print(i, j)

            for index_i in range(3):
                for index_j in range(3):
                    if board[j + index_j][i + index_i] != ".":
                        if checkset[int(board[j + index_j][i + index_i])][2] == 1:
                            # print(i, j, checkset[int(board[j][i])], checkset[int(board[j][i])][2])
                            # print("fail sub box")
                            return False
                        else:
                            # print("check")
                            checkset[int(board[j + index_j][i + index_i])][2] = 1
            for i in range(1, 10):
                checkset[i][2] = 0

        return True

    