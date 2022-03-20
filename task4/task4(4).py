with open('enemy.txt',"r", encoding ="utf-8" ) as file:
    text = file.readlines()
    characters = 0
    words = list()
    
    for i in text:
        word_list = i.split()
        characters += sum(len(word) for word in word_list)
        # print(characters)
        if "the" in word_list:
            words.append(word_list)
        
prc_words = len(words)
result = prc_words*100/characters
print(f"{result} %")



