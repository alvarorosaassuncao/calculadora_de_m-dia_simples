#CALCULADORA DE MÉDIA SIMPLES


nota1= int(input('Digite a nota 1:'))
nota2= int(input('Digite a nota 2:'))
media= (nota1 + nota2) / 2

if media <= 4:
  print('Você ficou com {} de média e infelizmente está reprovado'.format(media))

elif media > 6:
  print('Parabéns, você ficou com {} de média e está aprovado!'.format(media))
  
elif media == 5:
  print('Você ficou com {} de média e está de recuperação'.format(media))

