def main():
    wordlist = []
    with open('wl.txt','r') as wlfile:
        for line in wlfile:
            wordlist.append(line.strip())

    password = "mustang1234"

    for word in wordlist:
        hashing = minienc(word)
        if hashing == password:
            break
    print(hashing)






def minienc(text):
    return text + "1234"





if __name__ == '__main__':
    main()