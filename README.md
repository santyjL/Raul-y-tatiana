# Por Siempre Raúl y Tatiana

Un espacio digital creado para preservar, compartir y revivir los recuerdos de un día inolvidable.

Este proyecto funciona como una cápsula de recuerdos accesible desde cualquier dispositivo, permitiendo centralizar fotografías, mensajes, momentos especiales y contenido multimedia en un único lugar.

## Objetivo

La idea principal detrás de este proyecto es transformar una colección de recuerdos dispersos en una experiencia web elegante, accesible y permanente.

Más que una simple galería de imágenes, busca convertirse en un homenaje digital que permita conservar momentos importantes a través de una interfaz moderna y responsiva.

---
## Filosofía del Proyecto

Este proyecto nació con una idea sencilla:

> Conservar para siempre recuerdos que merecen permanecer accesibles en cualquier momento.
La tecnología utilizada no es el objetivo principal, sino el medio para transformar momentos importantes en una experiencia digital permanente.

---
## 🛠 Tecnologías Utilizadas

### Frontend
[![HTML5](https://img.shields.io/badge/HTML5-orange?style=for-the-badge&logo=html5&logoColor=white&labelColor=101010)]()
[![CSS3](https://img.shields.io/badge/Css3-blue?style=for-the-badge&logo=css&logoColor=white&labelColor=101010)]()
[![Reflex](https://img.shields.io/badge/Reflex0.9.3-violet?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)]()

### Backend

[![python](https://img.shields.io/badge/Python3.12-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)]()
[![Reflex](https://img.shields.io/badge/Reflex0.9.3-violet?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)]()

### Infraestructura

[![docker](https://img.shields.io/badge/Docker-skyblue?style=for-the-badge&logo=docker&logoColor=white&labelColor=101010)]()
[![Reiway](https://img.shields.io/badge/reilway-black?style=for-the-badge&logo=railway&logoColor=white&labelColor=101010)]()
[![Vercel](https://img.shields.io/badge/vercel-black?style=for-the-badge&logo=vercel&logoColor=white&labelColor=101010)]()

### Gestión de Dependencias

* pip
* requirements.txt
* reflex.lock

---

## 📂 Estructura del Proyecto

```text
.
├── assets/
├── public/
├── por_siempre_raul_y_tatiana/
├── requirements.txt
├── reflex.lock
├── rxconfig.py
├── dockerfile
├── build.sh
└── README.md
```

### Descripción de Directorios

| Carpeta                    | Propósito                                       |
| -------------------------- | ----------------------------------------------- |
| assets                     | Recursos estáticos utilizados por la aplicación |
| public                     | Archivos públicos servidos directamente         |
| por_siempre_raul_y_tatiana | Código principal de la aplicación Reflex        |
| dockerfile                 | Configuración para contenedores Docker          |
| build.sh                   | Script de construcción para despliegue          |
| rxconfig.py                | Configuración principal de Reflex               |

## Comandos Útiles de Reflex

### Ejecutar modo desarrollo

```bash
reflex run
```

### Ejecutar backend y frontend por separado

```bash
reflex run --backend-only
```

```bash
reflex run --frontend-only
```

### Exportar versión de producción

```bash
reflex export
```

### Inicializar proyecto

```bash
reflex init
```

### Actualizar dependencias de Reflex

```bash
reflex install
```

---

## Despliegue con Docker

### Construir imagen

```bash
docker build -t raul-y-tatiana .
```

### Ejecutar contenedor

```bash
docker run -p 8000:8000 raul-y-tatiana
```

---

## Despliegue en Railway

Railway detecta automáticamente la configuración Docker del proyecto.

### Pasos

1. Crear un nuevo proyecto en Railway.
2. Conectar el repositorio de GitHub.
3. Railway construirá la imagen utilizando el Dockerfile.
4. Desplegar automáticamente.

Variables recomendadas:

```env
PORT=8000
```

---

## ▲ Despliegue en Vercel

La versión pública del proyecto se encuentra desplegada en Vercel.

El flujo de despliegue es:

```text
GitHub
   ↓
Vercel
   ↓
Deploy automático
```
Cada push realizado a la rama principal genera una nueva compilación y despliegue.

---


