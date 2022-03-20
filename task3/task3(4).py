w = input("Введите текст: ")
up = []
low = []
for text in w:
    if text == text.upper():
        up.append(text)
    elif text == text.lower():
        low.append(text)

num_len = len(w)
num_up = len(up)
num_low = len(low)

prc_up = (num_up*100)//num_len
prc_low = (num_low*100)//num_len

print("Процент заглавных букв в тексте ",prc_up,'%')
print("Процент строчных букв в тексте ",prc_low,"%") 