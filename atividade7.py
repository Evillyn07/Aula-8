peso = float (input("Qual é o seu peso? (Kg)"))
altura = float(input("Qual é a sua altura? (M)"))
imc = peso / (altura ** 2)
print ("O seu IMC é {:.1f}" .format(imc))
if imc < 18.5:
    print ("Você está ABAIXO do peso.")

elif 18.5 < imc < 25:
    print ("Você está na faixa do peso IDEAL.")
elif 25 < imc < 30:
    print ("Você está em SOBREPESO.")
elif 30 < imc < 40:
    print ("Você está OBESO.")
elif imc > 40:
    print ("Você está em OBESIDADE MORBIDA. Se cuide!")