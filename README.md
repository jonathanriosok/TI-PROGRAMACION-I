  # 🐾 Adivina el Animal – Árbol de Decisión en Python

  Este proyecto fue desarrollado como trabajo integrador para la materia **Programación I** en la Tecnicatura Universitaria en Programación. Consiste en un juego interactivo de consola donde el sistema intenta adivinar qué animal está pensando el usuario mediante preguntas de “sí” o “no”. Lo más interesante es que el árbol de decisiones se actualiza dinámicamente: si el sistema falla, aprende una nueva pregunta y animal, expandiendo su conocimiento para futuras partidas.

  ---

  ## 📌 Características

  - Árbol binario de decisión representado con clases enlazadas.
  - Almacenamiento persistente del árbol en archivo `.txt`.
  - Visualización jerárquica del árbol en consola.
  - Aprendizaje automático básico: el árbol crece con cada error.
  - Juego ejecutable en consola sin dependencias externas.

  ---

  ## 🚀 Cómo ejecutar el juego

  1. Clonar este repositorio o descargar los archivos.

     ```bash
     git clone https://github.com/jonathanriosok/TI-PROGRAMACION-I.git
     cd TI-PROGRAMACION-I
     ```

  2. Asegurate de tener **Python 3.10+** instalado.

  3. Ejecutá el archivo principal:

     ```bash
     python adivina_el_animal.py
     ```

  4. Seguí las instrucciones en consola para comenzar a jugar.

  ---

  ## 🧠 Estructura del código

  - `NodoDecision`: clase que representa cada nodo del árbol (pregunta o animal).
  - `JuegoAdivinador`: clase principal que gestiona el juego, el aprendizaje y la interacción.
  - `arbol_animales.txt`: archivo donde se guarda el árbol de forma persistente.
  - Métodos auxiliares: para guardar/cargar el árbol, imprimirlo y recorrerlo de forma recursiva.

  ---

  ## 🎥 Video explicativo

  Podés ver una demostración completa del funcionamiento y desarrollo del proyecto en el siguiente enlace:  
  👉 [https://youtu.be/2SAgacWTAso](https://youtu.be/2SAgacWTAso)

  ---

  ## 🎯 Reflexión del equipo

  Este proyecto nos permitió aplicar conceptos fundamentales de la programación como **estructuras jerárquicas**, **recursividad**, y **persistencia de datos** de una forma práctica, lúdica y didáctica. El diseño del árbol de decisión con aprendizaje nos hizo reflexionar sobre cómo representar conocimiento y cómo hacer que un sistema evolucione con la experiencia. También reforzamos el trabajo en equipo y la importancia de planificar y dividir tareas en un desarrollo conjunto.

  ---

  ## 📷 Ejemplo de visualización
  [PREGUNTA] Tiene plumas?
├─Sí-> [ANIMAL] Pájaro
└─No-> [PREGUNTA] Ladra?
├─Sí-> [ANIMAL] Perro
└─No-> [ANIMAL] Gato