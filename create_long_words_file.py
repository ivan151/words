words = open('words.txt','r').readlines()
long_words = []
for word in words:
    if len(word) > 8:
        long_words.append(word)

with open('long_words.txt','w+') as lw:
    for word in long_words:
        lw.write(word)
lw.close()