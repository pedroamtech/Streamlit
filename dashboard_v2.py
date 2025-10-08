import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuración de la página con diseño atractivo
st.set_page_config(
    page_title="Dashboard Iris V2.0",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para hacer el dashboard más bonito
st.markdown("""
<style>
    .main {
        padding: 0rem 1rem;
    }
    
    .stTitle {
        color: #2E8B57;
        text-align: center;
        font-size: 3rem !important;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 0.5rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(90deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 10px;
    }
    
    .plot-container {
        background: white;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar datos con cache
@st.cache_data
def cargar_datos():
    """Cargar el dataset Iris con información adicional"""
    df = sns.load_dataset("iris")
    # Agregar algunas columnas calculadas para mayor interactividad
    df['sepal_ratio'] = df['sepal_length'] / df['sepal_width']
    df['petal_ratio'] = df['petal_length'] / df['petal_width']
    df['total_area'] = (df['sepal_length'] * df['sepal_width']) + (df['petal_length'] * df['petal_width'])
    return df

# TÍTULO: Título principal con emojis y estilo
st.title("Dashboard interactivo Iris V2.0")
st.markdown("<div class='info-box'><h3>Explora el famoso dataset Iris de manera interactiva</h3><p>Utiliza los controles de la barra lateral para filtrar y analizar los datos en tiempo real</p></div>", unsafe_allow_html=True)

# Cargar datos
df = cargar_datos()

# SIDEBAR: Panel lateral con controles
st.sidebar.markdown("#Controles del Dashboard")
st.sidebar.markdown("---")

# SELECTBOX: Selección de especie
st.sidebar.markdown("### Filtrar por Especie")
especies_disponibles = ['Todas'] + list(df['species'].unique())
especie_seleccionada = st.sidebar.selectbox(
    "Selecciona una especie:",
    especies_disponibles,
    help="Filtra los datos por especie de iris"
)

# Filtrar datos según selección
if especie_seleccionada == 'Todas':
    df_filtrado = df.copy()
    titulo_especie = "Todas las especies"
else:
    df_filtrado = df[df['species'] == especie_seleccionada]
    titulo_especie = especie_seleccionada

# SLIDER: Control deslizante para longitud de sépalo
st.sidebar.markdown("### Rango de Longitud de Sépalo")
longitud_min = float(df['sepal_length'].min())
longitud_max = float(df['sepal_length'].max())

rango_sepal = st.sidebar.slider(
    "Selecciona el rango (cm):",
    min_value=longitud_min,
    max_value=longitud_max,
    value=(longitud_min, longitud_max),
    step=0.1,
    help="Filtra las muestras por longitud de sépalo"
)

# Aplicar filtro de rango
df_filtrado = df_filtrado[
    (df_filtrado['sepal_length'] >= rango_sepal[0]) & 
    (df_filtrado['sepal_length'] <= rango_sepal[1])
]

# SLIDER: Control para ancho de pétalo
st.sidebar.markdown("### Rango de ancho de pétalo")
ancho_min = float(df['petal_width'].min())
ancho_max = float(df['petal_width'].max())

rango_petal = st.sidebar.slider(
    "Selecciona el ancho (cm):",
    min_value=ancho_min,
    max_value=ancho_max,
    value=(ancho_min, ancho_max),
    step=0.1,
    help="Filtra las muestras por ancho de pétalo"
)

# Aplicar filtro de ancho de pétalo
df_filtrado = df_filtrado[
    (df_filtrado['petal_width'] >= rango_petal[0]) & 
    (df_filtrado['petal_width'] <= rango_petal[1])
]

# Información sobre datos filtrados
st.sidebar.markdown("---")
st.sidebar.markdown("### Datos actuales")
st.sidebar.info(f"**Muestras:** {len(df_filtrado)}/{len(df)} ({len(df_filtrado)/len(df)*100:.1f}%)")
if len(df_filtrado) > 0:
    st.sidebar.success("Datos disponibles para análisis")
else:
    st.sidebar.error("No hay datos con los filtros actuales")

# Layout principal en columnas
col1, col2 = st.columns([2, 1])

with col1:
    # DATAFRAME: Mostrar datos filtrados de manera interactiva
    st.markdown(f"## Datos filtrados - {titulo_especie}")
    
    if len(df_filtrado) > 0:
        # Mostrar estadísticas rápidas
        col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
        
        with col_stats1:
            st.markdown('<div class="metric-card"><h4>Sépalo promedio</h4><h2>{:.1f} cm</h2></div>'.format(df_filtrado['sepal_length'].mean()), unsafe_allow_html=True)
        
        with col_stats2:
            st.markdown('<div class="metric-card"><h4>Pétalo promedio</h4><h2>{:.1f} cm</h2></div>'.format(df_filtrado['petal_length'].mean()), unsafe_allow_html=True)
        
        with col_stats3:
            st.markdown('<div class="metric-card"><h4>Ratio sépalo</h4><h2>{:.2f}</h2></div>'.format(df_filtrado['sepal_ratio'].mean()), unsafe_allow_html=True)
        
        with col_stats4:
            st.markdown('<div class="metric-card"><h4>Área total</h4><h2>{:.1f}</h2></div>'.format(df_filtrado['total_area'].mean()), unsafe_allow_html=True)
        
        # Tabla interactiva con colores
        st.markdown("### Tabla Interactiva")
        
        # Selectbox para columnas a mostrar
        columnas_disponibles = df_filtrado.columns.tolist()
        columnas_mostrar = st.multiselect(
            "Selecciona las columnas a mostrar:",
            columnas_disponibles,
            default=['species', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
            help="Elige qué columnas quieres visualizar en la tabla"
        )
        
        if columnas_mostrar:
            st.dataframe(
                df_filtrado[columnas_mostrar].round(2),
                use_container_width=True,
                height=300
            )
    else:
        st.warning("No hay datos que mostrar con los filtros actuales")

with col2:
    # FILE_UPLOADER: Subir archivos CSV
    st.markdown("## Subir dataset personalizado")
    
    archivo_subido = st.file_uploader(
        "Sube tu archivo CSV:",
        type=['csv'],
        help="Sube un archivo CSV para análisis comparativo"
    )
    
    if archivo_subido is not None:
        try:
            df_usuario = pd.read_csv(archivo_subido)
            st.success("Archivo cargado correctamente!")
            
            # Mostrar información del archivo
            st.write(f"**Dimensiones:** {df_usuario.shape[0]} filas × {df_usuario.shape[1]} columnas")
            
            # Vista previa
            st.write("**Vista previa:**")
            st.dataframe(df_usuario.head(), use_container_width=True)
            
            # Estadísticas básicas si es numérico
            columnas_numericas = df_usuario.select_dtypes(include=[np.number]).columns
            if len(columnas_numericas) > 0:
                st.write("**Estadísticas:**")
                st.dataframe(df_usuario[columnas_numericas].describe().round(2))
                
        except Exception as e:
            st.error(f"Error al procesar el archivo: {str(e)}")
    
    # Información adicional
    st.markdown("---")
    st.markdown("### Información del Dataset Iris")
    st.info("""
    **Dataset Iris (1936)**
    - Creado por Ronald Fisher
    - 150 muestras de flores
    - 3 especies diferentes
    - 4 características medidas
    """)

# Sección de gráficos
if len(df_filtrado) > 0:
    st.markdown("---")
    st.markdown("## Visualizaciones Interactivas")
    
    # Tabs para diferentes tipos de gráficos
    tab1, tab2, tab3, tab4 = st.tabs(["Dispersión", "Distribuciones", "Correlaciones", "Comparativas"])
    
    with tab1:
        # PLOTLY_CHART: Gráfico de dispersión interactivo
        col_plot1, col_plot2 = st.columns(2)
        
        with col_plot1:
            st.markdown("### Sépalo: Longitud vs Ancho")
            fig1 = px.scatter(
                df_filtrado,
                x='sepal_length',
                y='sepal_width',
                color='species',
                size='total_area',
                hover_data=['petal_length', 'petal_width'],
                title="Dispersión de Sépalos",
                color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
            )
            fig1.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col_plot2:
            st.markdown("### Pétalo: Longitud vs Ancho")
            fig2 = px.scatter(
                df_filtrado,
                x='petal_length',
                y='petal_width',
                color='species',
                size='sepal_length',
                hover_data=['sepal_length', 'sepal_width'],
                title="Dispersión de pétalos",
                color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
            )
            fig2.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        # Histogramas y distribuciones
        st.markdown("### Distribución de características")
        
        caracteristica = st.selectbox(
            "Selecciona una característica:",
            ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'sepal_ratio', 'petal_ratio']
        )
        
        fig3 = px.histogram(
            df_filtrado,
            x=caracteristica,
            color='species',
            marginal='box',
            title=f"Distribución de {caracteristica}",
            color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
        )
        fig3.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab3:
        # Matriz de correlación
        st.markdown("### Matriz de correlación")
        
        # Seleccionar solo columnas numéricas
        columnas_numericas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'sepal_ratio', 'petal_ratio', 'total_area']
        matriz_corr = df_filtrado[columnas_numericas].corr()
        
        fig4 = px.imshow(
            matriz_corr,
            text_auto=True,
            aspect="auto",
            title="Correlación entre características",
            color_continuous_scale='RdBu'
        )
        st.plotly_chart(fig4, use_container_width=True)
    
    with tab4:
        # PYPLOT: Gráfico con matplotlib
        st.markdown("### Comparación por especies")
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f'Análisis comparativo - {titulo_especie}', fontsize=16, fontweight='bold')
        
        # Gráfico 1: Boxplot de longitud de sépalo
        sns.boxplot(data=df_filtrado, x='species', y='sepal_length', ax=axes[0,0], palette='Set2')
        axes[0,0].set_title('Longitud de Sépalo por especie')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Gráfico 2: Boxplot de ancho de sépalo
        sns.boxplot(data=df_filtrado, x='species', y='sepal_width', ax=axes[0,1], palette='Set2')
        axes[0,1].set_title('Ancho de Sépalo por especie')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # Gráfico 3: Boxplot de longitud de pétalo
        sns.boxplot(data=df_filtrado, x='species', y='petal_length', ax=axes[1,0], palette='Set2')
        axes[1,0].set_title('Longitud de Pétalo por especie')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # Gráfico 4: Boxplot de ancho de pétalo
        sns.boxplot(data=df_filtrado, x='species', y='petal_width', ax=axes[1,1], palette='Set2')
        axes[1,1].set_title('Ancho de Pétalo por especie')
        axes[1,1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

else:
    st.error("No se pueden generar gráficos: no hay datos disponibles con los filtros actuales.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin-top: 2rem;'>
    <h3>Dashboard Iris V2.0</h3>
    <p><strong>Desarrollado usando Streamlit</strong></p>
    <p>Dataset: Iris de Ronald Fisher (1936) | Visualizaciones interactivas con Plotly & Matplotlib</p>
    <p><em>¡Explora, filtra y descubre patrones en los datos!</em></p>
</div>
""", unsafe_allow_html=True)