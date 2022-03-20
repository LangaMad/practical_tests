
def get_string():
    string = "thequickbrownfoxjumpsoverthelazydog"
    dic = dict()
    for words in string:
        if words in dic.keys():
            dic[words] = dic[words]+1
        else:
            dic[words] = 1
    return dic

print(get_string())
