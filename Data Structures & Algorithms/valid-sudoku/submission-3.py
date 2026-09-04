class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rowwise=[set(row)-{"."} for row in board]
        #columWise=[set(board[:len(board)][i])-{"."} for i in range(0,len(board[0]))]
        rowwise=[set() for i in range(0,len(board))]
        colwise=[set() for i in range(0,len(board[0]))]
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                blockwise=set()
                for b_r in range(i,i+3):
                    for b_c in range(j,j+3):
                        if board[b_r][b_c] ==".":
                            continue
                        if board[b_r][b_c] not in blockwise:
                            blockwise.add(board[b_r][b_c])
                        else:
                            return False
                        if board[b_r][b_c] not in rowwise[b_r]:
                            rowwise[b_r].add(board[b_r][b_c])
                        else:
                            return False
                        if board[b_r][b_c] not in colwise[b_c]:
                            colwise[b_c].add(board[b_r][b_c])
                        else:
                            return False
                if len(blockwise)==1 and blockwise=={'.'}:
                    return False
        for i in range(0,len(rowwise)):
            if (len(rowwise[i])==1 and rowwise[i]=={'.'}) or (len(colwise[i])==1 and colwise[i]=={'.'}):
                return False
        return True