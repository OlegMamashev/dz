import sys
sys.setrecursionlimit(2000)


def stirling(n, k):
    if n < k or k == 0:
        return 0
    if n == k:
        return 1
    if n > k > 0:
        return stirling(n-1, k-1) + (n-1)*stirling(n-1, k)


a = stirling(5, 4)

if a == 0:
    print("No solution")
else:
    print(f"Количество комбинаций - {a}")
