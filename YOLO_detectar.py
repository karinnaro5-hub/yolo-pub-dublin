from ultralytics import YOLO

# 1. CARGAR UN MODELO PREENTRENADO, usaremos el yolov8n(tiene un accuracy de 80), este es uno de los gratuitos, n de nano. El pt es la info de los pesos
# es el equivalente a un .keras solo que en yolo usas el punto pt
modelo = YOLO(
    "yolov8n.pt"
)

# 2. DETECTAR OBJETOS EN UNA IMAGEN
ruta_imagen = "cafeteria-dublin.jpg"

# 3. EJECUTAR EL MODELO SOBRE LA IMAGEN
resultados = modelo(
    ruta_imagen
)

# 4. OBTENER EL PRIMER RESULTADO
resultado = resultados[0]

# 5. MOSTRAR IMAGENES CON DETECCIONES
resultado.show()

# 6. GUARDAR IMAGEN CON DETECCIONES
resultado.save(
    filename="resultado_cafeteria-dublin.jpg"
)

# ANALISIS: me salio la imagen con las etiquetas y la probabilidad de que sea cada objeto etiquetado.

# 7. CONTAR OBJETOS DETECTADOS
cantidad_objetos = len(
    resultado.boxes
)

print(
    "\nOBJETOS DETECTADOS:",
    cantidad_objetos
)

# ANALISIS_2: me contó 25 boxes
# La confianza es del 0 al 1, mientras mas cerca al cero menos confianza tiene. Names son los nombres etiquetas. Los cliscs son los numeros

# Ahora vamos a hacerlo más complejo:



