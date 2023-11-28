import random

def criar_mapa_rota():
    linhas = int(input("Digite o número de linhas do mapa: "))
    colunas = int(input("Digite o número de colunas do mapa: "))
    mapa = [[0] * colunas for _ in range(linhas)]

    nivel = input("Escolha o nível de obstáculos (F - Fácil, M - Médio ou D - Difícil): ").lower()
    tipo_obstaculo = input("Escolha o tipo de obstáculo (L ou Q (quadrados)): ").lower()

    if nivel == 'f':
        gerar_obstaculos_facil(mapa, tipo_obstaculo, linhas, colunas)
    elif nivel == 'm':
        gerar_obstaculos_medio(mapa, tipo_obstaculo, linhas, colunas)
    elif nivel == 'd':
        gerar_obstaculos_dificil(mapa, tipo_obstaculo, linhas, colunas)
    else:
        print("Nível inválido. Saindo.")

    return mapa

def gerar_obstaculos_facil(mapa, tipo_obstaculo, linhas, colunas):
    tamanho_minimo = 2
    tamanho_maximo = min(len(mapa), len(mapa[0])) // 4
    quantidade_obstaculos = min(random.randint(1, 2), len(mapa) // 2, tamanho_maximo)

    gerar_obstaculos(mapa, tipo_obstaculo, quantidade_obstaculos,tamanho_minimo,tamanho_maximo)

def gerar_obstaculos_medio(mapa, tipo_obstaculo, linhas, colunas):
    tamanho_minimo = 2
    tamanho_maximo = min(len(mapa), len(mapa[0])) // 3
    quantidade_obstaculos = min(random.randint(3, 5), len(mapa) // 2, tamanho_maximo)

    gerar_obstaculos(mapa, tipo_obstaculo, quantidade_obstaculos,tamanho_minimo,tamanho_maximo)

def gerar_obstaculos_dificil(mapa, tipo_obstaculo, linhas, colunas):
    tamanho_minimo = 2
    tamanho_maximo = min(len(mapa), len(mapa[0])) // 2
    quantidade_obstaculos = min(random.randint(1, 8), len(mapa) // 2, tamanho_maximo)
    gerar_obstaculos(mapa, tipo_obstaculo, quantidade_obstaculos,tamanho_minimo,tamanho_maximo)

def gerar_obstaculos(mapa, tipo_obstaculo, quantidade_obstaculos,tamanho_minimo,tamanho_maximo):

    for _ in range(quantidade_obstaculos):
        tamanho_obstaculo = random.randint(tamanho_minimo, tamanho_maximo)
        if tipo_obstaculo == 'l':
            gerar_obstaculo_L(mapa)
        elif tipo_obstaculo == 'q':
            gerar_obstaculo_quadrado(mapa, tamanho_obstaculo)
        else:
            print("Tipo de obstáculo inválido. Saindo.")

def gerar_obstaculo_L(mapa):
    # Gera obstáculo em forma de L em posição aleatória do mapa
    i, j = encontrar_posicao_valida(mapa, 4, 3)

    if i is not None and j is not None:
        mapa[i][j] = 1
        mapa[i - 1][j] = 1
        mapa[i + 1][j] = 1
        mapa[i + 1][j + 1] = 1

def encontrar_posicao_valida(mapa, altura, largura):
    tentativas_maximas = 1000
    tentativas = 0

    while tentativas < tentativas_maximas:
        i = random.randint(1, len(mapa) - altura - 2)
        j = random.randint(1, len(mapa[0]) - largura - 2)

        # Verifica se a posição está livre e não colide com outros obstáculos
        posicao_valida = all(mapa[i + x][j + y] == 0 for x in range(altura) for y in range(largura)) \
                         and all(mapa[i - 1][j + y] == 0 for y in range(largura)) \
                         and all(mapa[i + altura][j + y] == 0 for y in range(largura)) \
                         and all(mapa[i + x][j - 1] == 0 for x in range(altura)) \
                         and all(mapa[i + x][j + largura] == 0 for x in range(altura))

        if posicao_valida:
            return i, j

        tentativas += 1
    return i, j

def gerar_obstaculo_quadrado(mapa, tamanho_max):
    # Gera obstáculo em forma de quadrado proporcional ao tamanho da matriz
    tamanho_quadrado = random.randint(2, tamanho_max)

    i = random.randint(1, len(mapa) - tamanho_quadrado - 2)  
    j = random.randint(1, len(mapa[0]) - tamanho_quadrado - 2)  

    for x in range(i, i + tamanho_quadrado):
        for y in range(j, j + tamanho_quadrado):
            mapa[x][y] = 1


def salvar_mapa_em_arquivo(mapa, nome_arquivo):
    # Abre o arquivo no modo de escrita
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve os elementos do mapa no arquivo
        for linha in mapa:
            arquivo.write(" ".join(map(str, linha)) + '\n')

if __name__ == "__main__":
    mapa = criar_mapa_rota()
    nome_arquivo = input("Digite o nome do arquivo de texto para salvar o mapa de rota: ")
    salvar_mapa_em_arquivo(mapa, nome_arquivo)
    print(f"O mapa de rota foi salvo no arquivo {nome_arquivo}.txt")
