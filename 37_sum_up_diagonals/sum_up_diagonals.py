def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # springboard answer
    total = 0 

    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1-i]

    return total

#   >>> m2 = [
#         ...    [1, 2, 3],
#         ...    [4, 5, 6],
#         ...    [7, 8, 9],
#         ... ]
#         >>> sum_up_diagonals(m2)
#         30
    # i = 0:    total += matrix[0][0] // 0 + 1 =1
    #           total += matrix[0][-1-0 = -1]// 1 + 3 = 4

    # i = 1:    total += matrix[1][1]// 4 + 5 = 9
    #           total += matrix[1][-1-1=-2]//9 + 5 = 14

    # i = 2     total += matrix[2][2] //14 + 9 = 23
    #           total += matrix[2][-1-2=-3]// 23 +7 =30
    # answer is 30

    # total=0
    # diagnal_row =[y for y in list(reversed(range(len(matrix))))]
    # for x in range(len(matrix)):
    #     total += (matrix[x][x] + matrix[x][diagnal_row[x]])
    
    # return total