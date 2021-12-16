Bucle
===================


Exploraciones para armar bucle, un instrumento audiovisual gestual.


# Contenido

* processors contendrà lo que a veces llamamos "filtros". Dentro de processors está su output dentro de un directorio del mismo nombre.


* visualizer será el módulo que armará la parte visual. Por ahora es un directorio de exploraciones.


* videos tienen ejemplos de raw data.

* current_outputs tiene los resultados de analizar la raw data.

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
