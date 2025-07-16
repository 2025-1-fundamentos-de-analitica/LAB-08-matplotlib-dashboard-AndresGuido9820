# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Path("docs").mkdir(parents=True, exist_ok=True)


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    def cargar_datos():
        datos = pd.read_csv("files/input/shipping-data.csv")
        return datos

    def crear_visual_envios_por_bodega(datos):
        datos = datos.copy()
        plt.figure()
        conteos = datos["Warehouse_block"].value_counts()
        conteos.plot.bar(
            title="Envíos por Bodega",
            xlabel="Bloque de Bodega",
            ylabel="Cantidad",
            color="tab:blue",
            fontsize=8,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/envios_por_bodega.png")

    datos = cargar_datos()
    crear_visual_envios_por_bodega(datos)

    def crear_visual_modo_envio(datos):
        datos = datos.copy()
        plt.figure()
        conteos = datos["Mode_of_Shipment"].value_counts()
        conteos.plot.pie(
            title="Modo de Envío",
            wedgeprops=dict(width=0.35),
            ylabel="",
            color=["tab:blue", "tab:orange", "tab:green"],
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/modo_de_envio.png")

    datos = cargar_datos()
    crear_visual_modo_envio(datos)
    ###############################################################

    def crear_visual_promedio_calificacion_cliente(datos):
        datos = datos.copy()
        plt.figure()
        resumen = (
            datos[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        resumen.columns = resumen.columns.droplevel()
        resumen = resumen[["mean", "min", "max"]]
        plt.barh(
            y=resumen.index.values,
            width=resumen["max"].values - 1,
            left=resumen["min"].values,
            height=0.9,
            color="lightgray",
            alpha=0.8,
        )
        colores = [
            "tab:green" if valor > 3.0 else "tab:orange"
            for valor in resumen["mean"].values
        ]
        plt.barh(
            y=resumen.index.values,
            width=resumen["mean"].values - 1,
            left=resumen["min"].values,
            height=0.5,
            color=colores,
            alpha=1,
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.savefig("docs/promedio_calificacion_cliente.png")
        return colores

    datos = cargar_datos()
    crear_visual_promedio_calificacion_cliente(datos)

    def crear_visual_distribucion_peso(datos):
        datos = datos.copy()
        plt.figure()
        datos.Weight_in_gms.plot.hist(
            title="Distribución de Peso",
            color="tab:orange",
            edgecolor="white",
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.savefig("docs/distribucion_peso.png")

    datos = cargar_datos()
    crear_visual_distribucion_peso(datos)

    datos = cargar_datos()
    crear_visual_envios_por_bodega(datos)
    crear_visual_modo_envio(datos)
    crear_visual_promedio_calificacion_cliente(datos)
    crear_visual_distribucion_peso(datos)
    html = """<!DOCTYPE html>
<html>
  <body>
    <h1>Ejemplo de Dashboard de Envíos</h1>
    <div style=\"width:45%;float:left">
      <img src=\"envios_por_bodega.png\" alt=\"Fig 1">
      <img src=\"modo_de_envio.png\"     alt=\"Fig 2">
    </div>
    <div style=\"width:45%;float:left">
      <img src=\"promedio_calificacion_cliente.png\" alt=\"Fig 3">
      <img src=\"distribucion_peso.png\"     alt=\"Fig 4">
    </div>
  </body>
</html>"""

    # escribe el archivo en docs
    with open("docs/index.html", "w", encoding="utf-8") as archivo:
        archivo.write(html)


if __name__ == "__main__":
    pregunta_01()
