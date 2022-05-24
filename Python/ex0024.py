cidade = str(input('Em que cidade você nasceu?')).strip()
listacidade = cidade.capitalize().split()
print(listacidade[0]=="Santo")

print('santo' in  cidade)

print(cidade.find('santo'))