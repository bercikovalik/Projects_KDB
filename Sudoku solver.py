#Backtrack algorithm
base  = 3
side  = base*base

def pattern(r,c): return (base*(r%base)+r//base+c)%side
    
from random import sample
def shuffle(s): return sample(s,len(s))
rBase = range(base)
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
completed_board = [line[:] for line in board]

squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0
numSize = len(str(side))

arr1 = []
for line in board:
    arr1.append([n for n in line])

print("Completed Board:")
for line in completed_board:
    print(line)

print("\nIncomplete Board:")
for line in arr1:
    print(line)

print("\n")

pos = {}
rem = {}
graph = {}

def printMatrix():
    for i in range(0, 9):
        for j in range(0, 9):
            print(str(arr1[i][j]), end=" ")
        print()

def is_safe(x, y):
    key = arr1[x][y]
    for i in range(0, 9):
        if i != y and arr1[x][i] == key:
            return False
        if i != x and arr1[i][y] == key:
            return False

    r_start = int(x / 3) * 3
    r_end = r_start + 3

    c_start = int(y / 3) * 3
    c_end = c_start + 3

    for i in range(r_start, r_end):
        for j in range(c_start, c_end):
            if i != x and j != y and arr1[i][j] == key:
                return False
    return True

def fill_matrix(k, keys, r, rows):
    for c in graph[keys[k]][rows[r]]:
        if arr1[rows[r]][c] > 0:
            continue
        arr1[rows[r]][c] = keys[k]
        if is_safe(rows[r], c):
            if r < len(rows) - 1:
                if fill_matrix(k, keys, r + 1, rows):
                    return True
                else:
                    arr1[rows[r]][c] = 0
                    continue
            else:
                if k < len(keys) - 1:
                    if fill_matrix(k + 1, keys, 0, list(graph[keys[k + 1]].keys())):
                        return True
                    else:
                        arr1[rows[r]][c] = 0
                        continue
                return True
        arr1[rows[r]][c] = 0
    return False

def build_pos_and_rem():
    for i in range(0, 9):
        for j in range(0, 9):
            if arr1[i][j] > 0:
                if arr1[i][j] not in pos:
                    pos[arr1[i][j]] = []
                pos[arr1[i][j]].append([i, j])
                if arr1[i][j] not in rem:
                    rem[arr1[i][j]] = 9
                rem[arr1[i][j]] -= 1


    for i in range(1, 10):
        if i not in pos:
            pos[i] = []
        if i not in rem:
            rem[i] = 9

def build_graph():
    for k, v in pos.items():
        if k not in graph:
            graph[k] = {}

        row = list(range(0, 9))
        col = list(range(0, 9))

        for cord in v:
            row.remove(cord[0])
            col.remove(cord[1])

        if len(row) == 0 or len(col) == 0:
            continue

        for r in row:
            for c in col:
                if arr1[r][c] == 0:
                    if r not in graph[k]:
                        graph[k][r] = []
                    graph[k][r].append(c)


build_pos_and_rem()

rem = {k: v for k, v in sorted(rem.items(), key=lambda item: item[1])}

build_graph()

key_s = list(rem.keys())
fill_matrix(0, key_s, 0, list(graph[key_s[0]].keys()))

printMatrix()

#Time complexity: O(9^(n*n))
#Auxiliary Space: O(n*n)
