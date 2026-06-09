print("--- ALUGUEL DE FILMES ---")
nome = input("Digite seu nome: ")
cpf = int(input("Digite seu cpf: "))
idade = int(input("digite sua idade: "))
plano_usuario = input("Digite seu plano bronze,prata ou ouro...")
if plano_usuario.lower == "bronze" and idade >= 18:
    print("teste")
elif plano_usuario.lower == "bronze" and idade < 18:
    print("teste")
if plano_usuario.lower == "prata" and idade >= 18:
    print("Matrix","Gladiador","Os Vingadores")