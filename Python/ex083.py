k = str(input('Digite uma expressão:'))
print(k.count("("))
print(k.count(")"))
print(k)
if k.count("(") == k.count(")"):
    if k.index('(') >k.index(")"):
        print('algo errado parenteses inicial incorreto')
    elif k.rindex('(') > k.rindex(')'):
        print('algo deu errado parenteses final incorreto')
    else:
        print('tudo ok com os parentes')
else:
    print('algo errado no numero de parenteses')