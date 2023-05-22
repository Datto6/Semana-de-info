import pandas as pd

# Lê a planilha
dataframe = pd.read_csv('respostas.csv')

# Itera sobre cada linha do dataframe
for _, row in dataframe.iterrows():
    nome_completo = row['Nome']
    turma = row['Carimbo de data hora/hora']
    preferencia_1 = row['Materia 1']
    preferencia_2 = row['Materia 2']
    preferencia_3 = row['Materia 3']

    # Cria o conteúdo da linha para o arquivo de texto
    linha = f"Nome completo: {nome_completo}\n" \
            f"Turma: {turma}\n" \
            f"Preferência 1: {preferencia_1}\n" \
            f"Preferência 2: {preferencia_2}\n" \
            f"Preferência 3: {preferencia_3}\n"

    # Escreve a linha em um arquivo de texto separado
    with open(f"{nome_completo}.txt", 'w') as file:
        file.write(linha)