import pandas as pd
import numpy as np
def escrita(xs_bissec, xs_mil, xs_newton, xs_secante, xs_regula):
    k_max = max(len(xs_bissec), len(xs_mil), len(xs_newton), len(xs_secante), len(xs_regula))
    
    k = list(range(1, k_max + 1))
    
    listas_de_xizes = [
        list(xs_bissec),
        list(xs_mil),
        list(xs_newton),
        list(xs_secante),
        list(xs_regula)
    ]
    #deixar todas as matrizes do tamanho igual com NaN    
    for lista in listas_de_xizes:
        while len(lista) < k_max:
            lista.append(np.nan)
    
    dados = {
        "K" : k,
        "X's_Bisseccao": listas_de_xizes[0],
        "X's_Mil": listas_de_xizes[1],
        "X's_Newton": listas_de_xizes[2],
        "X's_Secante": listas_de_xizes[3],
        "X's_RegulaFalsi": listas_de_xizes[4]
    }

    df = pd.DataFrame(dados)
    
    print(df)
    
    nome_arquivo = "resultados.txt"
    df.to_csv(nome_arquivo, index=False)
  