""" Music List """
def compare(nub):
    """ for compare """
    return len(nub)

def main():
    """ input """
    music2 = []
    music3 = []
    nub = []
    music = input().split(", ")
    music.sort(key=compare, reverse=True)
    music2 = music

    for i in range(len(music)):
        music3 += [music[i].lower()]

    for i in range(-1, -len(music3)-1, -1):
        if music3[i] in music3[0:i]:
            nub.append(i)
    nub.reverse()

    for i in range(len(nub)):
        music2.pop(nub[i])

    for i in range(len(music2)):
        print("%d.%s"%(i+1, music2[i]))

main()
