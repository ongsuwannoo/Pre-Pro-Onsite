""" [Extra] IT-REDMARE """
def main():
    ''' input '''
    num = int(input())
    for _ in range(num):
        print(("*****" * num) + (" " * num) + ("*****" * num) + \
            ("     " * num) + ("****" * num) + ("  " * num) + ("*****" * num) + \
            (" " * num) + ("***" * num) + ("   " * num) + ("*" * num) + \
            ("   " * num) + ("*" * num) + ("   " * num) + ("*" * num) + \
            ("   " * num) + ("****" * num) + ("  " * num) + ("*****" * num))

    for i in range(num+1):

        if i < num:
            print(("  " * num) + ("*" * num) + ("     " * num) + ("*" * num) + \
                ("       " * num) + ("*" * num) + ("   " * num) + ("*" * num) + \
                (" " * num) + ("*" * num) + ("     " * num) + ("*" * num) + ("  " * num) + \
                ("*" * num) + ("  " * num) + ("**" * num) + (" " * num) + ("**" * num) + \
                ("  " * num) + ("*" * num) + (" " * num) + ("*" * num) + ("  " * num) + \
                ("*" * num) + ("   " * num) + ("*" * num) + (" " * num) + ("*" * num))

        elif i == num:
            for _ in range(i):
                print(("  " * num) + ("*" * num) + ("     " * num) + ("*" * num) + \
                    ("   " * num) + ("***" * num) + (" " * num) + ("****" * num) + \
                    ("  " * num) + ("*****" * num) + (" " * num) + ("*" * num) + \
                    ("   " * num) + ("*" * num) + (" " * num) + ("*" * num) + (" " * num) + \
                    ("*" * num) + (" " * num) + ("*" * num) + (" " * num) + ("*****" * num) + \
                    (" " * num) + ("****" * num) + ("  " * num) + ("*****" * num))

    for i in range(num):
        print(("  " * num) + ("*" * num) + ("     " * num) + ("*" * num) + \
            ("       " * num) + ("*" * num) + (" " * num) + ("*" * num) + ("   " * num) + \
            ("*" * num) + ("     " * num) + ("*" * num) + ("  " * num) + ("*" * num) + \
            ("  " * num) + ("*" * num) + ("   " * num) + ("*" * num) + (" " * num) + \
            ("*" * num) + ("   " * num) + ("*" * num) + (" " * num) + ("*" * num) + \
            (" " * num) + ("*" * num) + ("   " * num) + ("*" * num))

    for _ in range(num):
        print(("*****" * num) + ("   " * num) + ("*" * num) + ("       " * num) + ("*" * num) + \
            ("  " * num) + ("*" * num) + ("  " * num) + ("*****" * num) + (" " * num) + \
            ("***" * num) + ("   " * num) + ("*" * num) + ("   " * num) + ("*" * num) + \
            (" " * num) + ("*" * num) + ("   " * num) + ("*" * num) + (" " * num) + ("*" * num) + \
            ("  " * num) + ("*" * num) + ("  " * num) + ("*****") * num)

main()
