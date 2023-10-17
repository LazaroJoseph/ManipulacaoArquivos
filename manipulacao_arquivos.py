n_entrevistados= int(input('Insira a quantidade de entrevistados: '))
with open('dados entrevistados.txt', 'w') as arquivo:
    for entrevistado in range(1, n_entrevistados + 1):
        print(f"Entrevistado {entrevistado}:")
        
        nome=input('Insira seu nome: ')
        idade=input('Insira sua idade: ')

        arquivo.write(f'[ Pessoa | {entrevistado}: ]\n')
        arquivo.write(f'Nome: {nome}\n')
        arquivo.write(f'Idade: {idade}\n')
        arquivo.write('\n')

with open("dados entrevistados.txt", "r") as arquivo:
    dados = arquivo.read()
    
print("Dados do questionário:")
print(dados)