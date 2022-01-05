#2021-1학기 웹파이썬
import os
######################### 1번 #########################
def getNewMatrix(n):
    z = n
    row = 0
    col = -1
    inc = 1
    n_2 = 1
    matrix = [[0] * n for i in range(n)]

    if n%2 == 1:
        while n >0:
            for i in range(n):
                col +=inc
                matrix[row][col] = z**n_2
            n = n -1
            if n==0:
                break
            for i in range(n):
                row += inc
                matrix[row][col] = z**n_2
        
            inc = inc * -1
            if inc ==1:
                n_2 +=1
    else:
        print("입력값이 홀수가 아닙니다.")
    return matrix
n = int(input("숫자를 입력하세요 : "))
matrix = getNewMatrix(n)
print(matrix)

######################### 2번 #########################
def saveFileMatrix(matrix):
    cnt = 0
    if os.path.isfile("MATRIX.txt"):
        with open('MATRIX.TXT', "a") as file:
            file.write("#LENGTH:{}#\n[".format(len(matrix[0])))
            for i in matrix:
                file.write(str(i))
            file.write("]\n")
    else:
        
        with open('MATRIX.TXT', "w") as file:
            file.write("#LENGTH:{}#\n[".format(len(matrix[0])))
            for i in matrix:
                file.write(str(i))
            file.write("]\n")
    with open("MATRIX.TXT", 'r') as file:
        cnt = int(len(file.readlines())/2)
    return cnt
cnt = saveFileMatrix(matrix)
print(f"saveFileMatrix 함수를 {cnt}번 실행했습니다.")
"""
######################### 3번 #########################
def readFileMatrix(n):
    with open("MATRIX.TXT","r") as file:
        read_file = file.readlines()
    
    return read_file

a = readFileMatrix(n)
#print(a.index(n))"""