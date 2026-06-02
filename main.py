print('-------------------------------------------------- IFB Asa-Sul -------------------------------------------------- ')
print('------------------------------------------------ Sistema de Notas --------------------------------------------------\n')

def cadastrar_dados(): #função para cadastro de dados como aluno, nivel de escolaridade e disciplinas


    aluno = input('Digite o nome do aluno: ') #nome do aluno
    nivel = input('Qual nível de ensino? [Fundamental II / Médio]: ') #nivel de escolaridade
    quantidade = int(input('Quantas matérias deseja cadastrar? ')) #quantidade de matérias que ele deseja cadastrar

    disciplinas = [] #lista para guardar as disciplinas vindas do dicionário

    for c in range(quantidade): #loop para rodar pedindo dados da disciplina quantas vezes o usuario escolher na variável 'quantidade'
        
        print(f'Disciplina {c + 1}') #cadastro de disciplinas
        nome_disciplina = input('Digite o nome da disciplina: ')
        nota = float(input('Nota final: '))
        faltas = int(input('Quantidade de faltas: '))

        materias_cadastradas = { #dicionário para armazenamento de dados das disciplinas
            'Nome': nome_disciplina,
            'Nota': nota,
            'Faltas': faltas
        }

        disciplinas.append(materias_cadastradas) #adiciona o dicionário 'materias_cadastradas' na lista 'disciplinas'

    return aluno,nivel,disciplinas #retorna os dados do aluno, nivel de escolaridade e a lista de disciplinas para as outras funções utilizarem




def calcular_notas(disciplinas): #função para calcular a média das notas das disciplinas cadastradas
    soma = 0 

    for materias_cadastradas in disciplinas:
        soma += materias_cadastradas['Nota']

    media = soma / len(disciplinas)
    return media 




def calcular_faltas(disciplinas): #função para calcular o total de faltas das disciplinas cadastradas
    total_faltas = 0

    for materias_cadastradas in disciplinas:
        total_faltas += materias_cadastradas['Faltas']

    return total_faltas   




def gerar_relatorio_final(aluno, nivel, disciplinas, media, total_faltas): #função para gerar o relatório final do aluno, mostrando os dados cadastrados, a média das notas e o total de faltas, além de mostrar se o aluno foi aprovado ou reprovado

    print('\n-----==== Relatório Final ====-----\n')
    
    print(f'Aluno: {aluno}')
    
    print(f'Nível de escolaridade: {nivel}')
    
    print('\nDisciplinas Cadastradas:\n')
    
    for materias_cadastradas in disciplinas: #loop para mostrar os dados de cada disciplina cadastrada, como nome, nota e faltas
        print(f"{materias_cadastradas ['Nome']} | Nota: {materias_cadastradas ['Nota']} | Faltas: {materias_cadastradas ['Faltas']}")

    
    print(f'\nMédia Final: {media:.2f}\n')
    print(f'Total de faltas: {total_faltas}')

    if media >= 6 and total_faltas < 16:
        print('Aprovado!\n')
        print('Nota final maior ou igual a nota mínima')
        print('Frequencia maior ou igual a 75%')

    elif media >= 6 and total_faltas > 16:
        print('Reprovado!\n')
        print('Frequencia inferior a 75%.')

    else:
        print('Reprovado por nota e frequencia!\n')
        print('Nota final menor que a nota mínima.')
        print('Frequencia inferior a 75%.')


aluno, nivel, disciplinas = cadastrar_dados() #chama a função de cadastro de dados e guarda os dados retornados em variáveis.
total_faltas = calcular_faltas(disciplinas) #chama a função de calcular faltas.
media = calcular_notas(disciplinas) #chama a função de calcular notas.
gerar_relatorio_final(aluno, nivel, disciplinas, media, total_faltas) #chama a função de gerar relatório final.
