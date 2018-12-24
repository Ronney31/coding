#https://www.codechef.com/problems/TRUEDARE
'''for i in range(int(input())):
    input()
    TruthR = set(map(int,input().strip().split()))
    input()
    DareR = set(map(int,input().strip().split()))
    input()
    TruthS = set(map(int,input().strip().split()))
    input()
    DareS = set(map(int,input().strip().split()))
    if DareS.intersection(DareR) == DareS and TruthS.intersection(TruthR) == TruthS:
        print ("yes")
    else:
        print ("no")
'''

for _ in range(int(input())):
    input()
    TruthR = set((input().strip().split()))
    input()
    DareR = set((input().strip().split()))
    input()
    TruthS = set((input().strip().split()))
    input()
    DareS = set((input().strip().split()))
    if DareS.intersection(DareR) == DareS and TruthS.intersection(TruthR) == TruthS:
        print ("yes")
    else:
        print ("no")
