def limpa_texto(cad):
    """Remove carateres brancos de uma cadeia de carateres.

    Args:
        cad (str): cadeia de carateres qualquer

    Returns:
        str: cadeia de carateres limpa
    """    
    return " ".join(cad.split())                      

def corta_texto(cad, coluna_l):
    """Devolve duas cadeias de carateres, a primeira com um comprimento até à largura
    fornecida e a segunda contendo o resto do texto.

    Args:
        cad (str): cadeia de carateres limpa
        coluna_l (int): largura da coluna

    Returns:
        tuple: tuplo constituído por duas cadeias de carateres
    """    
    palavras = cad.split()             
    str1 = str2 = ""
    for p in range(len(palavras)):
        if p == 0:
            str1 = palavras[p]
        elif len(str1) + 1 + len(palavras[p]) > coluna_l:                     
            str2 = " ".join(palavras[p:])
            return (str1, str2) 
        else:
            str1 += " " + palavras[p]
    return (str1, str2) 

def insere_espacos(cad, coluna_l):
    """Devolve uma cadeia de carateres de comprimento igual à largura da coluna formada
     pela cadeia original, com espacos entre palavras conforme descrito, ou a cadeia de 
     comprimento igual à largura da coluna formada pela cadeia original seguida de espaços.

    Args:
        cad (str): cadeia de carateres limpa
        coluna_l (int): largura da coluna

    Returns:
        str: cadeia de carateres de comprimento igual à largura da coluna
    """    
    espacos = coluna_l - len(cad)
    new_cad = ""
    if cad.count(" ") == 0:
        new_cad = cad.ljust(coluna_l)
    else:
        cad_list = cad.split()
        for c in range(len(cad_list) - 1):
            cad_list[c] = cad_list[c] + ((espacos // (len(cad_list) - 1)) + 1) * " "
        for w in range(espacos % (len(cad_list) - 1)):
            cad_list[w] = cad_list[w] + " "
        for p in range(len(cad_list)):
            new_cad += cad_list[p]
    return new_cad

def justifica_texto(cad, coluna_l):
    """Recebe uma cadeia de carateres não vazia e um inteiro positivo e devolve um tuplo
    de cadeias de carateres justificadas.

    Args:
        cad (str): cadeia de carateres não vazia
        coluna_l (int): largura da coluna

    Raises:
        ValueError: Argumentos inválidos

    Returns:
        tuple:  tuplo de cadeias de carateres justificadas
    """    
    if type(cad) != str or cad == "" or type(coluna_l) != int or not\
         all (len(w) <= coluna_l for w in limpa_texto(cad).split()):
        raise ValueError("justifica_texto: argumentos invalidos")
    cad_limpa = limpa_texto(cad)
    cadeia_just, cad_resto = (), " "
    while cad_resto != "":                                                  
        cad_v2 = corta_texto(cad_limpa, coluna_l)
        cad_cortada,  cad_resto = cad_v2[0], cad_v2[1]
        if cad_resto == "":
            cadeia_just+= (str(cad_cortada).ljust(coluna_l), )
            return cadeia_just
        cadeia_just += (insere_espacos(cad_cortada, coluna_l), )
        cad_limpa = cad_resto
        
def calcula_quocientes(dict_votos, deputados):
    """Devolve um dicionário com as mesmas chaves do dicionário argumento contendo
     a lista (de comprimento igual ao número de deputados) com os quocientes
    calculados com o método de Hondt, ordenados em ordem decrescente.

    Args:
        dict_votos (dict): dicionário com os votos apurados num círculo
        deputados (int): número de deputados

    Returns:
        dict: dicionário em que as chaves são partidos e os valores são os quocientes
    """    
    quocientes = {}
    for partido in dict_votos:
        for num in range(1, deputados + 1):
            if partido not in quocientes:
                quocientes[partido] = [(dict_votos[partido] / num)]
            else:
                quocientes[partido] += [(dict_votos[partido] / num )]
    return quocientes

def atribui_mandatos(dict_votos, deputados):
    """Devolve a lista ordenada de tamanho igual ao número de deputados 
    contendo as cadeias de carateres dos partidos que obtiveram cada mandato, ou seja,
    a primeira posição da lista corresponde ao nome do partido que obteve o primeiro
    deputado, a segunda ao partido que obteve o segundo deputado e assim sucessivamente.

    Args:
        dict_votos (dict): votos apurados num círculo
        deputados (int): número de deputados

    Returns:
        list: lista ordenada de partidos que obtiveram mandato
    """    
    mandatos = []
    quocientes = calcula_quocientes(dict_votos, deputados)
    for i in range(deputados):
        votenum = 0
        for partido in quocientes:
            if quocientes[partido][0] > votenum:
                votenum, partidocache = quocientes[partido][0], partido
            if quocientes[partido][0] == votenum and dict_votos[partido] <=\
                dict_votos[partidocache]:
                    partidocache = partido
        mandatos += [partidocache]
        quocientes[partidocache].pop(0)
    return mandatos

def obtem_partidos(info_eleicoes):
    """Obtém uma lista por ordem alfabetica com o nome de todos os 
    partidos que participaram nas eleições. 

    Args:
        info_eleicoes (dict): informação sobre eleições num território

    Returns:
        list: lista dos partidos que participaram nas eleições
    """    
    partidos = []
    for territorio in info_eleicoes:
        for partido in info_eleicoes[territorio]["votos"]:
            if partido not in partidos:
                partidos += [partido]
    return sorted(partidos)

def metodo_hondt_erros(info_eleicoes):  
    if type(info_eleicoes) != dict or info_eleicoes == {} or not all(type(key) == str\
         for key in info_eleicoes.keys()):
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    for territorio in info_eleicoes:
        if type(info_eleicoes[territorio]) != dict or list(info_eleicoes[territorio].keys())\
             != ["deputados", "votos"] or type(info_eleicoes[territorio]["votos"]) != dict or \
                info_eleicoes[territorio]["votos"] == {} or type(info_eleicoes[territorio]\
                    ["deputados"]) != int or info_eleicoes[territorio]["deputados"] < 1 or not\
                        all(type(n) == int and n > 0 for n in list(info_eleicoes[territorio]\
                            ["votos"].values())) or not all(type(partido) == str  for partido\
                                in info_eleicoes[territorio]["votos"]):
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    else:
        return (info_eleicoes)
        
def obtem_resultado_eleicoes(info_eleicoes):
    """Devolve a lista ordenada de comprimento igual ao número total de
    partidos com os resultados das eleições. Cada elemento da lista é
    um tuplo de tamanho 3 contendo o nome de um partido, o número total de
    deputados obtidos e o número total de votos obtidos. A lista está ordenada
    por ordem descendente de acordo com o número de deputados obtidos e, em caso
    de empate, de acordo com o número de votos.

    Args:
        info_eleicoes (dict): dicionário com informação sobre eleições num território

    Returns:
        list: lista dos partidos que participaram nas eleições e resultados obtidos
    """    
    metodo_hondt_erros(info_eleicoes)
    partidos = obtem_partidos(info_eleicoes)
    deputados = votos = 0
    resultados = []
    for partido in partidos:         ##########  
        for territorio in info_eleicoes:
            mandatos = atribui_mandatos(info_eleicoes[territorio]["votos"], \
                info_eleicoes[territorio]["deputados"])
            if partido in mandatos or partido in (info_eleicoes[territorio]["votos"]):
                deputados += mandatos.count(partido)
                votos += info_eleicoes[territorio]["votos"][partido]
        res_partido = (partido, deputados, votos)
        deputados = votos = 0
        resultados += [(res_partido)]
    return(sorted(resultados, key = lambda x : x[2], reverse = True))

def produto_interno(vetor1, vetor2):
    """Calcula o produto interno de dois vetores com as mesmas dimensões.

    Args:
        vetor1 (tuple): tuplo de números
        vetor2 (tuple): tuplo de números 

    Returns:
        float: produto interno os vetores
    """    
    return float(sum(i1 * i2 for i1, i2 in zip(vetor1, vetor2)))

def verifica_convergencia(matriz, constantes, solucao, precisao):
    """A função retorna True caso o valor absoluto do erro de todas as equações
    seja inferior à precisão, |fi(x) − ci| < ϵ, e False caso contrário.

    Args:
        matriz (tuple): tuplo de tuplos, cada um representando uma linha da matriz quadrada A
        constantes (tuple): vetor das constantes
        solucao (tuple): solução atual
        precisao (float): valor real positivo

    Returns:
        boolean: True ou False
    """    
    valor = True
    for i in range(len(matriz)):
        if abs(produto_interno(matriz[i], solucao) - constantes[i]) >= precisao:
            valor = False
    return valor

def retira_zeros_diagonal(matriz, constantes):
    """Retorna uma nova matriz com as mesmas linhas que a de entrada, mas com estas
    reordenadas de forma a não existirem valores 0 na diagonal.

    Args:
        matriz (tuple: tuplo de tuplos representando a matriz de entrada
        constantes (tuple): tuplo de números representando o vetor das constantes

    Returns:
        tuple: matriz de entrada reoordenada 
        tuple: vetor das constantes reoordenado
    """    
    l_matriz, l_constantes = [list(x) for x in matriz], list(constantes)
    for i in range(len(l_matriz)):
        j = 0
        while j < len(l_matriz[i]) and l_matriz[i][i] == 0:
            if l_matriz[j][i] != 0 and l_matriz[i][j] != 0:
                l_matriz[i], l_matriz[j] = l_matriz[j], l_matriz[i]
                l_constantes[i], l_constantes[j] = l_constantes[j], l_constantes[i]
            j += 1
            if all(matriz[j][i] == 0 for j in range(len(matriz[i]))):
                return matriz, constantes
    return tuple(tuple(x) for x in l_matriz), tuple(l_constantes)

def eh_diagonal_dominante(matriz):
    """Retorna True caso seja uma matriz diagonalmente dominante, e False caso contrário.

    Args:
        matriz (tuple): tuplo de tuplos representando uma matriz quadrada

    Returns:
        boolean: True ou False
    """    
    diag_dominante = True
    for i in range(len(matriz)):
        diagonal = abs(matriz[i][i])
        soma = sum([abs(num) for num in (matriz[i])]) - abs(diagonal)
        if diagonal < soma:
            diag_dominante = False
    return diag_dominante

def coluna_nula(matriz):
    n_linha, n_coluna = len(matriz), len(matriz[0])
    coluna_nula = True
    for j in range(n_coluna):
        coluna = []
        for i in range(n_linha):
            coluna += [matriz[i][j]]
        if all(num == 0 for num in coluna):
            return coluna_nula
    return not coluna_nula

def sistema_linear_erros(matriz, constantes, precisao):
    if type(matriz) != tuple or matriz == () or type(constantes) != tuple or type(precisao)\
         != float or precisao <= 0:
         raise ValueError("resolve_sistema: argumentos invalidos")
    for i in matriz:
        if type(i) != tuple or len(i) != len(constantes) or not all(type(ci) == int or \
            type(ci) == float for ci in constantes) or not all(type(j)== float or type(j)\
                 == int for j in i): 
            raise ValueError("resolve_sistema: argumentos invalidos")
    else:
        return(matriz, constantes, precisao)
       
def resolve_sistema(matriz, constantes, precisao):
    """Aplica o método de Jacobi ao cálculo da solução.
    
    Args:
        matriz (tuple): tuplo de tuplos representando uma matriz quadrada
        constantes (tuple): tuple de números representando o vetor das constantes
        precisao (float): valor real positivo correspondente à precisão pretendida

    Raises:
        ValueError: Matriz diagonal não dominante
        ValueError: Argumentos inválidos
    
    Returns:
        tuple: solução do sistema
    """    
    sistema_linear_erros(matriz, constantes, precisao)
    matriz_reord, constantes_reord = retira_zeros_diagonal(matriz, constantes)
    if not eh_diagonal_dominante(matriz_reord):
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")
    if coluna_nula(matriz_reord):
        raise ValueError("resolve_sistema: argumentos invalidos")
    solucao = next_sol = [0] * len(matriz)
    while not verifica_convergencia(matriz_reord, constantes_reord, solucao, precisao):
        next_sol = [0] * len(matriz)
        for i in range(len(matriz)):
            next_sol[i] += solucao[i] + (constantes_reord[i] - produto_interno(matriz_reord[i], solucao)) / matriz_reord[i][i]
        solucao = next_sol.copy()
    return(tuple(solucao))
