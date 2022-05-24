status = {'nome':input('Digite o nome do aluno: '), 'média': float(input('Digite a media do aluno: '))}
if status['média'] >= 7:
    status['situação'] = 'Reprovado'.upper()
elif 5 <= status['média'] < 7:
    status['situação'] = 'em Recuperação'.upper()
else:
    status['situação'] = 'Aprovado'.upper()
print("==="*10)
print(f"O aluno {status['nome']} está teve a média {status['média']} portanto está {status['situação']}")
