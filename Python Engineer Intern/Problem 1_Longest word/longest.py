


def findlongestword():

    file = open("twain.txt", "r")
    paragraph = file.read().split("\n")

    maxlen = -1
    longestword = ""
    for para in paragraph:
        if len(para) > maxlen:
            maxlen = len(para)
            maxpara = para
            maxpara.split()
            parawords = maxpara.split()

            longwordlen = -1
            for longw in parawords:
                if len(longw) > longwordlen:
                    longwordlen = len(longw)
                    longestword = longw
    print(longestword)



if __name__ == '__main__':
    findlongestword()