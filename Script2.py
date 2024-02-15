class NodoArbol:
    def __init__(self, valor):
        
        #Inicializa un nuevo nodo del árbol con el valor dado.
        
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolBinarioOrdenado:
    def __init__(self):
        
        #Inicializa un nuevo árbol binario ordenado con una raíz vacía.
      
        self.raiz = None

    def insertar(self, valor):
        
        #Inserta un nuevo nodo con el valor dado en el árbol manteniendo el orden.
        
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
    
        #Inserta un nuevo nodo de manera recursiva en el árbol.
        
        if valor <= nodo.valor:
            if nodo.izquierda is None:
                nuevo_nodo = NodoArbol(valor)
                nuevo_nodo.padre = nodo
                nodo.izquierda = nuevo_nodo
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nuevo_nodo = NodoArbol(valor)
                nuevo_nodo.padre = nodo
                nodo.derecha = nuevo_nodo
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def recorrido_preorden(self):
        
        #Realiza un recorrido pre-orden del árbol y devuelve una lista con los valores.
        
        return self._recorrido_preorden_recursivo(self.raiz, [])

    def _recorrido_preorden_recursivo(self, nodo, recorrido):
        
        #Realiza un recorrido pre-orden del árbol de manera recursiva.
        
        if nodo:
            recorrido.append(nodo.valor)
            self._recorrido_preorden_recursivo(nodo.izquierda, recorrido)
            self._recorrido_preorden_recursivo(nodo.derecha, recorrido)
        return recorrido

    def recorrido_inorden(self):
        
        #Realiza un recorrido in-orden del árbol y devuelve una lista con los valores.
       
        return self._recorrido_inorden_recursivo(self.raiz, [])

    def _recorrido_inorden_recursivo(self, nodo, recorrido):
        
        #Realiza un recorrido in-orden del árbol de manera recursiva.
        
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierda, recorrido)
            recorrido.append(nodo.valor)
            self._recorrido_inorden_recursivo(nodo.derecha, recorrido)
        return recorrido

    def recorrido_postorden(self):
        
        #Realiza un recorrido post-orden del árbol y devuelve una lista con los valores.
        
        return self._recorrido_postorden_recursivo(self.raiz, [])

    def _recorrido_postorden_recursivo(self, nodo, recorrido):
        
        #Realiza un recorrido post-orden del árbol de manera recursiva.
    
        if nodo:
            self._recorrido_postorden_recursivo(nodo.izquierda, recorrido)
            self._recorrido_postorden_recursivo(nodo.derecha, recorrido)
            recorrido.append(nodo.valor)
        return recorrido

def contar_valles(pasos):
    
    #Cuenta el número de valles en un recorrido dado.
    
    nivel = 0
    valles = 0
    for paso in pasos:
        if paso == 'U':
            nivel += 1
            if nivel == 0:
                valles += 1
        else:
            nivel -= 1
    return valles

if __name__ == "__main__":
    # Ejemplo de uso
    pasos = ['U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'D']
    print("Número de valles:", contar_valles(pasos))

    arbol = ArbolBinarioOrdenado()
    arbol.insertar(5)
    arbol.insertar(3)
    arbol.insertar(7)
    arbol.insertar(1)
    arbol.insertar(4)
    arbol.insertar(6)
    arbol.insertar(9)

    print("Recorrido pre-orden:", arbol.recorrido_preorden())
    print("Recorrido in-orden:", arbol.recorrido_inorden())
    print("Recorrido post-orden:", arbol.recorrido_postorden())
