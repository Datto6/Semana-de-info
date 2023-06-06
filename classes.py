import pandas as pd
respostas= pd.read_csv('respostas.csv')
class Pessoa:
    def __init__(self,informacoes):
        self.data=informacoes.loc['Carimbo de data/hora']
        self.nome=informacoes.loc['Nome']
    def nomear(self):
        return self.nome
    def aulas(self):
        return self.preferencias

def separar(lista):
    alunos=[]
    for indexo,fileira in lista.iterrows():
        alunos.append(Pessoa(fileira))
    return alunos


produto=separar(respostas)
for aluno in produto:
    print(aluno.nomear())
