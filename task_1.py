# Напишите программу, удаляющую из текста все слова, содержащие "абв".

#Method

def concatenatio(lst):
    txt: str = ""
    for i in lst:
        txt += i + " "
    return txt

# Code

text = "ммм абв лсд гдр абв фрг абвы ддт абво лалала"
print(f"Исходная строка: {text}")
res = text.split(' ') #превращаем строку в список строк сплитом
res = list(filter(lambda i: "абв" not in i, res)) # фильтруем список, выбрасывая элементы с "абв"
new_text = concatenatio(res) # превращаем список в строку
print(f"Новая строка: {new_text}")