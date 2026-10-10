# 🍺 ¿Cuánta gente hay en el pub? De 25 a 106 objetos con YOLOv8

> Detección de objetos con **YOLOv8** sobre una foto real de un pub de Dublín: personas, sillas, mesas, copas y botellas localizadas automáticamente con su nivel de confianza y sus coordenadas. Y un experimento: ¿qué cambia al pasar del modelo más pequeño al más grande?

![Detecciones de YOLOv8x en el pub](imagenes/resultado_yolov8x.jpg)

## ⚔️ Nano contra extra-grande

| | YOLOv8 **nano** | YOLOv8 **x** (extra-grande) |
| --- | --- | --- |
| Tamaño de los pesos | ~6 MB | ~137 MB |
| Confianza mínima (`conf`) | 0.25 (por defecto) | 0.05 |
| **Objetos detectados** | **25** | **106** |
| Categorías distintas | 3 | 10 |

![Comparación de objetos detectados por cada modelo](imagenes/comparacion_modelos.png)

**Qué nos dice:**
- El modelo nano es rápido y ligero, pero solo ve lo evidente: personas, sillas y mesas.
- YOLOv8x, con el umbral de confianza muy bajo, encuentra también tazas, copas, botellas, plantas y hasta un cuchillo.
- El precio de bajar `conf` a 0.05: aparecen detecciones dudosas (p. ej. un "remote" o cajas con confianza 0.06). Subir `conf` a ~0.5 da un resultado más limpio.

| YOLOv8 nano | YOLOv8x |
| --- | --- |
| ![Resultado nano](imagenes/resultado_yolov8n.jpg) | ![Resultado x](imagenes/resultado_yolov8x.jpg) |

## 🧠 Qué se practica

- Cargar un modelo **preentrenado** de YOLO (`YOLO("yolov8n.pt")`); el `.pt` contiene los pesos, como un `.keras` en Keras.
- Ejecutar la detección con `modelo.predict(imagen, conf=...)` y controlar el umbral de confianza.
- Recorrer `resultado.boxes` para obtener de cada objeto:
  - la clase (`caja.cls` → `modelo.names`),
  - la confianza (`caja.conf`, de 0 a 1),
  - las coordenadas de la caja (`caja.xyxy`: x1 izquierda, y1 arriba, x2 derecha, y2 abajo).
- Contar los objetos por categoría con un diccionario.
- Detección **en tiempo real con la webcam** (`source=0`, `stream=True`) para avisar cuando aparece una botella.
