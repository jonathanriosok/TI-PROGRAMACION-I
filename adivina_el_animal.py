import os

class NodoDecision:
    def _init_(self, texto):
        self.texto = texto
        self.si = None
        self.no = None

    def es_hoja(self):
        return self.si is None and self.no is None

def guardar_arbol(raiz, archivo="arbol_animales.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        _guardar_preorden(raiz, f)

def _guardar_preorden(nodo, f):
    if nodo is None:
        f.write("#\n")
        return
    f.write(nodo.texto + "\n")
    _guardar_preorden(nodo.si, f)
    _guardar_preorden(nodo.no, f)

def cargar_arbol(archivo="arbol_animales.txt"):
    if not os.path.exists(archivo):
        return NodoDecision("Perro")
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return _leer_nodo(lineas)

def _leer_nodo(lineas):
    if not lineas:
        return None
    texto = lineas.pop(0).rstrip("\n")
    if texto == "#":
        return None
    nodo = NodoDecision(texto)
    nodo.si = _leer_nodo(lineas)
    nodo.no = _leer_nodo(lineas)
    return nodo

def visualizar_arbol(nodo):
    def _imprimir(nodo, prefijo=""):
        if nodo is None:
            return
        print(prefijo + ("[PREGUNTA] " if not nodo.es_hoja() else "[ANIMAL]  ") + nodo.texto)
        if nodo.si:
            _imprimir(nodo.si, prefijo + "  ├─Sí-> ")
        if nodo.no:
            _imprimir(nodo.no, prefijo + "  └─No-> ")
    print("\n--- Visualización del Árbol ---")
    _imprimir(nodo)
print()
