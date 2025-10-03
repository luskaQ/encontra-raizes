from math import *
import re
import sympy as sp


# Definindo a variável simbólica
x = sp.symbols('x')

funcoes_conhecidas = {"sin", "cos", "tan", "exp", "log", "log10", "sqrt", "asin", "acos", "atan", "pow"}
arquivo_path = "func.txt" #caminho para o arquivo txt aqui
with open(arquivo_path, 'r') as arquivo:
    linhas_arquivo = arquivo.readlines()
pass
def adicionar_mult_antes_de_parenteses(match):
    nome = match.group(1)
    #se o grupo 1 estiver nas funcoes reconhecidas, retorna esse grupo sem alteracoes
    if nome in funcoes_conhecidas:
        return match.group(0)
    #se nao, retorna adicioando um asterisco
    else:
        return nome + "*("

def formatar_funcao(expressao : str):
    expressao = expressao.replace("phi(x)","")
    expressao = expressao.replace("f(x)","")
    expressao = expressao.replace("y","")
    expressao = expressao.replace("f'(x)","")
    expressao = expressao.replace("y'","")
    expressao = expressao.replace("dy/dx","")
    expressao = expressao.replace("=","")
    expressao = expressao.replace("tg", "tan")
    expressao = expressao.replace("sen", "sin")
    expressao = expressao.replace("e^", "exp")
    expressao = expressao.replace("^", "**")
    expressao = re.sub(r"\blog\b", "log10", expressao)
    expressao = expressao.replace("ln", "log")
    
    expressao = expressao.replace("xexp", "x*exp") #repetir isso para todas as funcoes conhecidas
    expressao = expressao.replace("xsin", "x*sin")
    expressao = expressao.replace("xcos", "x*cos")
    expressao = expressao.replace("xtan", "x*tan")
    expressao = expressao.replace("xsqrt", "x*sqrt")
    expressao = expressao.replace("xlog", "x*log")
    expressao = expressao.replace("xsqrt", "x*sqrt")
    expressao = expressao.replace("xasin", "x*asin")
    expressao = expressao.replace("xacos", "x*acos")
    expressao = expressao.replace("xatan", "x*atan")
    expressao = expressao.replace("xpow", "x*pow")



    #\blog\b é o padrao que procuramos, um log que esta entre limitadores de palavras (espacos, parenteses etc)
    #substituimos por log10
    
    expressao = expressao.replace("log10", "LOGDEZ") 
    expressao = re.sub(r"(\d)([a-zA-Z\(])", r"\1*\2", expressao) #ERRO AQUI
    expressao = expressao.replace("LOGDEZ", "log10") 
    #procuramos por um agrupamento de numeros seguidos por um agrupamento de caracteres ou parenteses
    expressao = re.sub(r"(\))\s*([a-zA-Z0-9\(])", r"\1*\2", expressao)
    #caso de (x-1)(x+1) ou (x)3 - fechamento de parenteses seguido por outra expressao, com verificacao de espaços 
    padrao_mult = r"([a-zA-Z0-9]+)(\()"
    #padrao de variavel/numero (group 1) seguido por abertura de parenteses
    expressao = re.sub(padrao_mult, adicionar_mult_antes_de_parenteses, expressao)
    #aqui é o caso de um numero/variavel multiplicando algo nos parenteses, o padrao_funcao garente que a
    #verificacao nao ocorrera caso seja encontrado alguma daquelas funcoes antes de uma abertura de parenteses
   
    expressao = re.sub(r"(\bexp)(-?\w+(?:\.\w+)?(?:\*\*[+\-]?\w+)?)", r"\1(\2)", expressao)
    #procuro um exp que nao esteja no meio de uma palavra, o capturo, e depois procuro: um sinal opcional, seguido
    #por um ou mais numeros/variaveis seguido por uma parte decimal opcional, seguido por mais um ** com sinal opcional

    
    expressao = expressao.replace(" ", "")

    return expressao


def ler_funcao():
    return formatar_funcao(linhas_arquivo[0]) #a funcao é a primeira linha do arquivo

def ler_derivada():
    return formatar_funcao(linhas_arquivo[1]) #a derivada da funcao é a segunda linha do arquivo

def ler_phi():
    return formatar_funcao(linhas_arquivo[2]) #phi é a terceira linha do arquivo

def ler_intervalo():
    intervalo_cru = linhas_arquivo[3] # o intervalo é a quarta linha do arquivo
    intervalo_cru = intervalo_cru.replace(";", ",")
    posicao_virgula = intervalo_cru.find(",")
    limite_inferior_cru = intervalo_cru[:posicao_virgula]
    limite_superior_cru = intervalo_cru[posicao_virgula:]

    limite_inferior_cru = limite_inferior_cru.replace("[", "")
    limite_superior_cru = limite_superior_cru.replace("]", "")

    limite_inferior_cru = limite_inferior_cru.replace(" ", "")
    limite_superior_cru = limite_superior_cru.replace(" ", "")

    limite_inferior_cru = limite_inferior_cru.replace(",", "")
    limite_superior_cru = limite_superior_cru.replace(",", "")

    return float(limite_inferior_cru), float(limite_superior_cru)

def ler_precisao():
    precisao_crua = linhas_arquivo[6] # precisao é a setima linha do arquivo
    precisao_crua = precisao_crua.replace("^","**")
    precisao_crua = precisao_crua.replace(".","*")
    precisao_crua = precisao_crua.replace(" ","")
    
    precisao = eval(precisao_crua)
    
    return precisao
def ler_x0_x1():
    x0_cru =linhas_arquivo[4]
    x1_cru =linhas_arquivo[5]
    
    x0_cru = x0_cru.replace(" ", "")
    x0_cru = x0_cru.replace("x0=", "")
    
    x1_cru = x1_cru.replace(" ", "")
    x1_cru = x1_cru.replace("x1=", "")

    return float(x0_cru), float(x1_cru)

def ler_num_max_iter():
    num_max_iter = linhas_arquivo[7] #A oitava linha do arquivo é o num max de iteracoes
    return int(num_max_iter)
    

#print(linhas_arquivo)

#print(ler_intervalo())
#print(ler_derivada())
#print(ler_precisao())
