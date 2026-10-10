from ultralytics import YOLO

modelo = YOLO(
    "yolov8n.pt"
)

# 1. ACTIVAR CAMARA ORDENADOR
resultados = modelo.predict(
    source=0,
    stream=True,  # el stream tiene que estar antes del show para que muestre bien
    show=True,   # va a mostar una ventana con el video con un pop up, solo para la clase
    conf=0.50,
    verbose=False  # para evitar que muestre tanta info tecnica en el terminal
)

# 2. RECORRER RESULTADOS DE LA CAMARA
for resultado in resultados:
    for caja in resultado.boxes:
        clase_id = int(
            caja.cls[0]
        )

        nombre_clase = modelo.names[
            clase_id
        ]
        confianza = float(
            caja.conf[0]
        )
# 3. COMPROBAR SI ES UNA BOTELLA (dentro del bucle, para revisar cada caja)
        if nombre_clase == "bottle":
            print(
                "BOTELLA ENCONTRADA",
                round(
                    confianza * 100,
                    2
                ),
                "%"
            )