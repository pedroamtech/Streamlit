#!/bin/bash

# Script de configuración para proyecto Streamlit
# Autor: Pedro AM
# Fecha: octubre 2025

echo "🚀 Configurando proyecto Streamlit..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir mensajes coloridos
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar si Python está instalado
print_status "Verificando instalación de Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    print_status "Python encontrado: $PYTHON_VERSION"
    PYTHON_PATH=$(which python3)
    print_status "Ubicación de Python: $PYTHON_PATH"
else
    print_error "Python 3 no está instalado. Por favor instala Python 3.7 o superior."
    exit 1
fi

# Verificar si pip está instalado
print_status "Verificando pip..."
if command -v pip3 &> /dev/null; then
    print_status "pip3 encontrado"
else
    print_warning "pip3 no encontrado. Intentando instalar..."
    python3 -m ensurepip --upgrade
fi

# Función para solucionar problemas de certificados SSL en macOS
fix_ssl_certificates() {
    print_status "Solucionando problemas de certificados SSL..."
    
    # Instalar certificados
    print_status "Instalando certificados..."
    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m ensurepip --upgrade
    
    # Verificar si existe el archivo de certificados
    CERT_FILE="/Applications/Python 3.13/Install Certificates.command"
    if [ -f "$CERT_FILE" ]; then
        print_status "Actualizando certificados de Python..."
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 "$CERT_FILE"
    else
        print_warning "Archivo de certificados no encontrado en la ubicación esperada"
        print_status "Intentando abrir directamente..."
        open "/Applications/Python 3.13/Install Certificates.command" 2>/dev/null || print_warning "No se pudo abrir automáticamente"
    fi
}

# Detectar si estamos en macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    print_status "Sistema macOS detectado"
    read -p "¿Deseas ejecutar la corrección de certificados SSL? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        fix_ssl_certificates
    fi
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    print_status "Creando entorno virtual..."
    python3 -m venv venv
    print_status "Entorno virtual creado en ./venv"
else
    print_status "Entorno virtual ya existe"
fi

# Activar entorno virtual
print_status "Activando entorno virtual..."
source venv/bin/activate

# Actualizar pip
print_status "Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
print_status "Instalando dependencias desde requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    print_status "Dependencias instaladas correctamente"
else
    print_error "Archivo requirements.txt no encontrado"
    exit 1
fi

# Verificar instalación de Streamlit
print_status "Verificando instalación de Streamlit..."
if python -c "import streamlit" &> /dev/null; then
    STREAMLIT_VERSION=$(streamlit version | head -n 1)
    print_status "Streamlit instalado correctamente: $STREAMLIT_VERSION"
else
    print_error "Error al verificar Streamlit"
    exit 1
fi

echo ""
print_status "🎉 ¡Configuración completada exitosamente!"
echo ""
echo "Para usar el proyecto:"
echo "1. Activa el entorno virtual: source venv/bin/activate"
echo "2. Ejecuta el dashboard: streamlit run dashboard.py"
echo "3. O ejecuta hello-world: streamlit run hello-world.py"
echo ""
print_status "Las aplicaciones se abrirán en http://localhost:8501"