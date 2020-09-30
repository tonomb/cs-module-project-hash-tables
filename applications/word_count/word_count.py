
unwanted = {'\"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[' ,']', '{' ,'}' '(', ')', '*', '^', '&', ' '}

def word_count(s):
    count = {}
    word = ''
    for c in s:
        if  c.isalpha() or c == "'":   # c not in unwanted or c == '':
            c = c.lower()
            word += c
        elif word == '':
            pass
        else:
            if word not in count:
                count[word] = 0

            count[word] +=1
            word = ''
    # catches last word 
    if word != '':
        if word not in count:
            count[word] = 0

        count[word] +=1

    return count
   


print(word_count("Hello    hello"))


if __name__ == "__main__":
    print(word_count(""))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))