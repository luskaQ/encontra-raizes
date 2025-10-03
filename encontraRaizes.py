from math import *
import os
import leituraFuncao
import escritaResultados

funcao_compilada = leituraFuncao.ler_funcao()
derivada_compilada = leituraFuncao.ler_derivada()
phi_compilado = leituraFuncao.ler_phi()
a_compilado, b_compilado = leituraFuncao.ler_intervalo()
precisao_compilada = leituraFuncao.ler_precisao()
x0_compilado, x1_compilado = leituraFuncao.ler_x0_x1()
max_iter_compilado = leituraFuncao.ler_num_max_iter()

xs_bissec = []
xs_mil = []
xs_newton = []
xs_secante = []
xs_regulaFalsi = []

def f(x):
    return eval(funcao_compilada)
    #return exp(-x**2) - cos(x)
def derivada_f(x):
    return eval(derivada_compilada)
def phi(x):
    return eval(phi_compilado)

def bisseccao(a,b, precisao, n):
    k = 0
    if(fabs(b-a) < precisao):
        raiz = a
        xs_bissec.append(a)
    else:
        while(fabs(b-a) > precisao and k < n):
            k = k+1
            finicio = f(a)
            meio = (a+b)/2
            fmeio = f(meio)
            if(fmeio * finicio < 0):
                b = meio
            else:
                a = meio
            xs_bissec.append(a)
        raiz = a
    print('\n',"Raiz de f(x) = ", raiz)
    print('\n',"Iteracoes = ", k)
    if k == n:
        xs_bissec.append("NUM MAX DE ITERACOES ATINGIDO")

def mil(x,precisao, n):
    k = 0
    x_ant = x
    if(fabs(f(x)) < precisao):
        raiz = x
        xs_mil.append(x)
    else:
        while(fabs(f(x)) > precisao or fabs(x_ant-x) > precisao and k < n):
            x_ant = x
            x = phi(x)
            k+= 1
            xs_mil.append(x)
    raiz = x
    print('\n',"Raiz de f(x) = ", raiz)
    print('\n',"Iteracoes = ", k) 
    if k == n:
        xs_mil.append("NUM MAX DE ITERACOES ATINGIDO")
         
def newton(x0, precisao, n):
    k = 0
    f_de_x = f(x0)
    if(fabs(f_de_x) < precisao):
        raiz = x0
        xs_newton.append(x0)
    else:
        f_de_x_linha = derivada_f(x0)
        x1 = x0 - (f_de_x/f_de_x_linha)
        f_de_x = f(x1)
        k += 1
        xs_newton.append(x1)
        while((fabs(f_de_x) > precisao or fabs(x1 - x0) > precisao) and k < n):
            k += 1
            x0 = x1
            f_de_x = f(x0)
            f_de_x_linha = derivada_f(x0)
            x1 = x0 - (f_de_x/f_de_x_linha)
            xs_newton.append(x1)
        raiz = x1
    print('\n',"Raiz de f(x) = ", raiz)
    print('\n',"Iteracoes = ", k)   
    if k == n:
        xs_newton.append("NUM MAX DE ITERACOES ATINGIDO")
               
def secante(x0, x1, precisao, n):
    k= 0
    if(fabs(f(x0)) < precisao):
        raiz = x0
        xs_secante.append(x0)
    elif(fabs(f(x1)) < precisao):
        raiz = x1
        xs_secante.append(x1)
    else:
        while True:
            k += 1
            x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)- f(x0)))
            x0 = x1
            x1 = x2
            xs_secante.append(x2)
            if(fabs(f(x2)) < precisao or k >= n):
                raiz = x2
                break
    print(f"Raiz de f(x) = {raiz}")
    print(f"Numero de iteracoes: {k}")
    if k == n:
        xs_secante.append("NUM MAX DE ITERACOES ATINGIDO")

def regulaFalsi(a, b, precisao, n):
    k = 0
    if(fabs(b-a) < precisao):
        raiz = a
        xs_regulaFalsi.append(a)
    elif (fabs(f(a)) < precisao):
        raiz = a
        xs_regulaFalsi.append(a)
    elif (fabs(f(b)) < precisao):
        raiz = b
        xs_regulaFalsi.append(b)
    else:
        while True:
            k += 1
            numerador = (a*f(b)) - (b*f(a))
            denominador = f(b) - f(a)
            x = numerador/denominador
            m = f(a)
            xs_regulaFalsi.append(x)
            if(fabs(f(x)) < precisao or k > n):
                raiz = x
                break
            if(m*f(x) > 0):
                a = x
            else:
                b = x
            if(fabs(b-a) < precisao):
                raiz = x
                break
    print(f"Raiz de f(x) = {raiz}")
    print(f"Numero de iteracoes: {k}")
    if k == n:
        xs_regulaFalsi.append("NUM MAX DE ITERACOES ATINGIDO")
                    
            
  

def saida_info():
    print(f"f(x) = {funcao_compilada}f'(x) = {derivada_compilada}phi(x) = {phi_compilado}")
    print(f"Intervalo = [{a_compilado} ; {b_compilado}]")
    print(f"Precisao = {precisao_compilada}")
    print(f"X0 = {x0_compilado}, X1 = {x1_compilado} \n")

def clear_tela():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

clear_tela()
saida_info()
input("Para calcular as raizes da função acima, digite enter")
bisseccao(a_compilado, b_compilado, precisao_compilada, max_iter_compilado)
mil(x0_compilado, precisao_compilada, max_iter_compilado)
newton(x0_compilado, precisao_compilada, max_iter_compilado)
secante(x0_compilado, x1_compilado, precisao_compilada, max_iter_compilado)
regulaFalsi(a_compilado, b_compilado, precisao_compilada, max_iter_compilado)
print("Calculo concluido, escrevendo resultados no arquivo...")

escritaResultados.escrita(xs_bissec, xs_mil, xs_newton, xs_secante, xs_regulaFalsi)


