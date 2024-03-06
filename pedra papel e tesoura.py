import random
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
sinais = [pedra, papel, tesoura]
nome = input("Qual o seu nome?\n> ")
nome_adv = input("Quem você deseja enfrentar?\n> ")
escolha_user = int(input("O que você escolhe?\n\n0 - Pedra\n1 - Papel\n2 - Tesoura\n> "))
if escolha_user >= 3 or escolha_user < 0:
    print("Escolha um número de 0 a 2!")
else:   
    print(sinais[escolha_user])
escolha_pc = random.randint(0, 2)

print(f"Escolha de {nome_adv}")
print(sinais[escolha_pc])

if escolha_user == 0 and escolha_pc == 2:
    print(nome +  " ganhou!")
elif escolha_pc == 2 and escolha_user == 0:
    print(nome + " ganhou!")
elif escolha_pc == 2 and escolha_user == 1:
    print(nome_adv + " ganhou!")
elif escolha_pc == 1 and escolha_user == 0:
    print(nome_adv + " ganhou!")
elif escolha_pc == 1 and escolha_user == 2:
    print(nome + " ganhou!")
elif escolha_pc == 0 and escolha_user == 1:
    print(nome + " ganhou!")
elif escolha_pc == 0 and escolha_user == 2:
    print(nome_adv + " ganhou!")
elif escolha_pc > escolha_user:
    print(nome_adv + " ganhou!")
elif escolha_user > escolha_pc:
    print(nome_adv + " ganhou!")
elif escolha_pc == escolha_user:
    print("Empate!")
elif escolha_user >= 3 or escolha_user < 0:
    print("Escolha um número de 0 a 2!")



