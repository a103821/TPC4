###funções
import random
listaPrincipal = []

def criaLista(N):
    global listaPrincipal
    listaPrincipal = []
    n = 1
    while n <= N:
        n = n + 1
        listaPrincipal.append(random.randrange(1,101))
    return listaPrincipal

def leLista(N):
    global listaPrincipal
    listaPrincipal=[] 
    k = 0
    while k < N:
        k = k + 1
        listaPrincipal.append(int(input("introduza um número para a sua lista1-"))) 
    return listaPrincipal


def somaLista(list):
        soma = 0
        for n in list:
            soma = soma + n             
        return (soma)

def mediaLista(list):
        soma = 0
        for n in list:
            soma = soma + n             
        return (soma/len(listaPrincipal))

def maiorLista(list):
        maior=list[0]
        for x in list:
                if x>maior:
                    maior=x
        return maior
        
def menorLista(list):
        menor=list[0]
        for x in list:
                if x<menor:
                    menor=x
        return menor

def estaOrdenadaC(list):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                return "Não"
        return "Sim"

def estaOrdenadaD(list):
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                return "Não"
        return "Sim"



def indiceDe(list, elem):
    cond=-1
    if elem in list:
        cond=list.index(elem)+1
    return cond

modo=-1

while modo != 0:
    modo = int(input("""(1) Criar Lista\n(2) Ler Lista\n(3) Soma\n(4) Média\n(5) Maior\n(6) Menor\n(7) estaOrdenada por ordem crescente\n(8) estaOrdenada por ordem decrescente\n(9) Procura um elemento\n(0) Sair\nQue operação quer realizar?-"""))
    
    if modo == 1:
        print(criaLista(int(input("Intoduza o total de números que quer na lista-"))))
        

    elif modo == 2:
        
        print(leLista(int(input("Intoduza o total de números que quer na lista-"))))
    
    
    elif modo == 3:
        
        print(somaLista(listaPrincipal))

    elif modo == 4:
        
        print(mediaLista(listaPrincipal))

    elif modo == 5:
                 
        print(maiorLista(listaPrincipal))
    elif modo == 6:
        
        print(menorLista(listaPrincipal))
    elif modo == 7:
        resultado=estaOrdenadaC(listaPrincipal)
        print(resultado)
    elif modo == 8:
        resultado2=estaOrdenadaD(listaPrincipal)
        print(resultado2)
    elif modo == 9:
        print(indiceDe(listaPrincipal,int(input("Procura um número na lista-"))))

    if modo == 0:
        print("Saíste do jogo!")





   