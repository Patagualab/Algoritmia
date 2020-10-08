'''
@author: Patricia Aguado Labrador

Algoritmo de ordenamiento por mezcla o mergesort. En primer lugar se realiza la funcion mergesort sobre
la lista que queremos ordenar, esta divide la lista en dos sublistas de la mitad del tamano a las que
aplicara recursivamente esta funcion hasta tener dos listas que tengan un elemento o esten vacias. Una
vez hecho esto se mezclaran ambas listas mediante la funcion merge. Esta recibe dos listas (seran la 
mitad izquierda y la mitad derecha) y crea una lista auxiliar en la que ira ordenando las sublistas
tomando un elemento de cada una e incluyendo el menor. Cuando se haya terminado de recorrer una lista
se incluira los elementos de la otra y dvolvera la lista auxiliar.'''

# funcion que recibe una lista a ordenar
def mergesort (lista):
    print('lista', lista)
    
    mitad = len(lista)//2   # calcula la mitad del tamano de la lista
    
    if(len(lista) <= 1):    # si la lista es vacia o solo tiene un elemento la devolvemos
        return lista
    
    lista[0:mitad] = mergesort(lista[0:mitad])  # llamamos recursivamente a mergesort con la primera mitad de la lista,
                                                # actualizando la primera mitad
    lista[mitad:len(lista)] = mergesort(lista[mitad:len(lista)])    # llamamos recursivamente a mergesort con la segunda 
                                                                    # mitad de la lista, actualizando la segunda mitad.
    
    return merge(lista[0:mitad], lista[mitad:len(lista)])   # devolvemos el resultado de mezclar las dos listas (mitades)

# funcion que recibe dos listas y las mezcla
def merge (lista1, lista2):
    l_aux = []  # creamos una lista auxiliar en la que almacenar la fusion de las listas
    i = 0   # indice para recorrer la primera lista
    j = 0   # indice para recorrer la segunda lista
    
    while (i < len(lista1) and j < len(lista2)):    # mientras haya elementos por recorrer en ambas listas
        
        if(lista1[i] < lista2[j]):  # si el elemento de la primera lista es menor que el elemento de la segunda
            l_aux.append(lista1[i]) # incluyo el de la primera
            i += 1  # aumento el indice que recorre la lista que ha incluido el menor elemento
            
        else:
            l_aux.append(lista2[j]) # si el menor elemento era el de la segunda lista lo incluyo
            j += 1  # aumento el indice que recorre la lista que ha incluido el menor elemento
    
    # cuando ya no quedan elementos que recorrer en alguna lista incluyo en la lista auxiliar los que quedan tanto
    # en una como en otra y devuelvo la lista auxiliar
    for i in range(i, len(lista1)):
        l_aux.append(lista1[i])
        
    for j in range(j, len(lista2)):
        l_aux.append(lista2[j])
    
    print('lista auxiliar', l_aux)
    
    return l_aux

#funcion que muestra por pantalla los elementos de la lista con un numero de guiones igual al elemento
def imprimir (lista):
    print(lista)
    for i in lista:
        print(i, end='\t')
        for j in range(i):
            print('-', end='')
        print('')
    print('')


lista =[2,4,7,5,1,5,10]
lista1=[2,4,7,5,1,5,10,9,-11,20,15,71,0,2,35,47,16]
imprimir (lista)
imprimir(mergesort(lista))