""" [Extra] Bon Appetit """
def main():
    ''' input '''
    chilli = int(input())
    level = input()
    want = int(input())
    if level == "MILD":
        level = 1000
    elif level == "MEDIUM":
        level = 2000
    elif level == "SPICY":
        level = 3000
    want *= level
    if chilli >= want:
        print("Enough")
        print(chilli - want)
    else:
        print("Not Enough")

main()
