"""Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
da expressão (sintaxe).
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída
para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais."""

biblioteca1 = ["T", "F"]
biblioteca2 = [ r"\neg","(", ")", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "v", "x", "y", "z"]
biblioteca3 = [ "\dis", "\con", "\imp", r"\bimp"]

def Inicio():

    lista = []
    lista2 = []
    filename = input("Digite o nome do arquivo com a devida extensão (EX: Teste.txt):")
    with open(filename, "r") as file:
        line = file.readlines()
        numExp = int(line[0])
        for x in range(1, numExp + 1):
            Exp = line[x]
            lista.append(Exp)
    for x in range(0, len(lista)):
        Ver = TermosValidos(lista[x])
        if Ver == True:
            if ExpValida(lista[x]) == True:
                print("Válida")
            else:
                print("Inválida")
        else:
            print("Inválida")

def TermosValidos(Exp):
    lista3 = Exp.split(" ")
    for x in range(0, len(lista3)):
        if (lista3[x] not in biblioteca1) and (lista3[x] not in biblioteca2) and (lista3[x] not in biblioteca3):
            return False

        else:
            if ExpValida(lista3) == True:
                return True

            else:
                return False

def ExpValida(Exp):
    cont2 = 0
    for x in range(0, len(Exp)):

        if Exp[x] in biblioteca1 and Exp[x + 1] in biblioteca1:
            return False

        elif Exp[x] in biblioteca2 and Exp[x + 1] in biblioteca2:
            return False

        elif Exp[x] == r"\neg" and ((Exp[x + 1] in biblioteca3) or (Exp[x] == ")")):
            return False

        elif Exp[x] == r"\dis" and (Exp[x + 1] in biblioteca3):
            return False

        elif Exp[x] == r"\con" and (Exp[x + 1] in biblioteca3):
            return False

        elif Exp[x] == r"\imp" and (Exp[x + 1] in biblioteca3):
            return False

        elif Exp[x] == r"\bimp" and (Exp[x + 1] in biblioteca3):
            return False

        elif Exp[x] == "(" and Exp[x + 1] == ")":
            return False

        if Exp[x] == "(":
            cont2 = cont2 + 1
        elif Exp[x] == ")":
            cont2 = cont2 - 1
            if cont2 < 0:
                return False

    return True


Inicio()