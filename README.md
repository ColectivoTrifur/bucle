Bucle
===================


Exploraciones para armar bucle, un instrumento audiovisual gestual.

Por ahora la parte python es una CLI.

# Instalar

[Instalar ffmpeg](https://www.ffmpeg.org/download.html)

```
git clone git@github.com:ColectivoTrifur/bucle.git
cd bucle
pip install PyOpenGL PyOpenGL_accelerate PyQt5 imgui[full] glfw python-mpv tqdm
pip install --editable .
```


# Correr

La parte python es un CLI. Una vez instalado, se puede acceder usando el comando

`bucle`

Este comando corre los procesadores sobre los videos que están en la carpeta `bucle/videos/`, escribe la data cruda del análisis en `bucle/current_outputs/` y escribe donde estás paradx los videos de los resultados. Después abre el visualizador y muestra en loop todos los videos creados.


Correr visualizador haciendo `python3 bucle/visualizer/with_glfw.py`


# Contenido

* bucle/processors contendrà lo que a veces llamamos "filtros" y que yo le llamo procesamientos o procesadores. 

Dentro de processors está su output dentro de un directorio del mismo nombre.


* bucle/visualizer será el módulo que armará la parte visual. Por ahora es un directorio de exploraciones.


* bucle/videos tienen ejemplos de raw data.

* bucle/current_outputs tiene los resultados de analizar la raw data.


# Comandos ùtiles
pasar de video a jpgs
ffmpeg -i squares.mp4 -vf fps=30 %d.jpg

pasar de imagenes a video
cat 1024_{1..387}.jpg | ffmpeg -framerate 30 -f image2pipe -i - ./output.mp4

