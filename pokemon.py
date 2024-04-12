import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

import random

while True:
    # Introdução
    limpar_console()
    print(30*'-')
    nome = input('Olá!! Seja bem vindo ao mundo pokemon!! Os Pokémons são criaturas incríveis que compartilham o mundo com os seres humanos\n\nPara começar, diga seu nome: \n\n')
    print(f'\n Seja bem vindo {nome}!!\n' + 30*'-')
           
    pokemons = []
    # Escolhendo inicial

    while True: 
        limpar_console()
        opcao = input(f'Para começar sua jornada, escolha seu pokemon inicial, ele será seu parceiro nessa sua aventura!\n\n 1 - Charmander\n 2 - Squirtle\n 3 - Bulbassauro \n\n')

        if opcao != '1' and opcao != '2' and opcao != '3':
            print('\nOpção inválida\n')
        elif opcao == '1':
            pokemon_inicial = 'Charmander'
            pokemons.append(pokemon_inicial)
            print(f'\nMuito bem!!! {pokemon_inicial} Será seu parceiro daqui pra frente, lute, explore e capture novos pokemons!!\n\n' )
            break
        elif opcao == '2':
            pokemon_inicial = 'Squirtle'
            pokemons.append(pokemon_inicial)
            print(f'\nMuito bem!!! {pokemon_inicial} Será seu parceiro daqui pra frente, lute, explore e capture novos pokemons!!\n\n')
            break
        elif opcao == '3':
            pokemon_inicial = 'Bulbassauro'
            pokemons.append(pokemon_inicial)
            print(f'\nMuito bem!!! {pokemon_inicial} Será seu parceiro daqui pra frente, lute, explore e capture novos pokemons!!\n\n' )
            break

    # Escolhendo caminho

    pokemons_da_rota = []
    rota = ''

    while True:
        limpar_console()
        opcao = int(input('Aonde deseja ir?\n\n1 - Caverna\n2 - Mato\n\n'))

        if opcao == 1:
            rota = 'Caverna'
            print(f"\nVocê Agora está na Caverna\n" )
            pokemons_da_rota = ["Zubat", "Geodude", "Onix", "Cubone", "Machop"]
            break
        elif opcao == 2:
            rota = 'mato'
            print('\nVocê Agora está no Mato\n' + 30*'-' )
            pokemons_da_rota = ["Pidgey", "Rattata", "Caterpie", "Weedle", "Oddish"]
            break
        else:
            print('\nOps, acho q n da pra ir por aí amigão\n')

        
    #entrando no caminho da rota e pegando pokemon:

    while True:
        limpar_console()
        pokemon_encontrado = pokemons_da_rota[random.randint(0, len(pokemons_da_rota) - 1)]
        opcao = int(input(f'\nlocal: {rota}\n\nVocê encontrou um {pokemon_encontrado}!, o que deseja fazer?\n\n1 - Capturar\n2 - Ignorar\n\n' ))

        if opcao == 1 and rota == 'mato':
            tentativas_de_captura = 3
            capturar = None
            while tentativas_de_captura > 0:
                limpar_console()
                print(f'\nTentando capturar {pokemon_encontrado}\n\ntentativas: {tentativas_de_captura}\n' )
                probabilidade = random.random()
                    
                if probabilidade <= 0.5:
                    capturar = True
                    break
                else:
                    tentarNovamente = int(input(f'\n{pokemon_encontrado} escapou da pokeball!\n\nTentar novamente?\n1 - sim\n2 - nao\n\n'))
                    
                    if tentarNovamente == 2:
                        print('\nVocê desistiu!')
                        capturar = False
                        break
                    elif tentarNovamente == 1:
                        
                        tentativas_de_captura -= 1
                        
                        if tentativas_de_captura == 0:
                            capturar = False
                            break
                        print('\nTentando novamente...\n')
                        
            
            
                        
            
            if capturar:
                print(f'\nVocê capturou o {pokemon_encontrado}!' )
                pokemons.append(pokemon_encontrado)
                break
            if capturar == False:
                print(f'\n{pokemon_encontrado} escapou!' )
                break

    print(pokemons)
    break
