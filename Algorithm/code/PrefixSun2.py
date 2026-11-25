import io
import sys

_INPUT = """\
8 3
ACACTACG
3 7
2 3
1 8

"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------
# https://atcoder.jp/contests/abc122/tasks/abc122_c

N, Q = map(int, input().split())
S = " " + input().strip()

TARGET_STR = "AC"

ans = [0] * len(S)

# for１回で回すために前の数値持ってきてから今回分を計算する
for i in range(1, N + 1):
    ans[i] = ans[i - 1]
    if S[i - 1] + S[i] == TARGET_STR:
        ans[i] += 1


for _ in range(Q):
    l, r = map(int, input().split())
    print(ans[r] - ans[l])
