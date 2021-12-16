Bucle
===================


Exploraciones para armar bucle, un instrumento audiovisual gestual.


# Contenido

* bucle/processors contendrà lo que a veces llamamos "filtros" y que yo le llamo procesamientos o procesadores. 

Dentro de processors está su output dentro de un directorio del mismo nombre.


* bucle/visualizer será el módulo que armará la parte visual. Por ahora es un directorio de exploraciones.


* bucle/videos tienen ejemplos de raw data.

* bucle/current_outputs tiene los resultados de analizar la raw data.

# Correr

Correr procesadores haciendo `python3 bucle/run.py`

Correr visualizador haciendo `python3 bucle/visualizer/with_glfw.py`

# Instalar

```
python3 setup.py install
pip install PyOpenGL PyOpenGL_accelerate
pip install PyQt5
pip install imgui[full]
pip install glfw
pip install python-mpv
```
