# AHORA CON UNA VERSION MAS PRECISA DE YOLO, medium

from ultralytics import YOLO

# 1. CARGAR UN MODELO PREENTRENADO, usaremos el yolov8n(tiene un accuracy de 80), este es uno de los gratuitos, n de nano. El pt es la info de los pesos
# es el equivalente a un .keras solo que en yolo usas el punto pt
modelo = YOLO(
    "yolov8x.pt"
)

# 2. DETECTAR OBJETOS EN UNA IMAGEN
ruta_imagen = "cafeteria-dublin.jpg"

# 3. EJECUTAR EL MODELO SOBRE LA IMAGEN
resultados = modelo.predict(
    ruta_imagen,
    conf=0.05,
    verbose=False   # Esto no afecta al resultado, pero lo puse para que sea más rápido y no me muestre el proceso
)

# 4. OBTENER EL PRIMER RESULTADO
resultado = resultados[0]



#  A. CREAR DICCIONARIO PARA CONTAR OBJETOS
conteo_objetos = {}   # Como es un diccionario, hay que poner llaves

#  B. RECORRER TODAS LAS CAJAS (DETECCIONES)

for numero, caja in enumerate(
    resultado.boxes,
    start=1  # es
):

#  C. OBTEBER NUMERO DE LA CLASE
    clase_id = int(
    caja.cls[0]
)

#  D. OBTENER NOMBRE DE LA CLASE
    nombre_clase = modelo.names[
    clase_id
]

#  E. OBTENER LA CONFIANZA

    confianza = float(
    caja.conf[0]
)

#  F. OBTENER COORDENADAS DE LA CAJA
    x1, y1, x2, y2 = caja.xyxy[0]  # Con esto puedes detectar movimientos, coordenadas visualizada en cruz 

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    print("\nDETALLE DE LOS OBJETOS DETECTADOS:")
    print(
    f"\nOBJETO: {numero}"
)
    print(
    f"\nNOMBRE DE LA CLASE: {nombre_clase}"
)
    print(
    f"\nCONFIANZA: {confianza:.2}"  # Para 2 decimales
)
    print(
    f"\nCAJA COORDENADAS: ({x1}), ({y1}), ({x2}), ({y2})"
)

#   G. CONTAR CADA CAJA POR CATEGORIA
    if nombre_clase in conteo_objetos:
        conteo_objetos[nombre_clase] += 1

    else:
        conteo_objetos[nombre_clase] = 1

    cantidad_objetos = len(
        resultado.boxes
    )

    print(
    "\nOBJETOS DETECTADOS:",
    cantidad_objetos
)

    print(
        "\nCONTEO POR CATEGORIA:")

for nombre_clase, cantidad in conteo_objetos.items():
    print(
        f"{nombre_clase}: {cantidad}"
    )


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



# ANALISIS_2: me contó 25 boxes
# La confianza es del 0 al 1, mientras mas cerca al cero menos confianza tiene. Names son los nombres etiquetas. Los cliscs son los numeros

# Ahora vamos a hacerlo más complejo: Para ello le añado el medium en lugar del nano ("yolov8m.pt"), es la version más precisa y más pesada
# Ahora solo me muestra todo lo que tiene confianza mayor a 0.80 y me sale 11 box (MODIFIQUÉ conf desde el paso 3, EJECUTAR EL MODELO). Con el conf controlamos eso

# x1 izq, x2 der, y1 arriba, y2 abajo.
# ANÁLISIS;
# CAJA COORDENADAS: (1439), (1094), (1660), (1320)), por ejemplo si usaras Matloplib se podría ver mejor las coordenadas
# OJO, hay que identar los print DENTRO DEL FOR
# Con la version m (yolov8m.pt)o x (yolov8x.pt) en mi caso son similares, pero te saca mas objetos al bajarle la confianza

