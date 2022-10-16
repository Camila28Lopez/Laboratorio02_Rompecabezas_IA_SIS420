# datos = estado

import time
class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_datos())


def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    numeroElementos = 10
    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop()
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            
            for i in range(numeroElementos-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]
                #para que los movimietos del rompecabezas no alamacenen demasiada informacion agregamoss un pequeño if que preguntara si la posicion del hijo actual
                #es igual al numero de vuelta actual +1 si es asi se quedara en esa posicion sin dar toda la vuelta entra del else ahorrandonos mucho tiempo.
                if temp == i+1:
                    True
                    
                else:        
                  hijo_datos[i] = hijo_datos[i + 1]
                  hijo_datos[i + 1] = temp
                  hijo = Nodo(hijo_datos)
                  #print(i)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)


if __name__ == "__main__":
    #si no se hacia el if implmentado la computadora hace demasiados ciclos, por lo cual el tamaño maximo del rompecabezas seria de 7 y no de 10 
    estado_inicial = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #importamos el tiempo para saber que tanto se tarda en resolver
    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end = time.time()
    
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    #Para que los resultados se impriman de mejor manera hacemos un for que impirma uno debajode otro
    for M in range(len(resultado)):
        
       print(resultado[M])
print("Tiempo : ",end-start, "seg")
print("............................")    