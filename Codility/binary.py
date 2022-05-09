# BinaryGap
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    pass
    bN = bin(N)
    bNStr = str(bN)
    IndexList = []
    tmp = 0
    for i in range(len(bNStr[2:])):
        if bNStr[2:][i] == "1":
            IndexList.append(i)
    for i in range(len(IndexList)-1):
        if int(IndexList[i+1]) - int(IndexList[i]) >= tmp:
            tmp = int(IndexList[i+1]) - int(IndexList[i])
    if tmp - 1 < 0:
        return 0
    else:
        return tmp - 1