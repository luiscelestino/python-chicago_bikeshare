# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
    print("Linha {}: ".format(i))
    print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for i in range(1, 21):
    print("Linha {}: ".format(i))
    print(data_list[i][6])

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função para retornar uma lista de uma coluna, a partir de uma lista de várias colunas.
    Argumentos:
        data:  Uma lista de várias colunas.
        index: O índice que representa a posição da coluna.
    Retorna:
        A lista de uma das colunas.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for linha in data:
        column_list.append(linha[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for linha in (column_to_list(data_list, -2)):
    if   linha == "Male":
        male += 1
    elif linha == "Female":
        female += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função para contar o número de ocorrências de cada tipo de gênero.
    Argumentos:
        data_list: Uma lista de gêneros.
    Retorna:
        Uma lista com a quantidade de cada de ocorrências para cada gênero. 
        Posição:
            0 -> Número de ocorrências com o valor 'Male'.
            1 -> Número de ocorrências com o valor 'Female'.
    """
    male = 0
    female = 0
    for linha in (column_to_list(data_list, -2)):
        if   linha == "Male":
            male += 1
        elif linha == "Female":
            female += 1
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    Função para verificar qual o gênero mais popular de uma lista de gêneros.
    Argumentos:
        data_list: Uma lista de gêneros.
    Retorna:
        Uma string contendo o gênero mais popular de uma lista de gêneros. 
        Possíveis retornos:
            'Male'   -> Maior número de ocorrências com o valor 'Male'.
            'Female' -> Maior número de ocorrências com o valor 'Female'.
            'Equal'  -> Mesmo número de ocorrências com os valores 'Male' e 'Female'. 
    """
    answer = ""
    male   = count_gender(data_list)[0]
    female = count_gender(data_list)[1]
    if   male > female:
        answer = "Male"
    elif male < female:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_type(data_list):
    """
    Função para contar o número de ocorrências de cada tipo de usuário.
    Argumentos:
        data_list: Uma lista de gêneros.
    Retorna:
        Uma lista com a quantidade de cada de ocorrências para cada tipo de usuário. 
        Posição:
            0 -> Número de ocorrências com o valor 'Customer'.
            1 -> Número de ocorrências com o valor 'Subscriber'.
            2 -> Número de ocorrências com o valor 'Dependent'.
    """
    customer   = 0
    subscriber = 0
    dependent  = 0
    for linha in (column_to_list(data_list, -3)):
        if   linha == "Customer":
            customer   += 1
        elif linha == "Subscriber":
            subscriber += 1
        elif linha == "Dependent":
            dependent  += 1
    return [customer, subscriber, dependent]

user_type_list = column_to_list(data_list, -3)
print(set(user_type_list)) # Verificando todos user_types existentes
user_types = ["Customer", "Subscriber", "Dependent"]
quantity = count_user_type(data_list)
print(quantity)            # Verificando a quantidade de cada tipo de usuário
y_pos = list(range(len(user_types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, user_types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem gêneros cujos valores não estão preenchidos (string vazia)."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
def fc_min_trip(data_list):
    """
    Função para verificar a duração de viagem mínima, para uma lista de duração de viagens.
    Argumentos:
        data_list: Uma lista de duração de viagens.
    Retorna:
        Um float contendo o valor da duração de viagem mínima.
    """
    v_min_trip = float(data_list[0])
    for item in data_list:
        if float(item) < float(v_min_trip):
            v_min_trip = float(item)
    return v_min_trip

def fc_max_trip(data_list):
    """
    Função para verificar a duração de viagem máxima, para uma lista de duração de viagens.
    Argumentos:
        data_list: Uma lista de duração de viagens.
    Retorna:
        Um float contendo o valor da duração de viagem máxima.
    """
    v_max_trip = float(data_list[0])
    for item in data_list:
        if float(item) > float(v_max_trip):
            v_max_trip = float(item)
    return v_max_trip

def fc_mean_trip(data_list):
    """
    Função para verificar a duração de viagem média, para uma lista de duração de viagens.
    Argumentos:
        data_list: Uma lista de duração de viagens.
    Retorna:
        Um float contendo o valor da duração de viagem média.
    """
    v_sum_trip = 0.
    v_count = 0
    for item in data_list:
        v_sum_trip += float(item)
        v_count += 1
    return v_sum_trip/v_count

def fc_median_trip(data_list):
    """
    Função para verificar a mediana da duração de viagem mínima, para uma lista de duração de viagens.
    Argumentos:
        data_list: Uma lista de duração de viagens.
    Retorna:
        Um float contendo o valor da mediana da duração de viagem.
    """
    v_sorted_list = sorted([float(item) for item in data_list])
    v_median_trip = 0.
    v_count = 0
    for item in v_sorted_list:
        v_count += 1
    if v_count % 2 == 1:
        v_median_trip = float(v_sorted_list[v_count//2])
    else:
        v_median_trip = (float(v_sorted_list[v_count//2]) + float(v_sorted_list[v_count//2 - 1])) / 2
    return v_median_trip

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

min_trip    = fc_min_trip(trip_duration_list)
max_trip    = fc_max_trip(trip_duration_list)
mean_trip   = fc_mean_trip(trip_duration_list)
median_trip = fc_median_trip(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.
"""
print("\nTAREFA 11: Documentando as funções")

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
    Função para verificar tipos de valores e número de ocorrências de cada tipo de uma lista genérica.
    Argumentos:
        column_list: Uma lista genérica.
    Retorna:
        Posição:
            0 -> Uma lista com os tipos de valores.
            1 -> Uma lista com o número de ocorrências de cada tipo.
    """
    item_types = []
    count_items = []
    item_types = list(set(column_list))
    # inicializando variável count_items com lista de valores 0
    for i in range(len(item_types)):
        count_items.append(0)
    # incrementando variável count_items
    for item in column_list:
        for i in range(len(item_types)):
            if item == item_types[i]:
                count_items[i] += 1
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------

def fc_plot_grafic(data_list, index, title, xlabel, ylabel):
    """
    Função para plotar gráfico.
    Argumentos:
        data_list: Uma lista de listas de colunas.
        index:     O índice que representa a posição da coluna.
        title:     O título do gráfico.
        xlabel:    O label do eixo x.
        ylabel:    O label do eixo y.
    Retorna:
        Não possui retorno.
    """
    types, quantity = count_items(column_to_list(data_list, index))
    y_pos = list(range(len(types)))
    plt.errorbar(y_pos, quantity)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(y_pos, types)
    plt.title(title)
    plt.show(block=True)

fc_plot_grafic(data_list, -2, 'Quantidade por Gênero', 'Gênero', 'Quantidade')

