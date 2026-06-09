print("--- ALUGUEL DE FILMES ---")
nome = input("Digite seu nome: ")
cpf = int(input("Digite seu cpf: "))
idade = int(input("digite sua idade: "))
plano_usuario = input("Digite seu plano bronze,prata ou ouro...").lower()

if plano_usuario == "bronze" :
    print("Forrest Gump",
    "Toy Story",
    "O Rei Leão",
    "Jurassic Park",
    "Titanic",
    "Harry Potter e a Pedra Filosofal",
    "De Volta para o Futuro")
if plano_usuario == "prata" and idade >= 18 :
    print("Matrix","Gladiador","Os Vingadores" "O Exorcista","It — A Coisa")

if plano_usuario == "ouro" and idade >= 18 :
    print("Interestelar","Clube da Luta","A Origem","O Exorcista","It — A Coisa")

elif plano_usuario == "ouro" or "prata" and  idade <= 18 :
    print("Existem alguns filmes que são muito pesados para você !")