#Задача 1
file = open('lines.txt', encoding='utf-8')
print(set(file.readlines()).pop())
file.close()

#Задача 2
file = open('prices.txt', mode = 'r')
lst = file.readlines()
result = float(0)
for item in lst:
    subitem = item.split()
    result += (float(subitem[1]) * float(subitem[2]))
    print(result)
    file.close()

#Задача 3
with open("lines.txt", "r") as file:
    lines = file.readlines()
even_lines = []
odd_lines = []
for index, line in enumerate(lines):
    if index % 2 == 0:
        even_lines.append(line)
else:
    odd_lines.append(line)
for line in even_lines:
    print(line)
for line in odd_lines:
    print(line)
  
#Задача 4
with open("words.txt", "r") as f:
    words = f.read().split("\n")

max_length = -1
longest_words = []

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_words = [word]
    elif len(word) == max_length:
        longest_words.append(word)

print(longest_words)

#Задача 5
import os
import math
def human_file_size(size_bytes):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    i = 0
    while size_bytes > 1024:
        size_bytes /= 1024
        i += 1
    return f"{round(size_bytes)} {sizes[i]}"
file_path = 'input.txt'
size_bytes = os.stat(file_path).st_size
print(f"Размер файла: {human_file_size(size_bytes)}")
