from datetime import datetime as dt
matrix = {}
canos = int
matrix['Contribuinte'] = str(input("Nome: ")).upper()
matrix['Nascimento'] = int(input('Ano de nascimento: (AAAA) '))
matrix['Carteira'] = int(input('Nº da CTPS: (0 caso nao tenha) '))
if matrix['Carteira'] != 0:
    matrix['anoc'] = int(input('Ano de contatração: AAAA '))
    matrix['salario'] = float(input('Salário: R$'))
    canos = dt.today().year - matrix['anoc']
idade = dt.today().year - matrix['Nascimento']
apos = 35 - canos
print(f"{matrix['Contribuinte']} tem {idade} anos e irá se aposentar aos {idade + apos}")
print(f'Seus dados: {matrix}')