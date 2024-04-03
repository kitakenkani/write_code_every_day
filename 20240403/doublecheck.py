# https://atcoder.jp/contests/past201912-open/tasks/past201912_a

def checknumber(S):
    try:
        S = int(S)
    except:
        return False
    return True

S = "012"

if checknumber(S):
    print(int(S) * 2)
else:
    print("error")