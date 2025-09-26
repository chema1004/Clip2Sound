# 🎵 Clip2Sound - YouTube to MP3 Downloader

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Una aplicación moderna y elegante para descargar audio de YouTube en formato MP3, con interfaz de usuario intuitiva y sistema de autenticación.

## ✨ Características

- 🔐 **Sistema de autenticación** - Registro e inicio de sesión seguro
- 🎵 **Descarga de audio** - Convierte videos de YouTube a MP3 de alta calidad
- 📁 **Gestión de playlists** - Descarga listas de reproducción completas
- 📊 **Historial personalizado** - Seguimiento de todas tus descargas
- 🎨 **Interfaz moderna** - Diseño oscuro con CustomTkinter
- 💾 **Base de datos local** - Tus datos seguros y privados

## 🚀 Instalación Rápida

### Prerrequisitos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio:**
```bash
git clone https://github.com/tuusuario/clip2sound.git
cd clip2sound
```

2. **Instala las dependencias:**
```bash
pip install customtkinter yt-dlp pillow
```

3. **Ejecuta la aplicación:**
```bash
python main2.py
```

## 📦 Estructura del Proyecto

```
clip2sound/
├── main2.py          # Aplicación principal con interfaz gráfica
├── database.py       # Gestión de base de datos SQLite
├── downloader.py     # Lógica de descarga de YouTube
├── music_downloader.db # Base de datos (se crea automáticamente)
└── README.md         # Este archivo
```

## 🎮 Uso de la Aplicación

### 1. Registro e Inicio de Sesión
- Crea una nueva cuenta o inicia sesión con tus credenciales
- Los usuarios deben tener al menos 4 caracteres
- Las contraseñas deben tener al menos 6 caracteres

### 2. Descarga Individual
1. Pega la URL del video de YouTube
2. Haz clic en "Descargar Single"
3. El audio se guardará en tu carpeta de descargas

### 3. Descarga de Playlists
1. Pega la URL de la playlist de YouTube
2. Haz clic en "Descargar Playlist"
3. Todos los audios se descargarán automáticamente

### 4. Gestión de Archivos
- **Seleccionar Folder**: Elige dónde guardar tus archivos MP3
- **Ver Historial**: Consulta tu historial completo de descargas
- **Logout**: Cierra sesión de forma segura

## 🔧 Configuración Técnica

### Dependencias Principales
- **customtkinter**: Interfaz gráfica moderna
- **yt-dlp**: Descarga de contenido de YouTube
- **sqlite3**: Base de datos local
- **threading**: Descargas en segundo plano

### Características de Seguridad
- Contraseñas almacenadas de forma segura
- Base de datos local sin conexión a internet
- Validación de entradas de usuario

## 🐛 Solución de Problemas

### Error: "No module named 'customtkinter'"
```bash
pip install customtkinter
```

### Error: "No module named 'yt_dlp'"
```bash
pip install yt-dlp
```

### Las descargas no inician
- Verifica tu conexión a internet
- Asegúrate de que la URL de YouTube sea válida
- Comprueba los permisos de escritura en la carpeta de destino

## 📋 Requisitos del Sistema

- **Sistema Operativo**: Windows 10/11, macOS, Linux
- **Python**: Versión 3.11 o superior
- **Espacio en disco**: 100 MB mínimo
- **Memoria RAM**: 512 MB recomendados

## 🛠️ Desarrollo

### Ejecutar en modo desarrollo
```bash
# Clonar y configurar entorno
git clone https://github.com/tuusuario/clip2sound.git
cd clip2sound
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Estructura de código
```python
# Arquitectura MVC simplificada
- database.py    # Modelo (gestión de datos)
- downloader.py  # Controlador (lógica de negocio)  
- main2.py       # Vista (interfaz de usuario)
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## ⭐ Características Futuras

- [ ] Soporte para más plataformas (SoundCloud, Vimeo)
- [ ] Calidades de audio configurables
- [ ] Metadatos ID3 personalizables
- [ ] Sistema de colas de descarga
- [ ] Modo portable (ejecutable .exe)

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:

- Abre un [issue](https://github.com/tuusuario/clip2sound/issues)
- Contacta al desarrollador: ruisco04@gmail.com

---

**¿Te gusta Clip2Sound?** ¡Dale una estrella ⭐ al repositorio!

---

<div align="center">
  
**Hecho con ❤️ y Python**

</div>

## 📸 Capturas de Pantalla

*(Incluirías aquí imágenes de la interfaz, pero como no puedo subir archivos, puedes agregar:)*

```
📱 Interfaz de Login - Diseño oscuro moderno
📱 Ventana Principal - Panel de control intuitivo  
📱 Historial de Descargas - Lista organizada por fecha
```

¡Disfruta usando Clip2Sound! 🎧
