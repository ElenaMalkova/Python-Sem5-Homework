# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

path = "rle_input.txt"
data = open(path, "r")
for line in data:
    print(f"Исходная строка: {line}")
data.close()

res = list(line) #превращаем строку в список строк сплитом
unique_symbols = [res[0]] #создаем список уникальных значений, где уже лежит нулевой элемент списка
symbol_count = [] #создаем список, где будем перечислять кол-во повторяющихся элементов
count = 1 #поскольку в списке уникальных значений уже лежит 1 элемент

for i in range(1, len(res)):
    if res[i] == res[i-1] and i != len(res)-1: # элемент i равен предыдущему и не последний в строке
        count +=1
    elif res[i] == res[i-1] and i == len(res)-1: # элемент i равен предыдущему и последний в строке
        count +=1
        symbol_count.append(count)      
    elif res[i] != res[i-1] and i == len(res)-1: # элемент i не равен предыдущему и последний в строке
        count +=1
        symbol_count.append(count)
    elif res[i] != res[i-1] and i != len(res)-1: # элемент i не равен предыдущему и не последний в строке
        unique_symbols.append(res[i])
        symbol_count.append(count)
        count = 1

rle = zip(symbol_count, unique_symbols) # Для вывода результата сжатия используется кортеж (print(tuple(rle))

rle_lst = [] 
for i in rle:               # Преобразование кортежа в список
    rle_lst.append(i[0])
    rle_lst.append(i[1])

print("Результат сжатия: " + "".join(map(str,rle_lst))) # Преобразуем список в строку при помощи join

def new_string(symbol, count):  # Функция умножения строки на число (из лекции 3)
    return symbol*count

rle_output = list(map(new_string, unique_symbols, symbol_count)) # В функцию умножения на число при помощи map кладем списки уникальных значений и количества их повторений
rle_output = "".join(map(str,rle_output))  # Преобразуем список в строку при помощи join
print("Результат восстановления: " + rle_output)

with open ("rle_output.txt", "w") as data:  #Записываем результат в новый файл
    data.write(rle_output)
    

