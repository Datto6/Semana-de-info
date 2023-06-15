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
        self.vagas=int(lista.loc['Vagas'])
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
            materias.append(fileira.loc['Preferencia 1'])
        for constante in range(int(aulas_max)):
            objeto_analisado=fileira.loc['Preferencia '+str(constante+1)]
            if  objeto_analisado not in materias:
                materias.append(objeto_analisado)
        if len(materias)==int(aulas_max):
            break
    aulas_e_horarios.update({'Horario'+str(tempo):materias})
    materias=[]
    while tempo<=horarios:
        for indexo,fileira in lista_respostas.iterrows():
            for constante in range(int(aulas_max)):
                objeto_analisado=fileira.loc['Preferencia '+str(constante+1)+'.'+str(tempo)]
                if objeto_analisado not in materias:
                    materias.append(objeto_analisado)
            if len(materias)==int(aulas_max):
                break
        if tempo<horarios:
            aulas_e_horarios.update({'Horario'+str(tempo+1):materias})
        elif tempo==horarios:
            aulas_e_horarios.update({'Horario'+str(tempo):materias})
        tempo=tempo+1
        materias=[]

    return pd.DataFrame(aulas_e_horarios)

def quantas_vagas(tabela):
    lista_de_materias={}
    vagas=[]
    horario=[]
    materias=[]
    for coluna in tabela:
        
        for aula in tabela[coluna]:
            vagas.append(input('Quantas vagas tem a aula '+aula+'? Responder em numero'))
            materias.append(aula)
            horario.append(coluna)                                     
        lista_de_materias.update({'Vagas':vagas,'Horario':horario,'Materia':materias})
    
    return pd.DataFrame(lista_de_materias)

def lista_de_aulas(lista_de_materias):
    aulas=[]
    for indexo,row in lista_de_materias.iterrows():
        aulas.append(Aula(row))
    return aulas


def definir_resultado(aulas,alunos):
    itinerario_definido={}
    max_aulas=input('Quantos horarios tem esse dia?')
    for pessoa in alunos:
        aulas_definidas=[]
        for preferencia in pessoa.preferencias:
            for itinerario in aulas:
                if itinerario.materia==preferencia and itinerario.vagas>0:
                    aulas_definidas.append(preferencia)
                    itinerario.vagas=itinerario.vagas-1
                if itinerario.materia==preferencia and itinerario.vagas==0:
                    aulas.remove(itinerario)
                if len(aulas_definidas)==max_aulas:
                    break
        if len(aulas_definidas)!=max_aulas:
            for alternativa in pessoa.segunda_op:
                for aula in aulas:
                    if aula.materia==alternativa and aula.vagas>0:
                        aulas_definidas.append(alternativa)
                        aula.vagas=aula.vagas-1
                    if aula.materia==alternativa and aula.vagas==0:
                        aulas.remove(aula)
                    if len(aulas_definidas)==max_aulas:
                        break
        if len(aulas_definidas)!=max_aulas:
            for curso in pessoa.terceira_op:
                for licao in aulas:
                    if licao.materia==alternativa and licao.vagas>0:
                        aulas_definidas.append(alternativa)
                        licao.vagas=licao.vagas-1
                    if licao.materia==alternativa and licao.vagas==0:
                        aulas.remove(licao)
                    if len(aulas_definidas)==max_aulas:
                        break

        itinerario_definido.update({'Aluno':pessoa.nome,'Aulas':aulas_definidas})
                
#alunos=separar(respostas)
#for pessoa in alunos:
#    print(alunos[pessoa])
blip=numero_aulas(respostas)
bleh=quantas_vagas(blip)
print(bleh)
