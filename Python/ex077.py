palavras = ('tupla', 'com', 'varias', 'palavras', 'sem', 'acento')
for i in palavras:
    print(f'\nA palavra {i.upper()} tem ',end=" ")
    for l in i:
        if l in 'aeiou':
            print(l, end=" ")

