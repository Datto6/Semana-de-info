import pandas as pd
respostas= pd.read_csv('atualizado.csv')
class Pessoa:
    def __init__(self,informacoes):
        self.data=informacoes.loc['Carimbo de data/hora']
        self.nome=informacoes.loc['Nome Completo']
        self.turma=informacoes.loc['Turma']
        self.preferencias=[]
        self.segunda_op=[]
        self.terceira_op=[]
        self.quarta_op=[]

        self.preferencias.append(informacoes.loc['Preferencia 1'])
        for indexo in range(4):
            self.preferencias.append(informacoes.loc['Preferencia 1'+'.'+str(indexo+1)])
        
        self.segunda_op.append(informacoes.loc['Preferencia 2'])
        for indexo in range(4):
            self.segunda_op.append(informacoes.loc['Preferencia 2'+'.'+str(indexo+1)])

        self.terceira_op.append(informacoes.loc['Preferencia 3'])
        for indexo in range(4):
            self.terceira_op.append(informacoes.loc['Preferencia 3'+'.'+str(indexo+1)])

        self.quarta_op.append(informacoes.loc['Preferencia 4'])
        for indexo in range(4):
            self.quarta_op.append(informacoes.loc['Preferencia 4'+'.'+str(indexo+1)])
    
class Aula:
    def __init__(self,lista):
        self.horario=lista.loc['Horario']
        self.vagas=lista.loc['Vagas']
        self.materia=lista.loc['Materia']

#para retornar qualquer atributo, so botar classe.atributo
def separar(lista):
    alunos=[]
    for indexo,fileira in lista.iterrows():
        alunos.append(Pessoa(fileira))
    return alunos

def numero_aulas(lista_respostas):
    horarios=int(input('Quantos horarios tem esse dia?responder em forma de numero'))
    aulas_e_horarios={}
    materias=[]
    aulas_max=int(input('Quantas aulas tem por horario? Responder em forma de numero'))
    tempo=1
    for indexo,fileira in lista_respostas.iterrows():
        if fileira.loc['Preferencia 1'] not in materias:
            materias.append(aula)
        for constante in range(3):
            if fileira.loc['Preferencia '+str(constante+2)] not in materias:
                materias.append(aula)
        if len(materias)==aulas_max:
            break
    aulas_e_horarios.update({'Horario'+str(tempo):materias})
    while tempo<=horarios:
        for aula in lista_respostas['Preferencia 1'+'.'+str(tempo)].values:
            if aula not in materias:
                materias.append(aula)
        aulas_e_horarios.update({'Horario'+str(tempo):materias})
        tempo=tempo+1

    return pd.DataFrame(aulas_e_horarios)


def quantas_vagas(tabela):
    lista_de_materias={}
    for coluna in tabela:
        vagas=[]
        horario=[]
        materias=[]
        for aula in tabela[coluna]:
            vagas.append(input('Quantas vagas tem a aula '+aula+'? Responder em numero'))
            materias.append(aula)                                     
            lista_de_materias.update({'Vagas':int(vagas),'Horario':coluna,'Materia':materias})
    
    return pd.DataFrame(lista_de_materias)

def lista_de_aulas(lista_de_materias):
    aulas=[]
    for indexo,row in lista_de_materias.iterrows():
        aulas.append(Aula(row))
    return aulas


def definir_resultado(aulas,alunos):
    itinerario_definido={}
    for pessoa in alunos:
        aula_definida=[]
        for preferencia in pessoa.preferencias:
            for itinerario in aulas:
                if itinerario.materia==preferencia and itinerario.vagas>0:
                    aula_definida.append(preferencia)
                    itinerario.vagas=itinerario.vagas-1

        itinerario_definido.update({'Aluno':pessoa.nome,'Aulas':aula_definida})
                
alunos=separar(respostas)
for pessoa in alunos:
    print(alunos[pessoa])
