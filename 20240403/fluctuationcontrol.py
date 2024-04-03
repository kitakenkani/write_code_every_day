# https://atcoder.jp/contests/past201912-open/tasks/past201912_b

def parser(S :str):
    S = list(map(int, S.split("\n")))
    return S


def fluctuation(Ai, Aii):
    if Aii == Ai:
        print("stay")
    elif Aii < Ai:
        print("down", Ai - Aii)
    else:
        print("up", Aii - Ai)
S = """10
9
10
3
100
100
90
80
10
30
10"""
S = parser(S)
for i in range(1, len(S)-1):
    Ai = S[i]
    Aii = S[i + 1]
    fluctuation(Ai, Aii)