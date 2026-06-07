class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hm = {}
        for i in range(len(board)):
            hor = set()
            vert = set()

            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in hor:
                        return False
                    hor.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in vert:
                        return False
                    vert.add(board[j][i])

                if (i // 3, j // 3) not in hm:
                    hm[(i // 3, j // 3)] = set()
                    if board[i][j] != ".":
                        hm[(i // 3, j // 3)].add(board[i][j])
                else:
                    if board[i][j] in hm[(i // 3, j // 3)]:
                        return False
                    if board[i][j] != ".":
                        hm[(i // 3, j // 3)].add(board[i][j])

        return True
