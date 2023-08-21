n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')
