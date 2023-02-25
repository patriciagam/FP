### TAD gerador ###

#construtores
#representação interna: [b, s]
def cria_gerador(b, s):
    """(Operação básica) Recebe um inteiro correspondente ao núumero de 
    bits do gerador e um inteiro positivo correspondente à seed, e 
    devolve o gerador correspondente.

    Args:
        b (int): número de bits do gerador
        s (int): seed ou estado inicial

    Raises:
        ValueError: Argumentos inválidos

    Returns:
        list: gerador constituído pelo númeor de bits e pela seed
    """
    if not( (b == 32 or b == 64) and type(b) == int and type(s) == int and 0 < s < 2**b):
        raise ValueError("cria_gerador: argumentos invalidos") 
    return [b, s]


def cria_copia_gerador(g):
    """(Operação básica) Recebe um gerador e devolve uma cópia nova do gerador.

    Args:
        g (list): gerador

    Returns:
       list: cópia do gerador
    """
    g_copia = g.copy()
    return g_copia

#seletor
def obtem_estado(g):
    """(Operação básica) Devolve o estado atual do gerador sem o alterar.

    Args:
        g (list): gerador

    Returns:
        int: estado atual do gerador
    """
    return g[1]


#modificadores
def define_estado(g, s):
    """(Operação básica) Define o novo valor do estado do gerador como sendo s
    e devolve s.

    Args:
        g (list): gerador
        s (int): estado

    Returns:
        int: novo estado do gerador
    """
    g[1] = s 
    return s


def atualiza_estado(g):
    """(Operação básica) Atualiza o estado do gerador de acordo com o 
    algoritmo xorshift de geração de números pseudoaleatórios, e devolve-o.

    Args:
        g (list): gerador

    Returns:
        int: estado atualizado do gerador
    """
    if g[0] == 32:
        g[1] ^= ( g[1] << 13) & 0xFFFFFFFF
        g[1] ^= ( g[1] >> 17) & 0xFFFFFFFF
        g[1] ^= ( g[1] << 5) & 0xFFFFFFFF
    else:
        g[1] ^= ( g[1] << 13) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] << 17) & 0xFFFFFFFFFFFFFFFF
    return g[1]


# reconhecedor
def eh_gerador(arg):
    """(Operação básica) Verifica se o argumento é um TAD gerador.

    Args:
        arg (universal): argumento

    Returns:
        boolean: True ou False
    """
    return type(arg) == list and len(arg) == 2 and type(arg[0]) == int and (arg[0] == 32 or\
         arg[0] == 64) and type(arg[1]) == int and 0 < arg[1] <= 2**arg[0]


#teste
def geradores_iguais(g1, g2):
    """(Operação básica) Verifica se os geradores são iguais.

    Args:
        g1 (list): gerador 1
        g2 (list): gerador 2

    Returns:
        boolean: True ou False
    """
    return g1 == g2 


#transformador
def gerador_para_str(g):
    """(Operação básica) Devolve a cadeia de carateres que representa o seu argumento.

    Args:
        g (list): gerador

    Returns:
        str: cadeia de carateres que representa o gerador 
    """
    return "xorshift%d(s=%d)" %(g[0], g[1])


#funções de alto nível
def gera_numero_aleatorio(g, n):
    """Atualiza o estado do gerador e devolve um número
    aleatório no intervalo [1, n] obtido a partir do novo estado s de g como 
    1 + mod(s, n).

    Args:
        g (TAD gerador): gerador
        n (int): número inteiro

    Returns:
        int: número aleatório
    """
    s = atualiza_estado(g)
    return 1 + s % n


def gera_carater_aleatorio(g, c):
    """Atualiza o estado do gerador e devolve um carater
    aleatório no intervalo entre "A e o carater maíusculo c.

    Args:
        g (TAD gerador): gerador
        c (str): carater maíusculo
    Returns:
        str: carater aleatório
    """
    s = atualiza_estado(g)
    l = ord(c) - ord("A") + 1
    return [chr(i) for i in range(ord("A"), ord(c) + 1)][s % l]   


### TAD coordenada ###

#construtor
#representação interna: (c, l)
def cria_coordenada(col, lin):
    """(Operação básica) Recebe os valores correspondentes à coluna e
    linha e devolve a coordenada correspondente.

    Args:
        col (str): coluna
        lin (int): linhas

    Raises:
        ValueError: Argumentos inválidos

    Returns:
        tuple: coordenada constituída pela coluna e linha recebidas
    """
    if not (type(col) == str and len(col) == 1 and "A" <= col <= "Z" and type(lin) == int\
         and 1 <= lin <= 99):
        raise ValueError("cria_coordenada: argumentos invalidos")
    return (col, lin)


#seletores
def obtem_coluna(c):
    """(Operação básica) Devolve a coluna da coordenada.

    Args:
        c (tuple): coordenada

    Returns:
        str: coluna da coordenada
    """
    return c[0]


def obtem_linha(c):
    """(Operação básica) Devolve a linha da coordenada.

    Args:
        c (tuple): coordenada

    Returns:
        int: linha da coordenada
    """
    return c[1]


#reconhecedor
def eh_coordenada(arg):
    """(Operação básica) Verifica se o argumento é um TAD coordenada.

    Args:
        arg (universal): argumento

    Returns:
        boolean: True ou False
    """
    return type(arg) == tuple and len(arg) == 2 and type(arg[0]) == str and len(arg[0]) == 1\
         and "A" <= arg[0] <= "Z" and type(arg[1]) == int and 1 <= arg[1] <= 99


#teste
def coordenadas_iguais(c1, c2):
    """(Operação básica) Verifica se as coordenadas são iguais.

    Args:
        c1 (tuple): coordenada 1
        c2 (tuple): coordenada 2

    Returns:
        boolean: True ou False
    """
    return c1 == c2


#transformadores
def coordenada_para_str(c):
    """(Operação básica) Devolve a cadeia de carateres que representa o seu 
    argumento.

    Args:
        c (tuple): coordenada

    Returns:
        str: cadeia de carateres que representa a coordenada 
    """
    return c[0] + "%0.2d" %(c[1])


def str_para_coordenada(s):
    """(Operação básica) Devolve a coordenada representada pelo seu argumento.

    Args:
        s (str): cadeia de carateres 

    Returns:
        tuple: coordenada que representa cadeia de carateres
    """
    return (s[0], int(s[1:]))


#funções de alto nível
def obtem_coordenadas_vizinhas(c):
    """Devolve um tuplo com as coordenadas vizinhas à coordenada,
     começando pela coordenada na diagonal acima-esquerda e seguindo no sentido horário.

    Args:
        c (TAD coordenada): coordenada

    Returns:
        tuple: tuplo com as coordenadas vizinhas à coordenada c
    """
    coord_vizinhas = ()
    for coluna, linha in [(ord(obtem_coluna(c)) + i, obtem_linha(c) + j) for i, j \
        in ((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))]:
        try:
            cria_coordenada(chr(coluna), linha)
        except:
            coord_vizinhas += ()
        else:
            coord_vizinhas += (cria_coordenada(chr(coluna), linha),)
    return coord_vizinhas


def obtem_coordenada_aleatoria(c, g): 
    """Recebe uma coordenada e um TAD gerador, e devolve uma
    coordenada gerada aleatoriamente em que c define a maior coluna e maior linha possíveis. 

    Args:
        c (TAD coordenada): coordenada
        g (TAD gerador): gerador 

    Returns:
        TAD coordenada: coordenada gerada aleatoriamente
    """
    coluna_aleatoria = gera_carater_aleatorio(g, obtem_coluna(c))
    linha_aleatoria = gera_numero_aleatorio(g, obtem_linha(c))
    return cria_coordenada(coluna_aleatoria, linha_aleatoria)


### TAD parcela ###

#contrutores
#representação interna: {"estado": "tapada", "mina": False}
def cria_parcela():
    """(Operação básica) Devolve uma parcela tapada sem mina escondida.

    Returns:
        dict: parcela cujas chaves são "estado" e "mina" e os valores são,
        respetivamente, "tapada" e False.
    """
    return {"estado": "tapada", "mina": False}


def cria_copia_parcela(p):
    """(Operação básica) Recebe uma parcela e devolve uma cópia nova da parcela.

    Args:
        p (dict): parcela

    Returns:
        dict: cópia da parcela
    """
    return p.copy()


#modificadores
def limpa_parcela(p):
    """(Operação básica) Modifica destrutivamente a parcela modificando o seu
    estado para limpa, e devolve a própria parcela.

    Args:
        p (dict): parcela

    Returns:
        dict: parcela p modificada
    """
    p["estado"] = "limpa"
    return p


def marca_parcela(p):
    """(Operação básica) Modifica destrutivamente a parcela modificando o seu
     estado para marcada com uma bandeira, e devolve a própria parcela.

    Args:
        p (dict): parcela

    Returns:
        dict: parcela p modificada
    """
    p["estado"] = "marcada"
    return p


def desmarca_parcela(p):
    """(Operação básica) Modifica destrutivamente a parcela modificando o seu
    estado para tapada, e devolve a própria parcela.

    Args:
        p (dict): parcela

    Returns:
        dict: parcela p modificada
    """
    p["estado"] = "tapada"
    return p


def esconde_mina(p):
    """(Operação básica) Modifica destrutivamente a parcela escondendo uma mina
    na parcela, e devolve a própria parcela.

    Args:
        p (dict): parcela

    Returns:
        dict: parcela p modificada
    """
    p["mina"] = True
    return p


#reconhecedores
def eh_parcela(arg):
    """(Operação básica) Verifica se o argumento é um TAD parcela.

    Args:
        arg (universal): argumento

    Returns:
        boolean: True ou False
    """
    return type(arg) == dict and len(arg) == 2 and "estado" in arg and (arg["estado"] ==\
         "tapada" or arg["estado"] == "marcada" or arg["estado"] =="limpa") and "mina" in arg\
             and (arg["mina"] == True or arg["mina"] == False)


def eh_parcela_tapada(p):
    """(Operação básica) Devolve True caso a parcela p se encontre tapada e
    False caso contrário.

    Args:
        p (dict): parcela

    Returns:
        boolean: True ou False
    """
    return eh_parcela(p) and p["estado"] == "tapada"


def eh_parcela_marcada(p):
    """(Operação básica) Devolve True caso a parcela p se encontre marcada e
    False caso contrário.

    Args:
        p (dict): parcela

    Returns:
        boolean: True ou False
    """
    return eh_parcela(p) and p["estado"] == "marcada"


def eh_parcela_limpa(p):
    """(Operação básica) Devolve True caso a parcela p se encontre limpa e
    False caso contrário.

    Args:
        p (dict): parcela

    Returns:
        boolean: True ou False
    """
    return eh_parcela(p) and p["estado"] == "limpa"


def eh_parcela_minada(p):
    """(Operação básica) Devolve True caso a parcela p se encontre minada e
    False caso contrário.

    Args:
        p (dict): parcela

    Returns:
        boolean: True ou False
    """
    return eh_parcela(p) and p["mina"] ==  True


#teste
def parcelas_iguais(p1, p2):
    """(Operação básica)  Verifica se as parcelas são iguais.

    Args:
        p1 (dict): parcela 1
        p2 (dict): parcela 2

    Returns:
        boolean: True ou False
    """
    return p1 == p2


#transformador
def parcela_para_str(p):
    """(Operação básica) Devolve a cadeia de caracteres que representa a parcela
    em função do seu estado: parcelas tapadas ("#"), parcelas marcadas ("@"),
    parcelas limpas sem mina ("?") e parcelas limpas com mina ("X").

    Args:
        p (dict): parcela

    Returns:
        str: cadeia de caracteres que representa a parcela
    """
    if p["estado"] == "tapada":
        return "#"
    elif p["estado"] == "marcada":
        return "@"
    elif p["estado"] == "limpa" and p["mina"] == False:
        return "?"
    else:
        return "X"


#função de alto nível
def alterna_bandeira(p):
    """Recebe uma parcela e modifica-a destrutivamente da seguinte
    forma: desmarca se estiver marcada e marca se estiver tapada, devolvendo True.
    Em qualquer outro caso, não modifica a parcela e devolve False.

    Args:
        p (TAD parcela): parcela

    Returns:
        boolean: True ou False
    """
    modifica = False
    if eh_parcela_marcada(p):
        p = desmarca_parcela(p)
        modifica = True
    elif eh_parcela_tapada(p):
        p = marca_parcela(p)
        modifica = True
    return modifica 


### TAD campo ###

#construtores
#representação interna: {TAD coordenada: TAD parcela}
def cria_campo(c, l):
    """(Operação básica) Recebe uma cadeia de carateres e um inteiro 
    correspondentes à última coluna e à última linha de um campo de minas,
    e devolve o campo do tamanho pretendido formado por parcelas tapadas sem minas.

    Args:
        c (str): última coluna do campo
        l (int): última linha do campo

    Raises:
        ValueError: Argumentos inválidos

    Returns:
        dict: campo de minas cujas chaves são coordenadas e os valores são 
        as parcelas correspondentes.
    """
    if not(type(c) == str and c in [chr(i) for i in range(ord("A"), ord("Z") + 1)]\
         and type(l) == int and 1 <= l <= 99):
         raise ValueError("cria_campo: argumentos invalidos")
    campo = {}
    for coordenada in [cria_coordenada(chr(coluna), linha) for coluna in range(ord("A"),\
         ord(c) + 1) for linha in range(1, l + 1)]:
        campo[coordenada] = cria_parcela()
    return campo                           


def cria_copia_campo(m):
    """(Operação básica) Recebe um campo e devolve uma cópia nova do campo.

    Args:
        m (dict): campo

    Returns:
        dict: cópia do campo
    """
    m_copia = cria_campo(obtem_ultima_coluna(m), obtem_ultima_linha(m))
    for coordenada in m:
            m_copia[coordenada] = cria_copia_parcela(obtem_parcela(m, coordenada))
    return m_copia


#seletores
def obtem_ultima_coluna(m):
    """(Operação básica) Devolve a cadeia de caracteres que corresponde à
    última coluna do campo de minas.

    Args:
        m (dict): campo de minas

    Returns:
        str: última coluna do campo de minas
    """
    return obtem_coluna(list(m)[-1])


def obtem_ultima_linha(m):
    """(Operação básica) Devolve o valor inteiro que corresponde à última 
    linha do campo de minas.

    Args:
        m (dict): campo de minas
    
    Returns:
        int: última linha do campo de minas
    """
    return obtem_linha(list(m)[-1])


def obtem_parcela(m, c):
    """(Operação básica) Devolve a parcela do campo m que se encontra na
    coordenada c.

    Args:
        m (dict): campo de minas
        c (TAD coordenada): coordenada

    Returns:
        TAD parcela: parcela que se encontra na coordenada c
    """
    return m[c]


def obtem_coordenadas(m, s):
    """(Operação básica) Devolve o tuplo formado pelas coordenadas ordenadas em 
    ordem ascendente de esquerda à direita e de cima a baixo das parcelas
    dependendo do valor de s: "limpas" para as parcelas limpas, "tapadas" para
    as parcelas tapadas, "marcadas" para as parcelas marcadas, e "minadas"
    para as parcelas que escondem minas.

    Args:
        m (dict): campo de minas
        s (str): cadeira de carateres 

    Returns:
        tuple: tuplo formado pelas coordenadas ordenadas
    """
    if s == "limpas":
        coordenadas = [coordenada for coordenada in m if eh_parcela_limpa(obtem_parcela(m, coordenada))]
    elif s == "tapadas":
        coordenadas = [coordenada for coordenada in m if eh_parcela_tapada(obtem_parcela(m, coordenada))]
    elif s == "marcadas":
        coordenadas = [coordenada for coordenada in m if eh_parcela_marcada(obtem_parcela(m, coordenada))]
    else:
        coordenadas = [coordenada for coordenada in m if eh_parcela_minada(obtem_parcela(m, coordenada))]
    return tuple(sorted(coordenadas, key = lambda coordenadas: (obtem_linha(coordenadas),\
         obtem_coluna(coordenadas))))


def obtem_numero_minas_vizinhas(m, c):
    """(Operação básica) Devolve o número de parcelas vizinhas da parcela
     na coordenada c que escondem uma mina.

    Args:
        m (dict): campo minado
        c (TAD coordenada): coordenada

    Returns:
        int: número de parcelas vizinhas que escondem uma mina
    """
    vizinhas = obtem_coordenadas_vizinhas(c)
    contador = 0
    for coordenada in vizinhas:
        if eh_coordenada_do_campo(m, coordenada) and eh_parcela_minada(m[coordenada]):
            contador += 1
    return contador


#reconhecedores
def eh_campo(arg):
    """(Operação básica) Verifica se o argumento é um TAD campo.

    Args:
        arg (universal): argumento

    Returns:
        boolean: True ou False
    """
    return type(arg) == dict and len(arg) >= 1 and all(eh_coordenada(coordenada) \
        for coordenada in arg) and all(eh_parcela(arg[coordenada]) for coordenada in arg)


def eh_coordenada_do_campo(m, c):
    """(Operação básica) Devolve True se c é uma coordenada válida dentro
    do campo m.

    Args:
        m (dict): campo de minas
        c (TAD coordenada): coordenada

    Returns:
        boolean: True ou False
    """
    return eh_coordenada(c) and c in m.keys()


#teste
def campos_iguais(m1, m2):
    """(Operação básica) Verifica se os geradores são iguais.

    Args:
        m1 (dict): campo 1
        m2 (dict): campo 2

    Returns:
        boolean: True ou False
    """
    chaves_m1 = sorted(list(m1.keys()))
    chaves_m2 = sorted(list(m2.keys()))
    return len(m1) == len(m2) and m1.keys() == m2.keys() and all(coordenadas_iguais(chaves_m1[i],\
        chaves_m2[i]) for i in range(len(chaves_m1))) and all([parcelas_iguais(obtem_parcela\
        (m1, coordenada),obtem_parcela(m2, coordenada)) for coordenada in m1])


#transformadores
def campo_para_str_aux(m):
    campo = ""
    for i in range(1, obtem_ultima_linha(m) + 1):
        for j in range(ord("A"), ord(obtem_ultima_coluna(m)) + 1):
            if parcela_para_str(obtem_parcela(m, cria_coordenada(chr(j), i))) == "?" and\
                 obtem_numero_minas_vizinhas(m, cria_coordenada(chr(j), i)) == 0:
                campo += " "
            elif parcela_para_str(obtem_parcela(m, cria_coordenada(chr(j), i))) == "?" and\
                obtem_numero_minas_vizinhas(m, cria_coordenada(chr(j), i)) != 0:
                campo += (str(obtem_numero_minas_vizinhas(m, cria_coordenada(chr(j), i))))
            else:
                campo += parcela_para_str(obtem_parcela(m, cria_coordenada(chr(j), i)))
        campo += "|\n%0.2d|" %(i + 1)
    return campo


def campo_para_str(m):
    """(Operação básica) Devolve uma cadeia de caracteres que representa o 
    campo de minas.

    Args:
        m (dict): campo de minas

    Returns:
        str: cadeia de caracteres que representa o campo
    """
    colunas = [chr(coluna) for coluna in range(ord("A"), ord(obtem_ultima_coluna(m)) + 1)]
    cabeçalho = str("   " + "".join(colunas)) +"\n" + "  +" + "-" *(len(colunas)) + "+\n"
    campo = ""
    rodape = "\n  +" + "-" *(len(colunas)) + "+"
    campo = "01|" + campo_para_str_aux(m)[:-4]  # retira linha extra
    return cabeçalho + campo + rodape


#funções de alto nível
def coloca_minas(m, c, g, n): 
    """Modifica destrutivamente o campo escondendo n minas em parcelas
    dentro do campo.

    Args:
        m (TAD campo): campo sem minas
        c (TAD coordenada): coordenada
        g (TAD gerador): gerador
        n (int): número de minas
    
    Returns:
        dict: campo minado
    """
    def coloca_minas_aux(m, c, coordenada_aleatoria, g, n):
        if n == 0:
            return m
        elif not coordenadas_iguais( coordenada_aleatoria, c) and coordenada_aleatoria not\
            in obtem_coordenadas_vizinhas(c) and not eh_parcela_minada(obtem_parcela(m, coordenada_aleatoria)):
            return esconde_mina(obtem_parcela(m, coordenada_aleatoria)) and \
                coloca_minas_aux(m, c, obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(m),\
                     obtem_ultima_linha(m)), g), g, n - 1)
        else:
            return coloca_minas_aux(m, c, obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(m),\
                 obtem_ultima_linha(m)), g), g, n)
    return coloca_minas_aux(m, c, obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(m),\
         obtem_ultima_linha(m)), g), g, n)


def limpa_campo(m, c):
    """Modifica destrutivamente o campo limpando a
    parcela na coordenada c e o devolvendo-a. Se não houver nenhuma mina
    vizinha escondida, limpa todas as parcelas vizinhas tapadas.

    Args:
        m (TAD campo): campo
        c (TAD coordenada): coordenada
    
    Returns:
        dict: campo modificado
    """
    def limpa_campo_aux(m, vizinhas):
        if vizinhas == ():
            return m
        if eh_coordenada_do_campo(m, vizinhas[0]) and eh_parcela_tapada(obtem_parcela(m, vizinhas[0])):
            limpa_parcela(obtem_parcela(m, vizinhas[0]))     
            if obtem_numero_minas_vizinhas(m, vizinhas[0]) == 0:
                return limpa_campo_aux(m, obtem_coordenadas_vizinhas(vizinhas[0])) and\
                     limpa_campo_aux(m, vizinhas[1:])
            else: 
                return limpa_campo_aux(m, vizinhas[1:])
        else:
            return limpa_campo_aux(m, vizinhas[1:])
    if not(eh_parcela_limpa(obtem_parcela(m, c))):
        limpa_parcela(obtem_parcela(m, c))     
        if obtem_numero_minas_vizinhas(m, c) != 0 or eh_parcela_minada(obtem_parcela(m, c)):
            return m
        else:
            return limpa_campo_aux(m, obtem_coordenadas_vizinhas(c))
    else:
        return m


### Funções adicionais ###

def jogo_ganho(m):
    """Recebe um campo do jogo das minas e devolve True se todas as parcelas
     sem minas se encontram limpas, ou False caso contrário.

    Args:
        m (TAD campo): campo

    Returns:
        boolean: True ou False
    """
    return all([eh_parcela_minada(obtem_parcela(m, coordenada)) for coordenada in\
         obtem_coordenadas(m, "tapadas")]) and all([eh_parcela_minada(obtem_parcela(m, coordenada))\
         for coordenada in obtem_coordenadas(m, "marcadas")])


def turno_jogador(m):
    """Recebe um campo de minas e oferece ao jogador a opção de escolher
    uma ação e uma coordenada. A função modifica destrutivamente o campo de
    acordo com ação escolhida, devolvendo False caso o jogador tenha limpo
    uma parcela que continha uma mina, ou True caso contrário. 

    Args:
        m (TAD campo): campo

    Returns:
        boolean: True ou False
    """
    acao = coordenada = ""
    while acao != "L" and acao != "M":
        acao = input("Escolha uma ação, [L]impar ou [M]arcar:")
    while not(len(coordenada) == 3 and ord("A") <= ord(coordenada[0]) <= ord(obtem_ultima_coluna(m))\
         and coordenada[1:].isnumeric() and 1 <= int(coordenada[1:]) <= obtem_ultima_linha(m)):
        coordenada = input("Escolha uma coordenada:")
    if acao == "L":
        limpa_campo(m, str_para_coordenada(coordenada))
    else:
        alterna_bandeira(obtem_parcela(m, str_para_coordenada(coordenada)))   
    return not(eh_parcela_minada(obtem_parcela(m, str_para_coordenada(coordenada)))\
         and eh_parcela_limpa(obtem_parcela(m, str_para_coordenada(coordenada))) )
    

def primeira_jogada(m, g, n):
    coordenada = ""
    print ("   [Bandeiras 0/%d]\n" %(n) + campo_para_str(m))
    while not(len(coordenada) == 3 and ord("A") <= ord(coordenada[0]) <= ord(obtem_ultima_coluna(m))\
         and coordenada[1:].isnumeric() and 1 <= int(coordenada[1:]) <= obtem_ultima_linha(m)):
        coordenada = input("Escolha uma coordenada:")
    m = limpa_campo(coloca_minas(m, str_para_coordenada(coordenada), g, n), str_para_coordenada(coordenada))
    print ("   [Bandeiras %d/%d]\n" %(len(obtem_coordenadas(m, "marcadas")) ,n) + campo_para_str(m))
    return m


def minas_erros(c, l, n, d, s):
    try:
         cria_gerador(d, s) and cria_coordenada(c, l) and cria_campo(c, l)
    except:
        raise ValueError("minas: argumentos invalidos")
    if not(type(n) == int and (ord(c) - ord("A") + 1) * l - 9 > n > 0):
        raise ValueError("minas: argumentos invalidos")


def minas(c, l, n, d, s):
    """Permite jogar ao jogo das minas. recebe uma cadeia de carateres e
    4 valores inteiros. A função devolve True se o jogador conseguir ganhar
    o jogo, ou False caso contrário.

    Args:
        c (str): última coluna do campo
        l (int): última linha do camp
        n (int): número de parcelas com minas
        d (int): dimensão do gerador
        s (int): estado inicial ou seed
    
    Raises:
        ValueError: Argumentos inválidos

    Returns:
        boolean: True, caso o jogador vença, ou False
    """
    minas_erros(c, l, n, d, s) 
    gerador = cria_gerador(d,s)
    campo = primeira_jogada(cria_campo(c, l) , gerador, n)
    while turno_jogador(campo):
        print ("   [Bandeiras %d/%d]\n" %(len(obtem_coordenadas(campo, "marcadas")), n) + campo_para_str(campo))
        if jogo_ganho(campo):
            print("VITORIA!!!")
            return jogo_ganho(campo)
    print ("   [Bandeiras %d/%d]\n" %(len(obtem_coordenadas(campo, "marcadas")), n) +\
         campo_para_str(campo) +"\nBOOOOOOOM!!!")
    return jogo_ganho(campo)
