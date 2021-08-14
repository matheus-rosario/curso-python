#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
altura = float(input('Digite sua altura (ex: 1.80): '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
if int(imc) < 18.5:
  print(f'IMC {int(imc)}, Abaixo do Peso')
elif int(imc) >= 18.5 and int(imc) <= 25:
  print(f'IMC {int(imc)}, Peso Ideal')
elif int(imc) >= 25 and int(imc)<= 30:
  print(f'IMC {int(imc)}, Sobrepeso')
elif int(imc) >=30 and int(imc) <= 40:
  print(f'IMC int{imc}, Obesidade')
elif int(imc) > 40:
  print(f'IMC {int(imc)}, Obesidade Mórbida')