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
# Adivina el Animal: Juego de Adivinación con Árboles de Decisión
class JuegoAdivinador:
    def __init__(self, archivo="arbol_animales.txt"):
        self.archivo = archivo
        self.raiz = cargar_arbol(self.archivo)

    def jugar(self):
        nodo_actual = self.raiz
        recorrido = []

        while not nodo_actual.es_hoja():
            respuesta = self._hacer_pregunta(nodo_actual.texto)
            recorrido.append((nodo_actual.texto, "sí" if respuesta else "no"))
            nodo_actual = nodo_actual.si if respuesta else nodo_actual.no

        adivinanza_final = nodo_actual.texto
        respuesta_final = self._hacer_pregunta(f"¿Estás pensando en un {adivinanza_final}?")
        recorrido.append((f"¿Estás pensando en un {adivinanza_final}?", "sí" if respuesta_final else "no"))

        if respuesta_final:
            print("\n¡Gané! Soy un genio.")
        else:
            self._aprender(nodo_actual)

        if self._hacer_pregunta("¿Querés ver el recorrido que hiciste?"):
            print("\n--- Recorrido de preguntas y respuestas ---")
            for pregunta, respuesta in recorrido:
                print(f"{pregunta}  ->  {respuesta}")
            print("------------------------------------------")

    def _hacer_pregunta(self, pregunta):
        while True:
            respuesta = input(f"{pregunta} (sí/no): ").lower().strip()
            if respuesta.startswith("s"):
                return True
            elif respuesta.startswith("n"):
                return False
            else:
                print("Por favor, responde 'sí' o 'no'.")

    def _aprender(self, nodo_fallado):
        animal_correcto = input("¡Vaya! Me rindo. ¿Cuál era tu animal?: ").strip()
        nueva_pregunta = input(f"Por favor, dime una pregunta que diferencie a un {animal_correcto} de un {nodo_fallado.texto}: ").strip()
        texto_anterior = nodo_fallado.texto
        nodo_fallado.texto = nueva_pregunta
        if self._hacer_pregunta(f"Para un {animal_correcto}, la respuesta a '{nueva_pregunta}' es sí o no?"):
            nodo_fallado.si = NodoDecision(animal_correcto)
            nodo_fallado.no = NodoDecision(texto_anterior)
        else:
            nodo_fallado.no = NodoDecision(animal_correcto)
            nodo_fallado.si = NodoDecision(texto_anterior)
        print("\n¡Gracias! He aprendido algo nuevo.")

if __name__ == "__main__":
    juego = JuegoAdivinador()

    print("--- Bienvenido al Juego 'Adivina el Animal' ---")
    print("Piensa en un animal y yo intentaré adivinarlo.")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar una partida")
        print("2. Guardar árbol")
        print("3. Visualizar árbol")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            juego.jugar()
        elif opcion == "2":
            guardar_arbol(juego.raiz, juego.archivo)
            print(f"Árbol guardado en {juego.archivo}.")
        elif opcion == "3":
            visualizar_arbol(juego.raiz)
        elif opcion == "4":
            print("¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")