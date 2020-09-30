def no_dups(s):
    count = {}
    word = ''

    for c in s:
        if c.isalpha():
            c = c.lower()
            word += c
        else:
            if word not in count:
                count[word] = True

            
            word = ''
    if word != '':
        if word not in count:
            count[word] = True

    count_list = list(count.items())

    final = ''
    for i in count_list:
        final += i[0]
        final += ' '
    
    final = final.strip()
    return final

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))