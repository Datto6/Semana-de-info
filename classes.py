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
    
class Aula:
    def __init__(self,lista):
        for indexo,aula in lista.iterrows():
            self.horario=lista.loc['Horario']
            self.vagas=lista.loc['Vagas']
            self.materia=lista.loc['Materia']

    def horario():
        return self.horario
    def vagas():
        return int(self.vagas)
    def materia():
        return self.materia

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
        aulas_e_horarios.update({'Horario '+str(tempo+1):split(aulas)})
    return pd.DataFrame(aulas_e_horarios)

def quantas_vagas(tabela):
    lista_de_materias={}
    for indexo,aula in tabela.iterrows():
        vagas=input('Quantas vagas tem a aula'+aula+'? Responder em numero')
        horario=tabela.columns[indexo]
        materia=aula
        lista_de_materias.update({'Vagas':vagas,'Horario':horario,'Materia':aula})
    
    return lista_de_materias


produto=separar(respostas)
for aluno in produto:
    print(aluno.nomear())
