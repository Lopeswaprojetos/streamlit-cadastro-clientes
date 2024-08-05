nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
print(nome)
if int(idade) >= 17:
    print("Voce pode entrar na festa!")
else:
    print("Voce nao pode entrar na festa!")

with open("base_dados.csv", "a") as arquivo:
    arquivo.write(f"Seja bem vindo (a) {nome}\n")