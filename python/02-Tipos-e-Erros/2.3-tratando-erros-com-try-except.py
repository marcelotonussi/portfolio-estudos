##

'''
Temos 3 formas de tratamento: 
    except:
    except Exception: 
    except Exception as e:

1) - except:
Aqui tratamos os erros de forma totalmente ampla. Pode ser qualquer erro.
Caso ocorra qualquer tipo de erro, entrará neste bloco do except.
O except puro captura absolutamente todos os tipos de erros e sinais do sistema (equivalente a BaseException)
Pega qualquer coisa que interrompa o código, incluindo fechar o programa à força.

Problema grave: 
    Captura comandos como KeyboardInterrupt (quando você aperta Ctrl + C para parar um loop infinito) e SystemExit.

Efeito colateral: 
    Pode esconder erros reais do sistema ou impedir você de desligar um script travado.

2) - except Exception:
Aqui ele captura apenas os erros normais de código, ignorando interrupções cruciais do usuário ou do sistema operacional.
Captura segura: 
    Pega somente os erros que herdam da classe padrão Exception 
    (como ValueError, TypeError, ZeroDivisionError, etc.).

Respeita o sistema: 
    Deixa passar avisos vitais de saída e interrupções manuais (KeyboardInterrupt), 
    permitindo o controle adequado do fluxo do programa.

Boa prática: 
    É considerado mais seguro, embora o ideal ainda seja especificar o erro exato que você espera (ex: except ValueError:).

3) - except Exception as e:
Neste caso, assim que um erro ocorre, além de tratarmos o erro,  ele é armazenado na variável "e" (pode utilizar a variável que quiser).
Permite que você acesse os detalhes da falha.

O que muda com o "as e": 
Acesso à mensagem: 
    Você consegue ler e exibir a mensagem de erro exata gerada pelo Python.
Inspeção: 
    Permite descobrir o tipo específico do erro ou investigar a causa do problema durante a execução.

Logs e depuração: 
    É essencial para gravar os erros em arquivos de texto (logs) para análise posterior, 
    sem interromper o funcionamento do sistema.
'''
#--------------------------------------------------------------
# 1) Código que quebra se o usuário digitar errado
#--------------------------------------------------------------
gols = int(input("Quantos gols o Brasil fez? "))
print(f"O Brasil fez {gols} gols.")

#--------------------------------------------------------------
# 2) ValueError acontecendo
#--------------------------------------------------------------
# numero = int("três")
# print(numero)

#--------------------------------------------------------------
# 3) Tratando erro ao digitar os gols do Brasil
#--------------------------------------------------------------
try:
    gols = int(input("Quantos gols o Brasil fez? "))
    print(f"O Brasil fez {gols} gols.")

except ValueError:
    print("Você precisa digitar um número inteiro") # esse print é opcional

#--------------------------------------------------------------
# 4) Analisando os gols do Brasil usando try/except com if
#--------------------------------------------------------------
try:
    gols = int(input("Quantos gols o Brasil marcou?"))

    if gols >= 3:
        print("O Brasil fez muitos gols!")
    elif gols ==1 or gols == 2:
        print("O Brasil marcou, mas poderia ter feito mais.")
    else:
        print(" O Brasil não marcou gols.")

except ValueError:
    print("Você precisa digitar um número inteiro.")

#--------------------------------------------------------------
# 5) Pedindo os gols até o usuário digitar um número válido
#--------------------------------------------------------------
numero_valido: bool = False

while numero_valido == False:
    try:
        gols = int(input("Quantos gols o Brasil fez? "))
        numero_valido = True

    except ValueError:
        print("Valor inválido. Digite um número inteiro. (ex: 1, 2, 4..)")


#--------------------------------------------------------------
# 6) Somnado os gols do Brasil em 3 jogos
#--------------------------------------------------------------
total_gols: int = 0

for jogo in range(1, 4):
    numero_valido: bool = False

    while numero_valido == False:
        try:
            gols = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))
            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols += gols

print(f"Total de gols do Brasil: {total_gols}")


#--------------------------------------------------------------
# 7) Mostrando o desempenho do Brasil em cada jogo
#--------------------------------------------------------------
total_gols: int = 0

for jogo in range(1, 4):
    numero_valido: bool = False

    while numero_valido == False:
        try:
            gols = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))
            numero_valido = True
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols += gols

    if gols == 0:
        print("O Brasil não marcou nesse jogo.")
    elif gols == 1:
        print("O Brasil marcou 1 gol nesse jogo.")
    else:
        print(f"O Brasil marcou {gols} gols nesse jogo.")

print(f"Total de gols do Brasil: {total_gols}")

media = total_gols / 3

print(f"Média de gols por jogo: {media:.2f}")


#--------------------------------------------------------------
# 8) Código Extra da aula para estudos: Campanha do Brasil na Copa
#--------------------------------------------------------------

total_gols_brasil: int = 0
total_gols_adversarios: int = 0
pontos: int = 0

for jogo in range(1, 4):
    print(f" Jogo {jogo}")

    numero_valido: bool = False

    while numero_valido == False:
        try:
            gols_brasil = int(input("Quantos gols o Brasil fez? "))
            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    numero_valido = False

    while numero_valido == False:
        try:
            gols_adversario = int(input("Quantos gols o adversário fez? "))
            numero_valido = True
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols_brasil += gols_brasil
    total_gols_adversarios += gols_adversario

    if gols_brasil > gols_adversario:
        print("Vitória do Brasil!")
        pontos += 3
        import sys
        #-------------------------------------------------------------------
        # Criando bandeira do Brasil.
        # Configuração de cores ANSI para blocos de fundo no terminal
        VERDE = '\033[48;5;28m'
        AMARELO = '\033[48;5;220m'
        AZUL = '\033[48;5;21m'
        BRANCO = '\033[48;5;15m'
        RESET = '\033[0m'

        # Matriz que define o desenho simplificado da bandeira
        desenho_bandeira = [
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
            "GGGGGGGGGGGGGGGGYYYGGGGGGGGGGGGGGG",
            "GGGGGGGGGGGGGGYYYYYYYGGGGGGGGGGGGG",
            "GGGGGGGGGGGYYYYYYYYYYYYYGGGGGGGGGG",
            "GGGGGGGGYYYYYYBBBBBBBYYYYYYGGGGGGG",
            "GGGGGGYYYYYYBBBBBBBBBBBYYYYYYGGGGG",
            "GGGYYYYYYYYYBBBBBBBWWWWYYYYYYYYYGG",
            "GGGYYYYYYYYYBBBWWWWBBBBYYYYYYYYYGG",
            "GGGGGGYYYYYYWWWBBBBBBBBYYYYYYGGGGG",
            "GGGGGGGGYYYYYYBBBBBBBYYYYYYGGGGGGG",
            "GGGGGGGGGGGYYYYYYYYYYYYYGGGGGGGGGG",
            "GGGGGGGGGGGGGGYYYYYYYGGGGGGGGGGGGG",
            "GGGGGGGGGGGGGGGGYYYGGGGGGGGGGGGGGG",
            "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
        ]

        # Dicionário de mapeamento para os blocos coloridos
        mapeamento = {
            'G': VERDE + '  ',    # Dois espaços para formar um bloco quadrado
            'Y': AMARELO + '  ',
            'B': AZUL + '  ',
            'W': BRANCO + '  '
        }
        #-------------------------------------------------------------------
        # Renderização na tela da bandeira do Brasil
        print("\n")
        for linha in desenho_bandeira:
            linha_colorida = "".join(mapeamento[pixel] for pixel in linha)
            print(linha_colorida + RESET)
        print("\n")
        #-------------------------------------------------------------------
    elif gols_brasil == gols_adversario:
        print("Empate do Brasil.")
        pontos += 1
    else:
        print("Derrota do Brasil. =(")

    print("--------------------------------")

print("Resumo de fase de grupos")
print("--------------------------------")
print(f"Total de gols do Brasil: {total_gols_brasil}")
print(f"Total de gols sofridos: {total_gols_adversarios}")
print(f"Pontuação final: {pontos}")

if pontos >= 6:
    print("Brasil classificado para a próxima fase!")    
elif pontos >= 4:
    print("O Brasil ainda tem chance, mas depende do grupo")
else: 
    print("Brasil em situação difícil na Copa.")