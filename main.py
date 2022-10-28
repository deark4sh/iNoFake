import random as r, string as st, pandas as pd, unidecode as uni


print("  _   _  _         ___          _         \n (_) | \| |  ___  | __|  __ _  | |__  ___ \n | | | .` | / _ \ | _|  / _` | | / / / -_)\n |_| |_|\_| \___/ |_|   \__,_| |_\_\ \___| \n")
print(" Hey, Bem-vind@! iNoFake v0.6 by DearK4sh.")
var=str(input(">>> "))
 
def numero_celular():
    print(f"Celular:            +55 ({r.randint(11, 99)}) 9{r.randint(1000, 9999)}-{r.randint(1000, 9999)}")

def numero_cpf():
    print(f"CPF:                {r.randint(100, 999)}.{r.randint(100, 999)}.{r.randint(100, 999)}-{r.randint(10, 99)}")

def numero_identidade():
    print(f"RG:                 {r.randint(10, 99)}.{r.randint(100, 999)}.{r.randint(100, 999)}-{r.randint(0, 9)}")

def conta_bancaria():
    uf=["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP", "TO"]
    print(f"Conta Bancaria:     Banco do Brasil {r.randint(100000, 999999)}-{r.randint(0, 9)}, Agência: {r.randint(1000, 9999)}, UF: {r.choice(uf)}")

def cartao_credito():
    print(f"Cartão de Crédito:  {r.randint(1000, 9999)} {r.randint(1000, 9999)} {r.randint(1000, 9999)} {r.randint(1000, 9999)}, Validade: {r.randint(1, 12)}/{r.randint(2023, 2050)}, CVV: {r.randint(100, 999)}")

def senha():
    senha=""
    for x in range(13): senha=senha+r.choice(st.ascii_letters+st.digits+st.punctuation)
    print(f"Senha:              {senha}")

def signo():
    signo=["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
    print(f"Signo:              {r.choice(signo)}")

def cor_favorita():
    cor=["Amarelo", "Vermelho", "Roxo", "Azul", "Rosa", "Preto", "Branco", "Marrom", "Cinza", "Verde", "Violeta", "Gosta de todas as cores."]
    print(f"Cor Favorita:       {r.choice(cor)}")

def manual():
    print("""iNoFake (v0.6) é uma ferramenta que gera dados aleatórios para a criação de documentos e até perfis/identidades completas.
Você pode usar algum dos parâmetros abaixo para ter o que deseja:
-p	para gerar um perfil completo, com todas as informações abaixo.
-d	para gerar dados isolados, usando os seguintes parâmetros:
	-cl	para gerar um número celular.
	-cp	para gerar um número de CPF.
	-id	para gerar uma identidade.
	-se	para gerar uma senha.
	-cb	para gerar uma conta bancaria.
	-ct	para gerar um cartão de crédito.
Se você curtiu essa ferramenta, contribua para o aperfeiçoamento dela no GitHub @DearK4sh/iNoFake!
Lembre-se: ética. A má utilização dos dados gerados é de total responsabilidade sua.""")

chars=["_", "-", ".", ""]

if var=="-p":
    print("Dados para o gênero masculino (-m) ou feminino (-f)?")
    var=str(input(">>> "))
    if  var=="-m":
        df=pd.read_excel(r"nms_mas.xls")
        nome=df["nome"]
        nome=r.choice(nome)
        sobrenome=df["sobrenome"]
        sobrenome=r.choice(sobrenome)
        provedor=df["provedor"]
        print(f"Nome Completo:      {nome} {sobrenome}")
        print(f"Email:              {uni.unidecode(str.lower(nome))}{r.choice(chars)}{uni.unidecode(str.lower(sobrenome))}{r.randint(195, 2050)}@{r.choice(provedor)}")
        senha()
        numero_celular()
        signo()
        cor_favorita()
        numero_cpf()
        numero_identidade()
        conta_bancaria()
        cartao_credito()
    elif var=="-f":
        df=pd.read_excel(r"nms_fem.xls")
        nome=df["nome"]
        nome=r.choice(nome)
        sobrenome=df["sobrenome"]
        sobrenome=r.choice(sobrenome)
        provedor=df["provedor"]
        print(f"Nome Completo:      {nome} {sobrenome}")
        print(f"Email:              {uni.unidecode(str.lower(nome))}{r.choice(chars)}{uni.unidecode(str.lower(sobrenome))}{r.randint(195, 2050)}@{r.choice(provedor)}")
        senha()
        numero_celular()
        signo()
        cor_favorita()
        numero_cpf()
        numero_identidade()
        conta_bancaria()
        cartao_credito()
    else:
        manual()
elif var=="-d":
    print("Ok, escolha um parâmetro!")
    var=str(input(">>> "))
    if var=="-cl":
        numero_celular()
    elif var=="-cp":
        numero_cpf()
    elif var=="-id":
        numero_identidade()
    elif var=="-se":
        senha()
    elif var=="-cb":
        conta_bancaria()
    elif var=="-ct":
        cartao_credito()
    else:
        manual()
else:
    manual()
