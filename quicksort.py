'''
@author: Patricia Aguado Labrador

ALgoritmo de ordenamiento rapido o quicksort. La funcion quicksort comienza eligiendo
un elemento como pivote (mitad de la lista a ordenar) y lo intercambia con el elemento 
del final. Una vez hecho esto mediante i va buscando elementos mayores que el pivote y
mediante j elementos menores y los va intercambiando hasta que i sea mayor que j, lo que
significa que se han cruzado y que ya estan los menores a la izquierda y mayores a la derecha.
Por ultimo cambia el pivote que estaba al final a la posicion i, ya que esa sera su posicion
correcta en la lista y realiza recursivamente el proceso en las sublistas de la derecha e 
izquierda del pivote hasta que las sublistas esten vacias o tengan un elemento.'''

#funcion que recibe una lista a ordenar, el inicio de la lista y su fin
def quicksort (lista, inicio, fin):
    imprimir(lista)
    i = inicio  # i comienza en el primer elemento de la lista
    j = fin-1   # j comienza en el penultimo elemento de la lista
    pivote = (fin+inicio+1)//2  # el pivote sera el elemento situado en la mitad de la lista
    
    if(len(lista) <= 1):    # cuando la lista este vacia o solo contenga un elemento la devolvemos
        return lista
    
    lista[pivote], lista[fin] = lista[fin], lista[pivote]   # intercambiamos el pivote con el ultimo elemento, para que este al final
    
    print('pivote:', lista[fin])
    imprimir(lista)
    
    while(i <= j):
        
        while(lista[i] < lista[fin]):   # avanzo la i (aumentandola en 1) hasta encontrar un elemento mayor o igual que el pivote
            i += 1
        
        while(lista[j] > lista[fin]):   # avanzo la j (diminuyendola en 1) hasta encontrar un elemento menor o igual que el pivote
            j -= 1
        
        if(i <= j): # como i y j no se han cruzado y he encontrado un elemento mayor en la izquierda y uno menor en la derecha, los interambio
            lista[i], lista[j] = lista[j], lista[i]
            i += 1  # aumento i en uno tras hacer el intercambio
            
    lista[i], lista[fin] = lista[fin], lista[i] # cuando i y j se han cruzado es que ya estan los menores o iguales en la izquierda y los mayores en la 
                                                # derecha, siendo el elemento en la posicion i mayor que el pivote, intercambiamos el elemento en 
                                                # esta posicion con la ultima en la que estaba el pivote, asi este ya esta en su posicion final dentro
                                                # de la lista.
    
    if(inicio < j): # si inicio es menor que j (que esta a la izquierda del pivote) entonces es que quedan elementos que ordenar a la izquierda
        print('lista izquierda')
        quicksort(lista, inicio, j) # realizo quicksort con la sublista izquierda tomando j como fin
        
    if(i < fin):    # si i es menor que fin entonces es que quedan elementos que ordenar a la derecha
        print('lista derecha')
        quicksort(lista, i+1, fin)  # realizo quicksort con la sublista derecha tomando como inicio el elemento de la derecha de del pivote

    return lista

#funcion que muestra por pantalla los elementos de la lista con un numero de guiones igual al elemento
def imprimir (lista):
    print(lista)
    for i in lista:
        print(i, end='\t')
        for n in range(i):
            print('-', end='')
        print('')
    print('')
    
    
lista=[9,8,7,6,5]
lista1=[10,9,8,7,6,5,4,3,2,1,0]
quicksort(lista, 0, (len(lista)-1))

