def solution(A):
    I = 1
    B = set(A)
    while True:
        if I not in B:
            return I
        I += 1