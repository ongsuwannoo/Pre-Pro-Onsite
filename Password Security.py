""" Password Security """
def main():
    ''' input '''
    password = input()
    score = 0
    #check len(password)
    if len(password) < 7:
        print("try again")
        password += input()
        if len(password) < 7:
            print("process terminated")
    #process
    if password.islower():
        score += 100
        print("3")
    if password.isupper():
        score += 85
        print("4")
    if password.isalnum():
        if password.isnumeric():
            score += 50
            print("1")
        if password.isalpha():
            score += 30
            print("2")
        else:
            score += 75
            print("5")
    #print
    if len(password) > 6:
        print("Password :", "*" * len(password))
        print(score)

main()
