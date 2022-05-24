a = input('Digite a uma frase:  ').upper().strip()
jun = list(''.join(a.split()))
'''print(jun)
print(list(reversed(jun)))'''
if jun == list(reversed(jun)):
    print("palindromo")
else:
    print('nao é palindromo')