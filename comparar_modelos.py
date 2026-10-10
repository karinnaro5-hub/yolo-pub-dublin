# COMPARAR CUÁNTOS OBJETOS DE CADA TIPO DETECTA YOLOv8 nano FRENTE A YOLOv8x

from collections import Counter

import matplotlib.pyplot as plt
from ultralytics import YOLO

ruta_imagen = "cafeteria-dublin.jpg"

# 1. EJECUTAR LOS DOS MODELOS Y CONTAR LOS OBJETOS POR CATEGORÍA
modelos = {
    "YOLOv8 nano (conf 0.25)": ("yolov8n.pt", 0.25),
    "YOLOv8x (conf 0.05)": ("yolov8x.pt", 0.05),
}

conteos = {}
for nombre, (pesos, conf) in modelos.items():
    modelo = YOLO(pesos)
    resultado = modelo.predict(ruta_imagen, conf=conf, verbose=False)[0]
    conteos[nombre] = Counter(modelo.names[int(caja.cls[0])] for caja in resultado.boxes)
    print(f"{nombre}: {len(resultado.boxes)} objetos -> {dict(conteos[nombre])}")

# 2. ORDENAR LAS CATEGORÍAS DE MÁS A MENOS DETECCIONES
nano, extra = conteos.values()
categorias = sorted(set(nano) | set(extra), key=lambda c: (extra[c], nano[c]))

# 3. GRÁFICO DE BARRAS HORIZONTALES AGRUPADAS
AZUL, NARANJA = "#2a78d6", "#eb6834"
TEXTO, TEXTO_SECUNDARIO, REJILLA = "#0b0b0b", "#52514e", "#e4e3df"

fig, eje = plt.subplots(figsize=(9, 6))
posiciones = range(len(categorias))
alto = 0.38

for desplazamiento, (nombre, color) in zip((alto / 2, -alto / 2), zip(conteos, (AZUL, NARANJA))):
    valores = [conteos[nombre][c] for c in categorias]
    barras = eje.barh([p + desplazamiento for p in posiciones], valores, height=alto - 0.04,
                      color=color, label=nombre)
    eje.bar_label(barras, padding=3, color=TEXTO_SECUNDARIO, fontsize=9,
                  labels=[v if v else "" for v in valores])

eje.set_yticks(list(posiciones), categorias, color=TEXTO)
eje.set_xlabel("Objetos detectados", color=TEXTO_SECUNDARIO)
eje.set_title("¿Qué ve cada modelo en el pub?", loc="left", fontsize=14, fontweight="bold")
eje.legend(frameon=False, loc="lower right")
eje.grid(axis="x", color=REJILLA, linewidth=0.8)
eje.set_axisbelow(True)
eje.tick_params(colors=TEXTO_SECUNDARIO)
for lado in ("top", "right", "left"):
    eje.spines[lado].set_visible(False)
eje.spines["bottom"].set_color(REJILLA)

fig.tight_layout()
fig.savefig("imagenes/comparacion_modelos.png", dpi=120, bbox_inches="tight")
print("Gráfica guardada en imagenes/comparacion_modelos.png")
