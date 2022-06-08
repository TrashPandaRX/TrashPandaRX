row0 = [0,0,0,0,0]
row1 = [1,1,1,1,1]
row2 = [2,2,2,2,2]
row3 = [3,3,3,3,3]
row4 = [4,4,4,4,4]

hold_rows = {
    0 : row0,
    1 : row1,
    2 : row2,
    3 : row3,
    4 : row4
}

for current_row in hold_rows:
    row_array = hold_rows[current_row]
    print(row_array)