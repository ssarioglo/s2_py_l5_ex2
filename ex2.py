print("Введите слово на английском языке")
wrd = input()
# гласные
a = 0
e = 0
i = 0
o = 0
u = 0
sog = 0 # согласные
cnt = len(wrd) # находим длину введенного слова

for inc in range(0, cnt):
    wrdi = wrd[inc]                         # перебираем по порядку каждую букву введенного слова
    if wrd[inc] == 'a':                     # если попадается гласная, увеличиваем счетчик гласных
        a += 1
    elif wrd[inc] == 'e':
        e += 1
    elif wrd[inc] == 'i':
        i += 1
    elif wrd[inc] == 'o':
        o += 1
    elif wrd[inc] == 'u':
        u += 1
    else:
        sog += 1                            # если не попадается гласная - то считаем, что это согласная

print()
print("Во введенном слове:")
print()
print("Согласных:", sog)
gl = int(a) + int(e) + int(i) + int(o) + int(u)
print("Гласных всего:", gl)
if a == 0:                                  # по условию задачи, если 0 - то False
    a = False
if e == 0:
    e = False
if i == 0:
    i = False
if o == 0:
    o = False
if u == 0:
    u = False
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)