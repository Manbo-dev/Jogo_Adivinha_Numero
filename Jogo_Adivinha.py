import random
import os
os.system("clear")
num=random.randrange(1,10)
erro=0
while 1:
    if erro==3:
        print("Você perdeu!!")
        print(f"O numero era {num}")
        break
    escolhido=int(input("Digite um número escolhido: "))
    os.system("clear")
    if escolhido>num:
        print("O número é menor!!!")
        erro+=1
        print(f"Erros {erro}")
    elif escolhido<num:
        print("O numero é maior!!!")
        erro+=1
        print(f"Erros {erro}")
    elif escolhido==num:
        print("Parabéns, você acertou:")
        break
print("Fim")

