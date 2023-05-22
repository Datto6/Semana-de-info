class Pessoa:
    def __init__(self,nome, preferencias):
       self.nome=nome
       self.preferencias=preferencias
    def nomear(self):
        return self.nome
    def aulas(self):
        return self.preferencias

def contains_number(string):
    return any(char.isdigit() for char in string)

def nome_ou_nao(string,materias):
    if  not contains_number(string) and  string not in materias:
        if string != 'Materia' and string != 'Carimbo' and string != 'de' and string != 'data/hora':
            return True
    else:
        return False 

def separar(lista,materias):
    alunos=[]
    preferencias=[]
    for word in lista:
        nomes=[]
        if nome_ou_nao(word,materias):
            nomes.append(word)
        elif word in materias:
            preferencias.append(word)
        alunos.append(Pessoa(nomes,materias))
    return alunos

file=open('info.txt')
lista_total=file.read()
lista_analisada=lista_total.split()
conjunto_alunos=separar(lista_analisada,['Engenharia','Quimica','Arte','Foto'])
for i in conjunto_alunos:
    print(i.nomear())

print(lista_analisada)