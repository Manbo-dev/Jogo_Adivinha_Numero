import random
import os
os.system("clear")
num=random.randrange(1,10)
erro=0
while 1:
    escolhido=int(input("Digite um número escolhido: "))
    if escolhido>num:
        print("O número é menor!!!")
        erro+=1
    elif escolhido<num:
        print("O numero é maior!!!")
        erro+=1
    elif escolhido==num:
        print("Parabéns, você acertou:")
        break


