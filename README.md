# Dashboard interactivo con Streamlit

Este proyecto contiene aplicaciones web interactivas desarrolladas con Streamlit, incluyendo un dashboard de visualización de datos y una aplicación básica de demostración.

## Descripción del proyecto

El proyecto incluye tres aplicaciones principales:

1. **Hello world** (`hello-world.py`): Una aplicación básica de demostración que muestra las funcionalidades fundamentales de Streamlit.

2. **Dashboard interactivo** (`dashboard.py`): Una aplicación completa de visualización de datos que utiliza el dataset Iris para mostrar gráficos interactivos, filtros y métricas.

3. **Dashboard V2.0** (`dashboard_v2.py`) - **¡NUEVO!**: Versión mejorada y más interactiva del dashboard con diseño avanzado, múltiples tipos de gráficos, controles de filtrado avanzados y capacidades de carga de archivos.

## Características

### Hello world
- Control deslizante interactivo
- Cálculos en tiempo real
- Demostración de conceptos básicos

### Dashboard interactivo
- Visualización de datos del dataset Iris
- Filtros por especie
- Gráficos de dispersión con Matplotlib y Plotly
- Controles deslizantes para filtrado dinámico
- Carga de archivos CSV personalizados
- Métricas calculadas en tiempo real

### Dashboard V2.0 - ¡NUEVO! 🚀
- **Diseño moderno** con gradientes y estilos CSS personalizados
- **Panel lateral interactivo** con múltiples controles de filtrado
- **Visualizaciones avanzadas** con Plotly interactivo y Matplotlib
- **Análisis multidimensional** con tabs organizados por tipo de análisis
- **Métricas en tiempo real** con tarjetas estilizadas
- **Carga de archivos mejorada** con vista previa y estadísticas
- **Paleta de colores profesional** y diseño responsivo
- **Filtros múltiples** (especie, rango de sépalo, ancho de pétalo)
- **Tabla interactiva** con selección de columnas personalizables
- **Gráficos especializados** (dispersión, distribuciones, correlaciones, comparativas)


## 🛠️ Instalación

### Prerequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el repositorio
```bash
git clone https://github.com/pedroam-dev/Streamlit.git
cd Streamlit
```

### 2. Crear un entorno virtual (recomendado)

#### Opción A: Usando venv (Python estándar)
```bash
python3 -m venv venv
source venv/bin/activate  # En macOS/Linux
# o
# venv\Scripts\activate  # En Windows
```

#### Opción B: Usando Anaconda
```bash
conda create -n streamlit python=3.13
conda activate streamlit
# Para desactivar el entorno: conda deactivate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

> **Nota para usuarios de Anaconda:** También puedes usar `conda install` para algunas dependencias principales:
> ```bash
> conda install pandas matplotlib seaborn numpy scipy
> pip install streamlit plotly  # Estas se instalan mejor con pip
> ```

##  Uso

### Ejecutar el Dashboard interactivo (Versión básica)
```bash
streamlit run dashboard.py
```

### Ejecutar el Dashboard V2.0 (Versión avanzada) - ¡RECOMENDADO! 🌟
```bash
streamlit run dashboard_v2.py
```

### Ejecutar Hello world
```bash
streamlit run hello-world.py
```

Las aplicaciones se abrirán automáticamente en tu navegador web en `http://localhost:8501`.

> **💡 Tip:** Te recomendamos probar primero `dashboard_v2.py` para una experiencia más completa e interactiva.

## Estructura del Proyecto

```
Streamlit/
├── dashboard.py           # Dashboard básico con visualizaciones
├── dashboard_v2.py        # Dashboard V2.0 - ¡NUEVO! Versión avanzada e interactiva
├── hello-world.py         # Aplicación de demostración básica
├── requirements.txt       # Dependencias del proyecto
├── setup.sh               # Script de configuración automática
├── .gitignore             # Archivos a ignorar en Git
├── .streamlit/            # Configuración de Streamlit
│   └── config.toml        # Configuración personalizada
├── README.md              # Documentación del proyecto
└── dataset/
    └── iris.csv           # Dataset de ejemplo
```

## Dependencias

- **streamlit**: Framework principal para aplicaciones web
- **pandas**: Manipulación y análisis de datos
- **seaborn**: Visualización estadística de datos
- **matplotlib**: Biblioteca de gráficos
- **plotly**: Gráficos interactivos

## Solución a Problemas Comunes

### Problema de Certificados SSL en macOS

Si encuentras errores relacionados con certificados SSL, ejecuta los siguientes comandos:

1. **Instalar certificados:**
```bash
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m ensurepip --upgrade
```

2. **Actualizar certificados de Python:**
```bash
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3 /Applications/Python\ 3.13/Install\ Certificates.command
```

3. **Si el paso 2 falla, verifica la existencia del archivo:**
```bash
ls "/Applications/Python 3.13/Install Certificates.command"
```

4. **Ejecutar directamente desde la terminal:**
```bash
open "/Applications/Python 3.13/Install Certificates.command"
```

5. **Verificar instalación de Python:**
```bash
which python3
```

## Funcionalidades del Dashboard

### Controles Interactivos
- **Selectbox**: Filtrado por especies del dataset Iris
- **Slider**: Selección de rangos de longitud de sépalo
- **File Uploader**: Carga de archivos CSV personalizados

### Visualizaciones
- **Matplotlib**: Gráficos de dispersión estáticos
- **Plotly**: Gráficos interactivos con zoom y hover
- **Métricas**: Promedios calculados dinámicamente

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

**Pedro AM** - [pedroam-dev](https://github.com/pedroam-dev)

## Enlaces Útiles

- [Documentación oficial de Streamlit](https://docs.streamlit.io/)
- [Galería de aplicaciones Streamlit](https://streamlit.io/gallery)
- [Cheat sheet de Streamlit](https://docs.streamlit.io/library/cheatsheet)

---

Si te gusta este proyecto, ¡dale una estrella en GitHub!