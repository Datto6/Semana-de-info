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


def quantas_aulas():
    horarios=input('Quantos horarios tem esse dia?Responder em numero')
    tempo=0
    aulas_e_horarios={}
    while tempo<horarios:
        aulas=input('Quantas aulas o horario '+str(tempo+1)+' tem? Responder como escrito no forms e separado por um espaco')
        aulas_e_horarios.update({'Horario'+str(tempo+1):split(aulas)})
    return pd.DataFrame(aulas_e_horarios)


produto=separar(respostas)
for aluno in produto:
    print(aluno.nomear())
