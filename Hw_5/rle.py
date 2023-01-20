# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.

with open(r'Hw_5\test.txt', 'r') as data: 
    phrase = data.read()
encoded_phr = ''
count = 1

for i in range(len(phrase)-1):
    if phrase[i] == phrase[i + 1]:
        count += 1
    else:
        encoded_phr += str(count) + phrase[i]
        count = 1
else:
    encoded_phr += str(count) + phrase[i]
print(encoded_phr)
        
# Реализуйте RLE алгоритм: реализуйте модуль восстановления данных.

decoded_phr = ''

for i in range(len(encoded_phr)-1):
    if encoded_phr[i].isdigit():
        decoded_phr += encoded_phr[i+1]*int(encoded_phr[i])

print(decoded_phr)        

