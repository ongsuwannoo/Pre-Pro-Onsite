"""Fibonacci V.2"""
def main():
    """doc"""
    num = int(input())
    lit = [0, 1]
    for _ in range(num):
        nextt = lit[0]+lit[1]
        lit[0] = lit[1]
        lit[1] = nextt
    print(lit[0])

main()
