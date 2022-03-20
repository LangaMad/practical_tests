with open('enemy.txt',"r", encoding ="utf-8" ) as infile:
    words=0
    characters=0
    for line in infile:
        wordslist=line.split()
        # print(wordslist)
        words=words+len(wordslist)
        characters += sum(len(word) for word in wordslist)
        # print(characters)
print(words)
print(characters)