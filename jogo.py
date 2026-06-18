print("********************************")
print("bom vindo ao jogo de adivinhaçao")
print("********************************")

numerosecreto = 40

chute+input("digite o seu numero")
print("voce  digitou: ", chute )

chutenumero = int(chute)

acertou = chutenumero == numerosecreto
maior = chutenumero > numerosecreto
menor = chutenumero < numerosecreto

#se voce digitar qualquer numero vou verificar se acertou ou errou
if(numerosecreto == chutenumero):
    print("voce acertou!")
elif(maior):
    print("voce errou! o seu chute foi maior que o numero secreto.")
elif(menor):
    print("voce errou! o seu chute foi menor que o numero secreto.")

print("fim de jogo")