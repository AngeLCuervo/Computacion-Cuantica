# 🔬 Proyecto: Lenguajes de Programación para Computación Cuántica

**Autores:** Geronimo Martinez Núñez · Angel Nicolás Cuervo  
**Contexto:** Trabajo de Curso — Lenguajes de Programación

---

## 📖 Descripción del Proyecto
Este proyecto presenta una inmersión profunda en los fundamentos teóricos y prácticos de la programación de computadores cuánticos. A través de este análisis revisaremos las diferencias fundamentales entre el paradigma clásico y el cuántico, la arquitectura base de los sistemas cuánticos y las herramientas actuales de desarrollo.

---

## 📝 Guion y Estructura del Contenido (Punto por Punto)

### 1. ¿Qué es programar un computador cuántico?
*   **1.1 Programación clásica vs. cuántica:** Análisis comparativo del paradigma tradicional (Datos + Control) frente al cuántico (Datos Cuánticos + Control).
*   **1.2 El qubit como dato fundamental:** Definición matemática y conceptual del qubit (superposición y transformaciones unitarias).

### 2. Modelos de cómputo cuántico
*   Descripción de los distintos paradigmas y modelos formales sobre los cuales operan los algoritmos cuánticos.

### 3. La arquitectura QRAM (Quantum Random Access Machine)
*   Explicación del modelo conceptual que permite a un ordenador clásico interactuar y controlar a un coprocesador cuántico.

### 4. Ensamblador Cuántico
*   **Registros:** Gestión y alocación de memoria cuántica y clásica.
*   **Puertas:** Operaciones fundamentales (transformaciones) sobre los qubits.
*   **Medición:** El proceso de colapso del estado cuántico para extraer información clásica.

### 5. Taxonomía de lenguajes cuánticos de alto nivel
*   Clasificación y evolución de los lenguajes de programación diseñados específicamente para abstraer el ensamblador cuántico.

### 6. El modelo híbrido clásico-cuántico
*   Cómo los algoritmos modernos (ej. VQE, QAOA) delegan tareas específicas al procesador cuántico mientras el flujo lógico principal se mantiene en hardware clásico.

### 7. Emuladores cuánticos
*   Herramientas y simuladores clásicos que permiten desarrollar, testear y depurar algoritmos cuánticos sin necesidad de hardware cuántico real.

### 8. Referencias y lectura adicional
*   Bibliografía, papers y recursos clave consultados para la elaboración de este trabajo.

---

## 🚀 Cómo utilizar este material
1. Abre el notebook principal: `notebook1_teoria_LPQ.ipynb`.
2. Sigue las celdas en orden conceptual, leyendo la teoría antes de avanzar a los posibles ejemplos prácticos o ecuaciones.
3. Se recomienda tener nociones básicas de álgebra lineal y números complejos para comprender la sección matemática de los qubits.

---
> *"El programador de computadores es un creador de universos de los cuales él solo es el legislador..."*
> — J. Weizenbaum, *Computer Power and Human Reason*

## 🔍 Guía de Soporte: Cómo leer y explicar los ejemplos de código

Durante la presentación, cuando lleguen a las celdas de código, no es necesario leer cada línea de Python, sino explicar la *intención* del código y cómo leer su resultado. Aquí tienen una guía para cada uno:

### 🖥️ Ejemplo 1: Esfera de Bloch (Visualización Matemática)
*   **Qué hace el código:** Usa `matplotlib` en 3D (`Axes3D`) para dibujar un globo terráqueo. Define los ejes X, Y y Z y ubica los estados base ($|0\rangle$ en el polo norte, $|1\rangle$ en el polo sur). Luego, dibuja un vector naranja.
*   **Cómo leer la gráfica:**
    *   Muestren el vector naranja ($|\psi\rangle$). Expliquen que cualquier flecha que *no* apunte directamente arriba o abajo está en "superposición".
    *   Hagan notar que la latitud (ángulo) define qué tan cerca está de ser un cero o un uno, y la longitud (el ecuador) representa lo que llamamos "fase cuántica" (algo sin equivalente clásico).

### 🖥️ Ejemplo 2: Diagrama de Flujo QRAM (Matplotlib Patches)
*   **Qué hace el código:** Es puramente visual. Dibuja rectángulos (`FancyBboxPatch`) iterando sobre una lista de colores y textos, y luego dibuja flechas que los conectan.
*   **Cómo leer el diagrama:**
    *   Lean el diagrama de **izquierda a derecha**.
    *   Señalen la caja amarilla ("Cuantización"), ahí es donde los datos entran al hardware cuántico.
    *   Señalen la caja verde ("Manipulación"), aquí ocurren las compuertas lógicas (Hadamard, CNOT).
    *   Muestren la flecha curva gris que dice "quizás repetir". Expliquen que esto representa el control clásico (ej: un bucle `while` en Python que evalúa `if RES == [10]`, y si no se cumple, vuelve a mandar otra orden al hardware cuántico).

### 🖥️ Ejemplo 3: Simulación con Qiskit (El código más importante)
*   **Qué hace el código:** Importa la librería real de IBM (`Qiskit`). Crea un circuito con 2 qubits y 2 bits clásicos (`QuantumCircuit(2, 2)`). Aplica una compuerta Hadamard (`qc.h`) a ambos qubits y finalmente los mide (`qc.measure`). Luego, corre un simulador 4096 veces (`shots=4096`).
*   **Cómo leer el resultado:**
    *   Primero, miren la gráfica de barras de matplotlib. Mostrará cuatro barras de alturas casi idénticas.
    *   Lean la salida de texto (los prints debajo de la celda): verán valores como `|00>: ~1024 veces`.
    *   **La explicación clave:** "Escribimos un código determinista, pero el resultado varía por las leyes cuánticas. Cada vez que el simulador lanza el circuito (un shot), el universo cuántico colapsa en una de 4 posibilidades. Al hacerlo miles de veces, descubrimos que las 4 posibilidades (00, 01, 10, 11) estaban equilibradas a un 25 por ciento."

### 🖥️ Ejemplo 4: Diagrama de Taxonomía
*   **Qué hace el código:** Divide la pantalla en 3 columnas (`plt.subplots(1, 3)`) de izquierda a derecha. Ubica lenguajes según su nivel de cercanía al hardware físico o al desarrollador abstracto.
*   **Cómo leer el diagrama:**
    *   Vayan de la columna azul (difícil, bajo nivel) a la rosa (abstracto, alto nivel).
    *   Mencionen lenguajes insignia de la columna central (verde), porque Qiskit y Cirq son las herramientas que las empresas (IBM, Google) más impulsan hoy en día, ya que viven dentro de un lenguaje muy amado: Python.
    *   Describan la última columna (rosa) como el "futuro": lenguajes funcionales que preverán errores cuánticos antes de siquiera compilar el código.
