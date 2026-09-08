def Search2D(mat, row, col, word):
    m = len(mat)
    n = len(mat[0])

    # Check first character
    if mat[row][col] != word[0]:
        return False

    lenWord = len(word)

    # 8 possible directions
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for direction in range(8):
        currX = row + x[direction]
        currY = col + y[direction]

        k = 1

        while k < lenWord:
            # Check boundaries
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break

            # Check character
            if mat[currX][currY] != word[k]:
                break

            currX += x[direction]
            currY += y[direction]
            k += 1

        if k == lenWord:
            return True

    return False


class Solution:
    def searchWord(self, mat, word):
        m = len(mat)
        n = len(mat[0])

        ans = []

        for i in range(m):
            for j in range(n):
                if Search2D(mat, i, j, word):
                    ans.append((i, j))

        return ans


def printresult(ans):
    for coord in ans:
        print(f"{{{coord[0]},{coord[1]}}}", end=" ")
    print()