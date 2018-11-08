""" [Extra] FirstROR """
def main():
    ''' input '''
    sentence = input()
    if "mak" in sentence and "ror" in sentence and "first" in sentence:
        print("P'First ror mak mak!!")
    elif ("ror" in sentence or "first" in sentence) and "mak" in sentence:
        print("I think so!!")
    elif "first" in sentence and "ror" in sentence:
        print("I'm so First!!")
    else:
        print("First == ror -> is always True!!")


main()
