import io
import sys
from itertools import accumulate

_INPUT = """\
5
3 1 4 1 5
1 4
"""
sys.stdin = io.StringIO(_INPUT)

# ---------------------------------------------------------------------------------------------------------

N = int(input())
A = list(map(int, input().split()))
l, r = map(int, input().split())
S = [0] + list(accumulate(A))

ans = S[r] - S[l]
print(ans)
